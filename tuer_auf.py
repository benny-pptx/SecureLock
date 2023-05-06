# import der benötigten Bibs
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

import lcddriver
import time

# Deklaration der notwendigen Gerätschaften
reader = SimpleMFRC522()

lcd = lcddriver.lcd()
lcd.lcd_clear()

# Liste der berechtigten Personen nach ID
zug_ids = 566903915301 # Fr. Dr. Voss

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
			time.sleep(1.5)
			lcd.lcd_clear() # Wichtig sonst Display doof :(

		else:
			print("Nicht berechtigt")
			lcd.lcd_display_string("Karte gelesen", 1)
			lcd.lcd_display_string("Nicht berechtigt", 2)
			time.sleep(2)
			lcd.lcd_clear()
	except Exception as e:
		print(e)
		lcd.lcd_clear()
		lcd.lcd_display_string("  Fehler!!  ", 1)
		lcd.lcd_display_string("Nicht autorisiert", 2)
	time.sleep(2)


GPIO.cleanup()
