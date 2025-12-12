import RPi.GPIO as GPIO
import time
from RPLCD.i2c import CharLCD
import random

GPIO.setwarnings(False)
Gpio.setmode(GPIO.BCM)
BUTTON_PIN = 27
GPIO.setup(27,GPIO.IN,GPIO.PUD_UP)
lcd = CHarLCD(i2c_expander='PCF8574',address = 0x27,port = 1,cols = 16,rows = 2,dotsize = 8)
click = 0
try:
	while True:
		boost = random.randint(0,100)
		input_state = GPIO.input(27)
		click = int(click)
		if click > 499:
			lcd.cursor_pos=(0,0)
			lcd.write_string("YOU WIN!!!")
			time.sleep(5)
			break
		if input_state == False:
			click = str(click)
			if boost == 100:
				boostime = 50
				while boostime > 0:
					if input_state == False:
						click = int(click)
						click += 3
						click = str(click)
						lcd.cursor_pos=(1,0)
						lcd.write_string("BOOST!!!")
						lcd.cursor_pos=(0,0)
						lcd.write_string("Clicks:")
						lcd.cursor_pos=(0,8)
						lcd.write_string(click)
			else:
				time.sleep(0.2)
			lcd.clear()
			click = int(click)
			click += 1
			click = str(click)
			lcd.cursor_pos=(0,0)
			lcd.write_string("Clicks:")
			lcd.cursor_pos=(0,8)
			lcd.write_string(click)

except KeyboardInterrupt:
	GPIO.cleanup()
	lcd.clear()
finally:
	GPIO.cleanup()
	lcd.clear
