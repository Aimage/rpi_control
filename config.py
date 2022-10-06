from rpi_control.controled_object.light import Light
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)

TWILIO_SMS_CONTROLLED_OBJECTS = {"GarageLight": Light(18, "GarageLight")}
