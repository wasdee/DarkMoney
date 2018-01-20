import uplink
import json
from box import Box

class Bx(uplink.Consumer):

    @uplink.timeout(10)
    @uplink.get('')
    def _getTicker(self): pass

    def getLTCSell(self):
        response = self._getTicker()
        tickers = json.loads(response.text)

        # for pair_id scaning
        # LTC_tickers = [t for _, t in tickers.items() if t['primary_currency'] == 'LTC' or t['secondary_currency'] == 'LTC']

        LTC = tickers['30']
        LTC = Box(LTC)
        assert LTC.primary_currency == 'THB'
        assert LTC.secondary_currency == 'LTC'

        return LTC.orderbook.asks.highbid

        pass



if __name__ == '__main__':

    a = Bx('https://bx.in.th/api/')
    a.getLTCSell()