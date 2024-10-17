import time
import pyotp

# Het geheime wachtwoord dat overeenkomt met de Google Authenticator QR-code
secret = "JBSWY3DPEHPK3PXP"
totp = pyotp.TOTP(secret)

try:
    while True:
        code = input("Voer de code in: ")
        if totp.verify(code):
            print("Toegang verleend!")
        else:
            print("Toegang geweigerd! Verkeerde code.")
        
        time.sleep(1)  # Eventuele vertraging tussen de pogingen
except KeyboardInterrupt:
    print("\nProgramma gestopt.")
