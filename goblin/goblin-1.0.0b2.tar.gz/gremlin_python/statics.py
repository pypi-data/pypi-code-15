'''
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.
'''
from aenum import Enum

staticMethods = {}
staticEnums = {}
default_lambda_language = "gremlin-python"


class long(int): pass


def add_static(key, value):
    if isinstance(value, Enum):
        staticEnums[key] = value
    else:
        staticMethods[key] = value


def load_statics(global_dict):
    for key in staticMethods:
        global_dict[key] = staticMethods[key]
    for key in staticEnums:
        global_dict[key] = staticEnums[key]


def unload_statics(global_dict):
    for key in staticMethods:
        if key in global_dict:
            del global_dict[key]
    for key in staticEnums:
        if key in global_dict:
            del global_dict[key]
