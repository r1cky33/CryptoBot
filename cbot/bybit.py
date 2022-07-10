from pybit.usdt_perpetual import HTTP

# bybitAPI
import cfg

class bybit:
    def __init__(self) -> None:
        # open session
        self.session = HTTP(
            endpoint = cfg.bybit_endpoint,
            api_key = cfg.api_key,
            api_secret = cfg.api_secret
        )

        self.symbol = 'BTCUSDT'

    # get current BTC price
    def get_current_price(self):
        ob = self.session.orderbook(self.symbol)
        fr = ob['result'][0]
        return float(fr['price'])

    # market buy
    def market_buy(self, b_reduce_only, qty):
        self.session.place_active_order(
            symbol=self.symbol,
            side="Buy",
            order_type="Market",
            qty=0.001,
            time_in_force="GoodTillCancel",
            reduce_only=b_reduce_only,
            close_on_trigger=False
        )

    def market_sell(self, b_reduce_only, qty):
            self.session.place_active_order(
            symbol=self.symbol,
            side="Sell",
            order_type="Market",
            qty=0.001,
            time_in_force="GoodTillCancel",
            reduce_only=b_reduce_only,
            close_on_trigger=False
        )