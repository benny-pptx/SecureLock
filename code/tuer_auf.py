# import der benötigten Bibs
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import lcddriver
import time
import logging

# Deklaration für die notwendigen Gerätschaften
reader = SimpleMFRC522()

lcd = lcddriver.lcd()
lcd.lcd_clear()

servoPIN = 40
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPIN, GPIO.OUT)

servo = GPIO.PWM(servoPIN, 50)
servo.start(0)
servo.ChangeDutyCycle(0)

# Basis fürs Logging
logging.basicConfig(filename='tuer_auf.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(message)s')
logging.info('Hier beginnt das Log')

# Liste der berechtigten Personen nach ID
zug_ids = 566903915301 # Dr. Voss, Deklaration einer Hilfsvariable

# Abfrage der Berechtigung und ausgeben des Status der "Tür-Lesers"
while True:

	try:
		print("Bitte Karte präsentieren")
		lcd.lcd_display_string("Guten Tag", 1)
		lcd.lcd_display_string("Karte vorzeigen", 2)
		id, text = reader.read()
		print("Kartennummer: {}".format(id))

		if id == zug_ids:
			print("Zutritt gewährt")
			print("Guten Tag Dr. " + text)
			lcd.lcd_display_string("Karte gelesen", 1)
			lcd.lcd_display_string("Zutritt gewaehrt", 2)
			servo.ChangeDutyCycle(7.5)
			time.sleep(1)
			servo.ChangeDutyCycle(2.5)
			time.sleep(1)
			servo.ChangeDutyCycle(0)
			lcd.lcd_clear() # Wichtig sonst Display doof :(
			logging.debug('Erfolgreiche Authorisierung')

		else:
			print("Nicht berechtigt")
			lcd.lcd_display_string("Karte gelesen", 1)
			lcd.lcd_display_string("Nicht berechtigt", 2)
			time.sleep(1.5)
			lcd.lcd_clear()
			logging.warning('Nicht authorisierter Zutrittsversuch')

	except Exception as e:
		print(e)
		lcd.lcd_clear()
		lcd.lcd_display_string("  Fehler!!  ", 1)
		lcd.lcd_display_string("Nicht autorisiert", 2)
		logging.error('Fehler beim Lesen oder keine Authorisierung')

GPIO.cleanup()
logging.info('Hier endet das Log')
