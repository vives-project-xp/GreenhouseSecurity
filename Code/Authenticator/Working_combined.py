import RPi.GPIO as GPIO
import time
import pyotp

# Het geheime wachtwoord dat overeenkomt met de Google Authenticator QR-code
secret = "JBSWY3DPEHPK3PXP"
totp = pyotp.TOTP(secret)

# Definieer de layout van het 4x3 keypad (zonder letters)
KEYPAD = [
    ['1', '2', '3'],  # Eerste rij
    ['4', '5', '6'],  # Tweede rij
    ['7', '8', '9'],  # Derde rij
    ['*', '0', '#']    # Vierde rij
]

# Pas de GPIO-pinnen aan volgens jouw verbindingen:
ROW_PINS = [5, 6, 13, 19]  # GPIO5, GPIO6, GPIO13, GPIO19 voor de 4 rijen
COL_PINS = [26, 20, 21]  # GPIO26, GPIO20, GPIO21 voor de 3 kolommen

# GPIO setup
GPIO.setmode(GPIO.BCM)

# Stel de rijen in als outputs en zet ze hoog
for row_pin in ROW_PINS:
    GPIO.setup(row_pin, GPIO.OUT)
    GPIO.output(row_pin, GPIO.HIGH)

# Stel de kolommen in als inputs en zet ze met pull-up weerstanden
for col_pin in COL_PINS:
    GPIO.setup(col_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def read_keypad():
    # Loop door alle rijen
    for row_index, row_pin in enumerate(ROW_PINS):
        # Zet de huidige rij laag
        GPIO.output(row_pin, GPIO.LOW)

        # Controleer welke kolom laag is (toets ingedrukt)
        for col_index, col_pin in enumerate(COL_PINS):
            if GPIO.input(col_pin) == GPIO.LOW:
                # Wacht totdat de toets losgelaten wordt om bouncing te voorkomen
                while GPIO.input(col_pin) == GPIO.LOW:
                    time.sleep(0.1)

                # Zet de rij weer hoog en geef de ingedrukte toets terug
                GPIO.output(row_pin, GPIO.HIGH)
                return KEYPAD[row_index][col_index]

        # Zet de rij weer hoog
        GPIO.output(row_pin, GPIO.HIGH)

    return None

try:
    input_code = ""  # Variabele om de ingevoerde code op te slaan

    while True:
        key = read_keypad()
        if key:
            if key == '#':  # Als de '#' toets is ingedrukt
                # Verifieer de code
                if totp.verify(input_code):
                    print("\nToegang verleend!")
                else:
                    print("\nToegang geweigerd! Verkeerde code.")
                input_code = ""  # Reset de code na controle
            elif key == '*':  # Reset de code bij het indrukken van '*'
                input_code = ""
                print("Code gereset.")
            else:
                input_code += key  # Voeg de ingedrukte toets toe aan de code
                print(f"\r Code ingevoerd: {input_code}", end='')  # Houd de cursor op dezelfde regel

except KeyboardInterrupt:
    print("\nProgramma gestopt.")
finally:
    GPIO.cleanup()
