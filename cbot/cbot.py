from bot_all import set_quantity
import utils
import bybit
import cfg

import time
from flask import Flask, request, abort

app = Flask(__name__)

myBybit = bybit.bybit()

# position settings
qty15m = 0
qty30m = 0

# webhook that receives tf signals
@app.route('/webhook30m', methods=['POST'])
def webhook30m():
	print("[BOT] Webhook 30m received")

	dictionary = request.get_json(force=True)
	print("[JSON]:", dictionary)

        global qty30m = utils::utils.get_qty(6, 100, '30m', myBybit.get_current_price())

	if dictionary["secret"] == cfg.strategy_secret:
		if dictionary["command"] == "openlong":
			print("[BOT] Opened LONG with qty:", set_quantity(6, 100, '30m'))
			myBybit.market_buy(False, '30m')

		if dictionary["command"] == "openshort":
			print("[BOT] Opened SHORT with qty:", set_quantity(6, 100, '30m'))
			bybit_sell(False, '30m')
        
		if dictionary["command"] == "closelong":
			print("[BOT] Closing LONG\n")
			bybit_sell(True, '30m')

		if dictionary["command"] == "closeshort":
			print("[BOT] Closing SHORT\n")
			bybit_buy(True, '30m')
	else:
		print("[BOT] NO SECRET:", dictionary)

	print("-----------------------------")
	return { "success": False, "message": "invalid"}

@app.route('/webhook15m', methods=['POST'])
def webhook15m():
	print("[BOT] Webhook 15m received")

	dictionary = request.get_json(force=True)
	print("[JSON]:", dictionary)

        global qty30m = utils::utils.get_qty(6, 100, '15m', myBybit.get_current_price())

	if dictionary["secret"] == cfg.strategy_secret:
		if dictionary["command"] == "openlong":
			print("[BOT] Opened LONG with qty:", set_quantity(6, 100, '15m'))
			bybit_buy(False, '15m')

		if dictionary["command"] == "openshort":
			print("[BOT] Opened SHORT with qty:", set_quantity(6, 100, '15m'))
			bybit_sell(False, '15m')

		if dictionary["command"] == "closelong":
			print("[BOT] Closing LONG\n")
			bybit_sell(True, '15m')

		if dictionary["command"] == "closeshort":
			print("[BOT] Closing SHORT\n")
			bybit_buy(True, '15m')
	else:
		print("[BOT] NO SECRET:", dictionary)

	print("-----------------------------")
	return { "success": False, "message": "invalid"}

# start srv
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)