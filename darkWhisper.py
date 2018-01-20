
"""tell if dif >= 16"""
from coinbaseAPI import Coinbase
from bxAPI import Bx
from exchange import toTHB
from time import sleep
import pendulum

coinB = Coinbase('https://api.coinbase.com/v2/')
bx = Bx('https://bx.in.th/api/')

def main():
    oldPerGain = 0
    while True:
        sleep(1)
        buysgd = coinB.getBuyPriceLTC()
        sellthb = bx.getLTCSell()
        buysgd_thb = toTHB(buysgd)
        # perLTC = (sellthb-buysgd_thb)
        perGain = (sellthb-buysgd_thb)/buysgd_thb

        if oldPerGain!= perGain:
            print(f"{pendulum.now().to_time_string()} %gain:  {perGain}")
            oldPerGain = perGain

if __name__ == '__main__':
    main()