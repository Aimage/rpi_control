
from rpi_control.evaluation import evaluate
from config import TWILIO_SMS_CONTROLED_OBJECTS


if __name__ == "__main__":
    message = """
                GarageLight:switch:on
                GarageLight:switch:off
                bey:status:
    """
    results = evaluate(TWILIO_SMS_CONTROLED_OBJECTS, message)
    for res in results:
        print(res)


