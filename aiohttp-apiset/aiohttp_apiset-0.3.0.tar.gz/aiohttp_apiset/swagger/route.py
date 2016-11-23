import asyncio
from collections.abc import Mapping

from aiohttp import web, multidict

from ..dispatcher import Route
from .validate import convert, validator
from .loader import deref
from .operations import get_docstring_swagger


class SwaggerRoute(Route):
    """
    :param method: as well as in aiohttp
    :param handler: as well as in aiohttp
    :param resource: as well as in aiohttp
    :param expect_handler: as well as in aiohttp
    :param location: SubLocation instance
    :param swagger_data: data
    """
    def __init__(self, method, handler, resource, *,
                 expect_handler=None, location=None, swagger_data=None):
        super().__init__(method, handler,
                         expect_handler=expect_handler,
                         resource=resource, location=location)
        self._parameters = {}
        self._required = []
        swagger_op = get_docstring_swagger(handler)
        if swagger_op:
            self._swagger_data = swagger_op
            self.is_built = True
            self.build_swagger_data({})
        else:
            self._swagger_data = swagger_data
            self.is_built = False

    def build_swagger_data(self, swagger_schema):
        """ Prepare data when schema loaded

        :param swagger_schema: loaded schema
        """
        self.is_built = True
        self._required = []
        self._parameters = {}
        if not self._swagger_data:
            return
        self._swagger_data = deref(self._swagger_data, swagger_schema)
        for param in self._swagger_data.get('parameters', ()):
            p = param.copy()
            name = p.pop('name')
            self._parameters[name] = p
            if p.pop('required', False):
                self._required.append(name)
            if 'schema' in p:
                p.update(p.pop('schema'))

    @asyncio.coroutine
    def handler(self, request):
        parameters, errors = yield from self.validate(request)

        if errors:
            raise web.HTTPBadRequest(reason=errors)

        request.update(parameters)

        parameters['request'] = request
        kwargs = {
            k: parameters.get(k)
            for k in self._handler_args
        }

        response = yield from self._handler(**kwargs)
        return response

    def _validate(self, data, errors):
        return data

    @asyncio.coroutine
    def validate(self, request: web.Request):
        """ Returns parameters extract from request and multidict errors

        :param request: Request
        :return: tuple of parameters and errors
        """
        parameters = {}
        files = {}
        errors = multidict.MultiDict()

        if request.method not in request.POST_METHODS:
            body = None
        elif request.content_type in (
                'application/x-www-form-urlencoded',
                'multipart/form-data'):
            try:
                body = yield from request.post()
            except Exception:
                body = Exception('Bad form')
        elif request.content_type == 'application/json':
            try:
                body = yield from request.json()
            except Exception:
                body = Exception('Bad json')
        else:
            body = None

        for name, param in self._parameters.items():
            where = param['in']
            vtype = param['type']
            is_array = vtype == 'array'

            if where == 'query':
                source = request.GET
            elif where == 'header':
                source = request.headers
            elif where == 'path':
                source = request.match_info
            elif body is None:
                source = ()
            elif where == 'formData':
                source = body
            elif where == 'body':
                if isinstance(body, BaseException):
                    errors.add(name, str(body))
                else:
                    parameters[name] = body
                continue
            else:
                raise ValueError(where)

            if is_array and hasattr(source, 'getall'):
                value = source.getall(name, [])
            elif isinstance(source, Mapping) and name in source \
                    and (vtype not in ('number', 'integer') or source[name]):
                value = source[name]
            elif 'default' in param:
                parameters[name] = param['default']
                continue
            elif name in self._required:
                errors.add(name, 'Required')
                if isinstance(source, BaseException):
                    errors.add(name, str(body))
                continue
            else:
                continue

            if is_array:
                vtype = param['items']['type']
                vformat = param['items'].get('format')
            else:
                vformat = param.get('format')

            if source is body and isinstance(body, dict):
                pass
            elif vtype not in ('string', 'file'):
                value = convert(name, value, vtype, vformat, errors)

            if vtype == 'file':
                files[name] = value
            else:
                parameters[name] = value

        parameters = self._validate(parameters, errors)
        parameters.update(files)
        return parameters, errors


class SwaggerValidationRoute(SwaggerRoute):
    def build_swagger_data(self, swagger_schema):
        super().build_swagger_data(swagger_schema)
        schema = {
            'type': 'object',
            'properties': self._parameters,
        }
        self._validate = validator(schema)


def route_factory(method, handler, resource, *,
                  expect_handler=None, **kwargs):
    if kwargs.get('swagger_data') is None:
        return Route(method, handler, resource=resource,
                     expect_handler=expect_handler)

    elif kwargs.get('validate') is True:
        route_class = SwaggerValidationRoute
    else:
        route_class = SwaggerRoute

    route = route_class(method, handler, resource=resource,
                        expect_handler=expect_handler,
                        swagger_data=kwargs['swagger_data'])
    return route
