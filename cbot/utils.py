import cfg
import requests

# get atr
def get_atr(interval):
    parameters =  {
	'secret':cfg.taapi_key,
	'exchange':'binance',
	'symbol':'BTC/USDT',
	'interval':interval
    }

    response = requests.get(url=cfg.taapi_endpoint, params=parameters)
    return response.json()

# position quantity
def get_qty(risk, balance, timeframe, current_price):
    # get atr based on the TF; factor depending on the strategy
    atr = 0
    if timeframe == '10m':
        atr = get_atr('15m')
        atr['value'] * 0.66
    elif timeframe == '15m':
        atr = get_atr('15m')
    elif timeframe == '30m':
        atr = get_atr('30m')
    else:
        return None

    print("[bot] current atr:", atr)
    print(type(current_price))
    print(type(atr['value']))

    stop = current_price - (atr['value'] * 2)
    stop_difference = current_price - stop
    risk_amount = balance * (float(risk) / 100)
    position_size = risk_amount / stop_difference * current_price
    quantity = round(position_size / current_price, 3)

    # bybit api only accepts positive qty
    if quantity < 0 and position_size < 0:
        quantity *= -1
        position_size *= -1

    # posiition_size == USD value; quantity == BTC value
    return position_size, quantity