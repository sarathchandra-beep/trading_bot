import argparse
from bot.client import BinanceFuturesClient
from bot.orders import create_order
from bot.validators import validate_side, validate_order_type, validate_price
from bot.logging_config import setup_logging


def main():
    setup_logging()

    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

    parser.add_argument("--symbol", required=True, help="Trading pair (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", type=float, required=True, help="Order quantity")
    parser.add_argument("--price", type=float, help="Required for LIMIT orders")

    args = parser.parse_args()

    try:
        # ✅ Validate inputs
        validate_side(args.side)
        validate_order_type(args.type)
        validate_price(args.type, args.price)

        # ✅ Initialize client
        client = BinanceFuturesClient()

        # ✅ Place order
        response = create_order(
            client,
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        # ✅ Output
        print("\n✅ Order Successful")
        print(f"Symbol: {args.symbol}")
        print(f"Side: {args.side}")
        print(f"Type: {args.type}")
        print(f"Quantity: {args.quantity}")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")
        print(f"Avg Price: {response.get('avgPrice', 'N/A')}")

    except Exception as e:
        print("\n❌ Order Failed")
        print(str(e))


if __name__ == "__main__":
    main()