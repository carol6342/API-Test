#! /usr/bin/env python
# XCoin API-call sample script (for Python 3.X)
#
# @author	btckorea
# @date	2017-04-11
#
#
# First, Build and install pycurl with the following commands::
# (if necessary, become root)
#
# https://pypi.python.org/pypi/pycurl/7.43.0#downloads
#
# tar xvfz pycurl-7.43.0.tar.gz
# cd pycurl-7.43.0
# python setup.py --libcurl-dll=libcurl.so install
# python setup.py --with-openssl install
# python setup.py install

import sys
from price import *
from bithumb_api import *
from polonix_api import *
from bitrex_api import *
import pprint





#
# public api
#
# /public/ticker
# /public/recent_ticker
# /public/orderbook
# /public/recent_transactions


#
# private api
#
# endpoint		=> parameters
# /info/current
# /info/account
# /info/balance
# /info/wallet_address

#result = api.xcoinApiCall("/info/account", rgParams);
#print("status: " + result["status"]);
#print("created: " + result["data"]["created"]);
#print("account id: " + result["data"]["account_id"]);
#print("trade fee: " + result["data"]["trade_fee"]);
#print("balance: " + result["data"]["balance"]);


#bithumb

api_key = "api_connect_key";
api_secret = "api_secret_key";
"""
api = BithumbAPI(api_key, api_secret);

rgParams = {
	#"group_orders" : "1",
	#"count" : "30"
};
result = api.BithumbAPICall("/public/ticker/BTC", rgParams);
print("BTC_Opening: " + result["data"]["opening_price"]);
print("BTC_Closing: " + result["data"]["closing_price"]);
print("BTC_Min: " + result["data"]["min_price"]);
print("BTC_Max: " + result["data"]["max_price"]);
print("BTC_Avg: " + result["data"]["average_price"]);
print("BTC_units_traded: " + result["data"]["units_traded"]);
print("BTC_volume_1day: " + result["data"]["volume_1day"]);
print("BTC_volume_7day: " + result["data"]["volume_7day"]);
print("BTC_Buy: " + result["data"]["buy_price"]);
print("BTC_Sell: " + result["data"]["sell_price"]);
"""




#poloniex
"""
api = poloniex(api_key, api_secret);

rgParams = {
	#"group_orders" : "1",
	#"count" : "30"
};

result=api.api_query("returnTicker",rgParams);
print("last: " + result["BTC_ETH"]["last"]);
print("lowestAsk: " + result["BTC_ETH"]["lowestAsk"]);
print("highestBid: " + result["BTC_ETH"]["highestBid"]);
print("percentChange: " + result["BTC_ETH"]["percentChange"]);
print("baseVolume: " + result["BTC_ETH"]["baseVolume"]);
print("quoteVolume: " + result["BTC_ETH"]["quoteVolume"]);
print("USDT_BTC: " + result["USDT_BTC"]["last"]);
"""

api = Bittrex(api_key, api_secret);

rgParams = {
	"market" : "BTC-ETH",
	#"count" : "30"
};


result=api.api_query("getmarketsummary",rgParams);
#print("last: " + result["result"]["Last"]);
for i in range(len(result['result'])):
	if result['result'][i]['MarketName'] == 'BTC-ETH':
		print (result['result'][i]);

sys.exit(0);

