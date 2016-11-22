"""
We provide an attribute based DSL for converting attributes into the fields
dictionary, with a classmethod for creating a create_spec object for the class.

So we can define something like:

.. code-block:: python

    class MyAmazingKls(dictobj.Spec):
        one = dictobj.Field(string_spec)
        two = dictobj.Field(string_spec, wrapper=listof)
        three = dictobj.NullableField(string_spec)

Which is equivalent to

.. code-block:: python

    class MyAmazingKls(six.with_metaclass(Field.metaclass, dictobj)):
        one = Field(string_spec)
        two = Field(string_spec, wrapper=listof)
        three = Field(string_spec, nullable=True)

Which is equivalent to:

.. code-block:: python

    class MyAmazingKls(dictobj, Field.mixin):
        fields = {"one": string_spec, "two": listof(string_spec()), "three": defaulted(or_spec(none_spec(), string_spec()), None)}

and have MyAmazingKls.FieldSpec().normalise for normalising a
dictionary into an instance of MyAmazingKls!
"""

from input_algorithms.spec_base import create_spec, formatted, defaulted, NotSpecified, none_spec, or_spec
from input_algorithms.errors import BadSpec
from input_algorithms.meta import Meta

import six

class FieldSpec(object):
    """
    Responsible for defining the Spec object used to convert a
    dictionary into an instance of the kls.
    """
    def __init__(self, kls, formatter=None, create_kls=None):
        self.kls = kls
        self.create_kls = create_kls or kls
        self.formatter = formatter

    def make_spec(self, meta):
        """
        Assume self.kls has a fields dictionary of

        fields = {name: (description, options)}

        or

        fields = {name: options}

        Where options may be:

          * A callable object to a spec or Field
          * A spec
          * A Field

        If it's a Field, we create a spec from that

        Finally we create a create_spec with all the fields
        """
        kwargs = {}
        errors = []
        if not hasattr(self.kls, "fields"):
            raise BadSpec("No fields on the class!", kls=self.kls)

        for name, options in sorted(self.kls.fields.items()):
            if type(options) in (tuple, list):
                if len(options) == 2:
                    options = options[1]
                elif len(options) == 1:
                    options = options[0]

            if not options or isinstance(options, six.string_types):
                errors.append(BadSpec("No spec found for option", option=name, meta=meta.at(name)))

            if callable(options):
                options = options()

            spec = None
            if isinstance(options, Field):
                try:
                    spec = options.make_spec(meta.at(name), self.formatter)
                except BadSpec as error:
                    errors.append(error)
            else:
                spec = options

            # And set our field
            kwargs[name] = spec

        if errors:
            raise BadSpec(_errors=errors)

        return create_spec(self.create_kls, **kwargs)

    def normalise(self, meta, val):
        """Normalise val with the spec from self.make_spec"""
        return self.make_spec(meta).normalise(meta, val)

    def empty_normalise(self, **kwargs):
        """Normalise val with the spec from self.make_spec"""
        return self.normalise(Meta.empty(), kwargs)

class FieldSpecMixin(object):
    """
    Mixin to give FieldSpec to an object

    class MyAmazingKls(FieldSpecMixin):
        fields = {...}

    And have MyAmazingKls.FieldSpec(formatter=...)
    create a Spec object that normalises a dictionary into an instance
    of this class
    """
    FieldSpec = classmethod(FieldSpec)

class FieldSpecMetakls(type):
    """
    A metaclass that converts attributes into a fields dictionary
    at class creation time.

    It looks for any attributes on the class that have an attibute of
    "is_input_algorithms_field" that is a Truthy value

    It will then:

      * Ensure FieldSpecMixin is one of the base classes
      * There is a fields dictionary containing all the defined Fields
    """
    def __new__(metaname, classname, baseclasses, attrs):
        fields = {}
        for name, options in attrs.items():
            if getattr(options, "is_input_algorithms_field", False):
                if options.help:
                    fields[name] = (options.help, options)
                else:
                    fields[name] = options

        attrs['fields'] = fields

        if Field.mixin not in baseclasses:
            baseclasses = baseclasses + (Field.mixin, )

        return type.__new__(metaname, classname, baseclasses, attrs)

class Field(object):
    """
    Representation of a single Field

    This has a reference to the mixin and metaclass in this file.

    It also let's you define things like:

      * Whether this is a formatted field
      * has a default
      * Is wrapped by some other spec class
    """
    mixin = FieldSpecMixin
    metaclass = FieldSpecMetakls
    is_input_algorithms_field = True

    def __init__(self, spec
        , help=None
        , formatted=False
        , wrapper=NotSpecified
        , default=NotSpecified
        , nullable=False
        ):
        self.spec = spec
        self.help = help
        self.default = default
        self.wrapper = wrapper
        self.nullable = nullable
        self.formatted = formatted

    def clone(self, **overrides):
        return self.__class__(self.spec
            , help = overrides.get("help", self.help)
            , formatted = overrides.get("formatted", self.formatted)
            , wrapper = overrides.get("wrapper", self.wrapper)
            , default = overrides.get("default", self.default)
            , nullable = overrides.get("nullable", self.nullable)
            )

    def make_spec(self, meta, formatter):
        """
        Create the spec for this Field:

          * If callable, then call it
          * if it has a default, wrap in defaulted
          * If it can be formatted, wrap in formatted
          * If it has a wrapper, wrap it with that
          * Return the result!
        """
        spec = self.spec
        if callable(spec):
            spec = spec()

        if self.nullable:
            spec = defaulted(or_spec(none_spec(), spec), None)

        if self.default is not NotSpecified:
            spec = defaulted(spec, self.default)

        if self.formatted:
            if formatter is None:
                raise BadSpec("Need a formatter to be defined", meta=meta)
            else:
                spec = formatted(spec, formatter=formatter)

        if self.wrapper is not NotSpecified:
            spec = self.wrapper(spec)

        return spec

class NullableField(Field):
    is_input_algorithms_field = True

    def __init__(self, spec, **kwargs):
        kwargs["nullable"] = True
        super(NullableField, self).__init__(spec, **kwargs)

