# -*- coding: utf-8 -*-
# Copyright 2016 Yelp Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
"""
Utility methods for manipulating lists.
"""
from __future__ import absolute_import
from __future__ import unicode_literals


def unlist(a_list):
    """Convert the (possibly) single item list into a single item"""
    if len(a_list) > 1:
        raise ValueError(len(a_list))

    if len(a_list) == 0:
        return None
    else:
        return a_list[0]
