import RPi.GPIO as GPIO #is alleen voor raspberry pi
import time
import pyotp
from pad4pi import rpi_gpio #is alleen voor raspberry pi

# GPIO setup for the relay
RELAIS_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAIS_PIN, GPIO.OUT)

# Het geheime wachtwoord dat overeenkomt met de Google Authenticator QR-code
secret = "JBSWY3DPEHPK3PXP"
totp = pyotp.TOTP(secret)

# Keypad setup
KEYPAD = [
    ['1', '2', '3', 'A'],
    ['4', '5', '6', 'B'],
    ['7', '8', '9', 'C'],
    ['*', '0', '#', 'D']
]

ROW_PINS = [5, 6, 13, 19]  # GPIO pinnen verbonden met de rijen van het keypad
COL_PINS = [26, 16, 20, 21]  # GPIO pinnen verbonden met de kolommen van het keypad

factory = rpi_gpio.KeypadFactory()
keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)

# Variabele om de code op te slaan
code = ""

def open_deur():
    GPIO.output(RELAIS_PIN, GPIO.HIGH)  # Zet relais aan
    print("Deur is open voor 5 seconden...")
    time.sleep(5)
    GPIO.output(RELAIS_PIN, GPIO.LOW)   # Zet relais uit
    print("Deur is nu gesloten.")

# Callback-functie voor wanneer een toets wordt ingedrukt
def keypad_press(key):
    global code
    print(key)
    
    if key == '#':  # # om de code te bevestigen
        print(f"Code ingevoerd: {code}")
        if totp.verify(code):
            print("Toegang verleend!")
            open_deur()
        else:
            print("Toegang geweigerd! Verkeerde code.")
        code = ""  # Reset de code na invoer
    elif key == '*':  # * om de code te resetten
        code = ""
        print("Code gereset.")
    else:
        code += key  # Voeg de ingedrukte toets toe aan de code

# Keypad listener
keypad.registerKeyPressHandler(keypad_press)

try:
    while True:
        time.sleep(0.1)  # Houd het programma draaiende
except KeyboardInterrupt:
    print("\nProgramma gestopt.")
finally:
    GPIO.cleanup()  # GPIO netjes afsluiten
    keypad.cleanup()  # Keypad netjes afsluiten
