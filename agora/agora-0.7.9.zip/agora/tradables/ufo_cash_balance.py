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

from onyx.core import ValueType, ReferenceField
from agora.corelibs.tradable_api import TradableObj

__all__ = ["CashBalance"]


###############################################################################
class CashBalance(TradableObj):
    """
    Tradable class that represents a cash amount in a given currrency.
    """
    Currency = ReferenceField(obj_type="Currency")

    # -------------------------------------------------------------------------
    @ValueType()
    def MktVal(self, graph):
        return 1.0

    # -------------------------------------------------------------------------
    @ValueType()
    def MktValUSD(self, graph):
        return graph("{0:3s}/USD".format(graph(self, "Currency")), "Spot")

    # -------------------------------------------------------------------------
    @property
    def ImpliedName(self):
        return "CASH {0:3s}".format(self.Currency)


# -----------------------------------------------------------------------------
def prepare_for_test():
    from agora.corelibs.tradable_api import AddByInference
    import agora.system.ufo_database as ufo_database
    import agora.system.ufo_holiday_calendar as ufo_holiday_calendar
    import agora.system.ufo_currency as ufo_currency
    import agora.system.ufo_currency_cross as ufo_currency_cross

    ufo_database.prepare_for_test()
    ufo_holiday_calendar.prepare_for_test()
    ufo_currency.prepare_for_test()
    ufo_currency_cross.prepare_for_test()

    securities = []
    for ccy in ["USD", "EUR", "GBP"]:
        securities.append(AddByInference(CashBalance(Currency=ccy)))

    return [sec.Name for sec in securities]
