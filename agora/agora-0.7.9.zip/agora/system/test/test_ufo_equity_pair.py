###############################################################################
#
#   Agora Portfolio & Risk Management System
#
#   Copyright 2015 Carlo Sbraccia
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
###############################################################################

from onyx.core import GetVal, OnyxTestCase

import agora.system.ufo_equity_pair as ufo_equity_pair
import unittest


###############################################################################
class UnitTest(OnyxTestCase):
    # -------------------------------------------------------------------------
    def setUp(self):
        super().setUp()
        ufo_equity_pair.prepare_for_test()

    def test_config(self):
        self.assertEqual("EQ SSE LN",
                         GetVal("EQP SSE LN - CNA LN", "Symbol1"))
        self.assertEqual("EQ CNA LN",
                         GetVal("EQP SSE LN - CNA LN", "Symbol2"))

    def test_Ratio(self):
        pass
#        print(GetVal("PAIR SSE LN - CNA LN", "Ratio", None, None))


if __name__ == "__main__":
    from onyx.core import UseEphemeralDbs
    with UseEphemeralDbs():
        unittest.main(failfast=True)
