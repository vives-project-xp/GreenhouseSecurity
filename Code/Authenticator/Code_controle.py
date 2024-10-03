from flask import Flask, request, jsonify
import pyotp

# Setup Flask app
app = Flask(__name__)

# Het geheime wachtwoord dat overeenkomt met de Google Authenticator QR-code
secret = "JBSWY3DPEHPK3PXP"  # Dit moet hetzelfde geheim zijn als in je QR-code!
totp = pyotp.TOTP(secret)

# Endpoint om de code te verifiëren
@app.route('/verify', methods=['POST'])
def verify_code():
    data = request.get_json()
    ingevoerde_code = data.get('code')

    if not ingevoerde_code:
        return jsonify({"status": "error", "message": "Code ontbreekt"}), 400
    
    # Verifieer de TOTP-code
    if totp.verify(ingevoerde_code):
        print("Toegang verleend!")
        return jsonify({"status": "success", "message": "Toegang verleend!"}), 200
    else:
        print("Toegang geweigerd!")
        return jsonify({"status": "error", "message": "Toegang geweigerd!"}), 403

# Start de server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
