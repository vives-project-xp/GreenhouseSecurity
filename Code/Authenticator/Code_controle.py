from flask import Flask, request, jsonify
import pyotp

# Setup Flask app
app = Flask(__name__)

# Genereer geheime sleutel (of sla deze elders op)
secret = "JBSWY3DPEHPK3PXP"  # Dit is slechts een voorbeeld, vervang dit door een echte geheime sleutel
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
        # Als de code juist is, kan je hier de hardware aansturen
        print("Toegang verleend!")
        return jsonify({"status": "success", "message": "Toegang verleend!"}), 200
    else:
        print("Toegang geweigerd!")
        return jsonify({"status": "error", "message": "Toegang geweigerd!"}), 403

# Start de server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

