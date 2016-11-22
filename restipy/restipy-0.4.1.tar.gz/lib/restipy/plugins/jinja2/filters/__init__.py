from restipy.renderer import SilentUndefined

import jmespath as _jmespath
import yaml as _yaml
import json as _json

def jmespath(data, expr, **kwargs):
    return _jmespath.search(expr, data, kwargs)

def yaml(data, **kwargs):
    if type(data) is SilentUndefined:
        return

    return _yaml.dump(data)

def json(data, **kwargs):
    return _json.dumps(data, kwargs)
