# Copyright (c) 2016. Mount Sinai School of Medicine
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

__all__ = ['utils', 'models', 'sim']

import sys as _sys
if (_sys.version_info > (3, 0)):
    # Python 3 code in this block
    from .survivalstan import *
    from . import utils, models, sim
    __all__ = ['utils', 'models', 'sim']
else:
    import utils
    import models
    import sim
    from survivalstan import *

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
