from uplink import Consumer, get, headers, Path, Query, timeout
import uplink
import json as json
from box import Box

@headers({'CB_VERSION': "2018-01-15"})
class Coinbase(Consumer):

    @timeout(10)
    @get('prices/LTC-SGD/buy')
    def _getBuyPriceLTC(self): pass

    def getBuyPriceLTC(self):
        response = self._getBuyPriceLTC()
        price = json.loads(response.text)
        price = Box(price['data'])
        assert price.base == 'LTC'
        assert price.currency == 'SGD'
        return float(price.amount)


if __name__ == '__main__':
    a = Coinbase('https://api.coinbase.com/v2/')
    b = a.getBuyPriceLTC()
    print(b)