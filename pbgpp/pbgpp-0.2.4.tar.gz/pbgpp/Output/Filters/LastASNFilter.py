#
# This file is part of PCAP BGP Parser (pbgpp)
#
# Copyright 2016 DE-CIX Management GmbH
# Author: Tobias Hannaske <tobias.hannaske@de-cix.net>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from pbgpp.Output.Filter import BGPFilter
from pbgpp.BGP.Statics import BGPStatics


# @todo Verify functionality
class LastASNFilter(BGPFilter):
    def __init__(self, values=[]):
        BGPFilter.__init__(self, values)

    def apply(self, message):
        try:
            # AS_PATH is a path attribute of BGP UPDATE message
            # Therefore we first need to make that we are currently handling an UPDATE message
            if message.type is not BGPStatics.MESSAGE_TYPE_UPDATE:
                # Skip messages that are no UPDATE messages
                return None

            for attribute in message.path_attributes:
                # Skip attributes that are no NEXT_HOP attributes
                if attribute.type is not BGPStatics.UPDATE_ATTRIBUTE_AS_PATH:
                    continue

                for path_segment in attribute.path_segments:
                    segment_asn = path_segment.segments[-1:]
                    for value in self.values:
                        if str(segment_asn[0]) == str(value):
                            return message

                        # Negative filtering using ~ character
                        if value[0:1] == "~" and (str(segment_asn[0]) != str(value[1:])):
                            return message

            # Searched value was not found
            return None
        except Exception as e:
            # On error the filtering was not successful (due to wrong fields, etc.)
            return None
