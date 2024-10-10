import pyotp
import RPi.GPIO as GPIO  #is alleen voor raspberry pi
import time

# GPIO setup
RELAIS_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAIS_PIN, GPIO.OUT)

# Het geheime wachtwoord dat overeenkomt met de Google Authenticator QR-code
secret = "JBSWY3DPEHPK3PXP"  # Dit moet hetzelfde geheim zijn als in je QR-code!
totp = pyotp.TOTP(secret)

def open_deur():
    GPIO.output(RELAIS_PIN, GPIO.HIGH)  # Zet relais aan
    print("Deur is open voor 5 seconden...")
    time.sleep(5)  # Deur open voor 5 seconden
    GPIO.output(RELAIS_PIN, GPIO.LOW)   # Zet relais uit
    print("Deur is nu gesloten.")

def main():
    while True:
        # Vraag de gebruiker om een code in te voeren
        ingevoerde_code = input("Voer uw code in (of type 'exit' om te stoppen): ")

        if ingevoerde_code.lower() == 'exit':
            print("Programma gestopt.")
            break

        # Verifieer de TOTP-code
        if totp.verify(ingevoerde_code):
            print("Toegang verleend!")
            open_deur()
        else:
            print("Toegang geweigerd! Verkeerde code.")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgramma onderbroken door gebruiker.")
    finally:
        GPIO.cleanup()  # Zorg ervoor dat de GPIO netjes wordt afgesloten
