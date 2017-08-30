import json
import urllib.request
from urllib.request import Request, urlopen

class bithumb:
    urlTicker = urllib.request.urlopen('https://api.bithumb.com/public/ticker/all')
    readTicker = urlTicker.read().decode('utf-8')
    jsonTicker = json.loads(readTicker)
    FindBTC = jsonTicker['data']['BTC']['closing_price']
    BTC = int(FindBTC)
    FindETH = jsonTicker['data']['ETH']['closing_price']
    ETH = int(FindETH)
    FindDASH = jsonTicker['data']['DASH']['closing_price']
    DASH = int(FindDASH)
    FindLTC = jsonTicker['data']['LTC']['closing_price']
    LTC = int(FindLTC)
    FindETC = jsonTicker['data']['ETC']['closing_price']
    ETC = int(FindETC)
    FindXRP = jsonTicker['data']['XRP']['closing_price']
    XRP = int(FindXRP)

class coinone:
    urlTicker = urllib.request.urlopen('https://api.coinone.co.kr/ticker/?currency=all')
    readTicker = urlTicker.read().decode('utf-8')
    jsonTicker = json.loads(readTicker)
    FindETC = jsonTicker['etc']['last']
    ETC = int(FindETC)
    FindBTC = jsonTicker['btc']['last']
    BTC = int(FindBTC)
    FindETH = jsonTicker['eth']['last']
    ETH = int(FindETH)
    FindXRP = jsonTicker['xrp']['last']
    XRP = int(FindXRP)

class korbit:
    reqBTC = Request('https://api.korbit.co.kr/v1/ticker?currency_pair=btc_krw' , headers={'User-Agent': 'Mozilla/5.0'})
    readBTC = urlopen(reqBTC).read().decode('utf-8')
    jsonBTC = json.loads(readBTC)
    FindBTC = jsonBTC['last']
    BTC = int(FindBTC)
    reqETH = Request('https://api.korbit.co.kr/v1/ticker?currency_pair=eth_krw' , headers={'User-Agent': 'Mozilla/5.0'})
    readETH = urlopen(reqETH).read().decode('utf-8')
    jsonETH = json.loads(readETH)
    FindETH = jsonETH['last']
    ETH = int(FindETH)
    reqETC = Request('https://api.korbit.co.kr/v1/ticker?currency_pair=etc_krw' , headers={'User-Agent': 'Mozilla/5.0'})
    readETC = urlopen(reqETC).read().decode('utf-8')
    jsonETC = json.loads(readETC)
    FindETC = jsonETC['last']
    ETC = int(FindETC)
    reqXRP = Request('https://api.korbit.co.kr/v1/ticker?currency_pair=xrp_krw' , headers={'User-Agent': 'Mozilla/5.0'})
    readXRP = urlopen(reqXRP).read().decode('utf-8')
    jsonXRP = json.loads(readXRP)
    FindXRP = jsonXRP['last']
    XRP = int(FindXRP)