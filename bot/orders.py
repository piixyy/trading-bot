from bot.client import get_client
import logging

logger = logging.getLogger(__name__)

def place_order(symbol, side, order_type, quantity, price=None):
    client = get_client()

    try:
        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity
        }

        # If LIMIT order → need price
        if order_type == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        logger.info(f"Placing order: {params}")

        response = client.futures_create_order(**params)

        logger.info(f"Response: {response}")

        return response

    except Exception as e:
        logger.error(f"Error placing order: {str(e)}")
        raise