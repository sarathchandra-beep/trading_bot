def create_order(client, symbol, side, order_type, quantity, price=None):
    try:
        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity
        }

        if order_type == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        response = client.place_order(**params)

        if not response:
            raise Exception("Empty response from Binance API")

        return response

    except Exception as e:
        raise Exception(f"Order failed: {str(e)}")