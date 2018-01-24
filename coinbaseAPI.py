from uplink import Consumer, get, headers, Path, Query, timeout
import uplink
import json as json
from box import Box
from itertools import product

CRIPTOS = ['ETH', 'BCH', 'BTC', 'LTC']
CURRENCYS = ['USD',"SGD"]


@headers({'CB_VERSION': "2018-01-15"})
class Coinbase(Consumer):
    @classmethod
    def startDefault(cls):
        return cls('https://api.coinbase.com/v2/')

    @timeout(10)
    @get('prices/LTC-SGD/buy')
    def _getBuyPriceLTC(self): pass

    @timeout(10)
    @get('prices/{cripto}-{currency}/buy')
    def _getBuyPrice(self,cripto,currency): pass

    def getBuyPrice(self,cripto, currency):
        response = self._getBuyPrice(cripto,currency)
        price = json.loads(response.text)
        return price

    def getBuyPrices(self):
        all = []
        for pair in product(CRIPTOS, CURRENCYS):
            b = self.getBuyPrice(*pair)
            print(b)
            all.append(b)
        return {'all':all}

    def getBuyPriceLTC(self):
        response = self._getBuyPriceLTC()
        price = json.loads(response.text)
        price = Box(price['data'])
        assert price.base == 'LTC'
        assert price.currency == 'SGD'
        return float(price.amount)



if __name__ == '__main__':
    a = Coinbase.startDefault()
