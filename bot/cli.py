import argparse
from bot.orders import place_order
from bot.validators import validate_inputs
from bot.logging_config import setup_logging

def main():
    setup_logging()

    print("=== Binance Trading Bot ===")

    try:
        symbol = input("Enter symbol (e.g. BTCUSDT): ").upper()
        side = input("Enter side (BUY/SELL): ").upper()
        order_type = input("Enter order type (MARKET/LIMIT): ").upper()
        quantity = float(input("Enter quantity: "))

        price = None
        if order_type == "LIMIT":
            price = float(input("Enter price: "))

        # Validate input
        validate_inputs(symbol, side, order_type, quantity, price)

        print("\n📌 Order Request:")
        print({
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
            "price": price
        })

        # Place order
        response = place_order(symbol, side, order_type, quantity, price)

        print("\n✅ Order Successful")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")
        print(f"Avg Price: {response.get('avgPrice')}")

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")

if __name__ == "__main__":
    main()