from pymongo import MongoClient
from coinbaseAPI import Coinbase
from bxAPI import Bx
from time import sleep
import os

client = MongoClient()
db = client['darkMoney']
collectionBx = db['bx']
collectionCoinbase = db['coinbase']

def bxRoutine():
    while True:
        bx = Bx.startDefault()
        while True:
            sleep(10)
            try:
                data = bx.getAll()
                collectionBx.insert_one(data)
            except Exception as e:
                desc = vars(e)
                collectionBx.insert_one(desc)
                print(e)

def coinbaseRoutine():
    while True:
        try:
            cb = Coinbase.startDefault()
            while True:
                sleep(10)
                try:
                    data = cb.getBuyPrices()
                    collectionBx.insert_one(data)
                except Exception as e:
                    desc = vars(e)
                    collectionBx.insert_one(desc)
                    raise e
        except Exception as e:
            raise e

if __name__ == '__main__':
    if os.fork():
        coinbaseRoutine()
    else:
        bxRoutine()