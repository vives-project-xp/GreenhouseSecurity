import pyotp
import qrcode

# Het geheime wachtwoord
secret = "JBSWY3DPEHPK3PXP"

# Maak een TOTP object met de geheime sleutel
totp = pyotp.TOTP(secret)

# Genereer de provisioning URI (voor 'My Service' met een e-mailadres als identifier)
uri = totp.provisioning_uri(name="Xander toegang serre", issuer_name="Serre Vives")

# Print de URI, deze kun je ook direct gebruiken als je wilt
print("Provisioning URI:", uri)

# Maak de QR-code van de URI
qr = qrcode.make(uri)

# Sla de QR-code op als afbeelding
qr.save("authenticator_qrcode.png")

# Of toon de QR-code direct
qr.show()
