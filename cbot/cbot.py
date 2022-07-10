import utils
import bybit
import cfg

import time
from flask import Flask, request, abort

app = Flask(__name__)
app.testing = True

myBybit = bybit.bybit()

# webhooks that receives tf signals
@app.route('/btc_10m_3', methods=['POST'])
def btc_10m_3():
	print("[bot] signal btc-10m-3 received")

	dictionary = request.get_json(force=True)
	print("[json]:", dictionary)
	
	cfg.qty10m = utils.get_qty(3, 110, '10m', myBybit.get_current_price())

	if dictionary["secret"] == cfg.strategy_secret:
		if dictionary["command"] == "openlong":
			print("[bot] opened LONG with qty:", cfg.qty10m)
			myBybit.market_buy(False, cfg.qty10m)

		if dictionary["command"] == "openshort":
			print("[bot] opened SHORT with qty:", cfg.qty10m)
			myBybit.market_sell(False, cfg.qty10m)
        
		if dictionary["command"] == "closelong":
			print("[bot] closed LONG\n")
			myBybit.market_sell(True, cfg.qty10m)

		if dictionary["command"] == "closeshort":
			print("[bot] closed SHORT\n")
			myBybit.market_buy(True, cfg.qty10m)
	else:
		print("[bot] no secret-key given:", dictionary)

	print("-----------------------------")
	return { "success": False, "message": "invalid"}

@app.route('/btc_15m_1', methods=['POST'])
def btc_15m_1():
	print("[bot] signal btc-15m-1 received")

	dictionary = request.get_json(force=True)
	print("[json]:", dictionary)
	
	cfg.qty15m = utils.get_qty(3, 110, '15m', myBybit.get_current_price())

	if dictionary["secret"] == cfg.strategy_secret:
		if dictionary["command"] == "openlong":
			print("[bot] opened LONG with qty:", cfg.qty15m)
			myBybit.market_buy(False, cfg.qty15m)

		if dictionary["command"] == "openshort":
			print("[bot] opened SHORT with qty:", cfg.qty15m)
			myBybit.market_sell(False, cfg.qty15m)

		if dictionary["command"] == "closelong":
			print("[bot] closed LONG\n")
			myBybit.market_sell(True, cfg.qty15m)

		if dictionary["command"] == "closeshort":
			print("[bot] closed SHORT\n")
			myBybit.market_buy(True, cfg.qty15m)
	else:
		print("[bot] no secret-key given:", dictionary)

	print("-----------------------------")
	return { "success": False, "message": "invalid"}

@app.route('/btc_15m_2', methods=['POST'])
def btc_15m_2():
	print("[bot] signal btc-15m-2 received")

	dictionary = request.get_json(force=True)
	print("[json]:", dictionary)
	
	cfg.qty15m_2 = utils.get_qty(3, 110, '15m', myBybit.get_current_price())

	if dictionary["secret"] == cfg.strategy_secret:
		if dictionary["command"] == "openlong":
			print("[bot] opened LONG with qty:", cfg.qty15m_2)
			myBybit.market_buy(False, cfg.qty15m_2)

		if dictionary["command"] == "openshort":
			print("[bot] opened SHORT with qty:", cfg.qty15m_2)
			myBybit.market_sell(False, cfg.qty15m_2)

		if dictionary["command"] == "closelong":
			print("[bot] closed LONG\n")
			myBybit.market_sell(True, cfg.qty15m_2)

		if dictionary["command"] == "closeshort":
			print("[bot] closed SHORT\n")
			myBybit.market_buy(True, cfg.qty15m_2)
	else:
		print("[bot] no secret-key given:", dictionary)

	print("-----------------------------")
	return { "success": False, "message": "invalid"}

# start srv
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)