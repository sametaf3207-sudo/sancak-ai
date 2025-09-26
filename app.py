
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    incoming_msg = request.values.get("Body", "").lower()
    response = MessagingResponse()
    reply = response.message()

    if "müşteri" in incoming_msg:
        reply.body("📞 Müşteri Temsilcisi: Size yardımcı oluyorum.")
    elif "sağ kol" in incoming_msg:
        reply.body("🤝 Sağ Kol: Partnerlerle iletişimi ben yürütürüm.")
    elif "sol kol" in incoming_msg:
        reply.body("📊 Sol Kol: Finans ve hesap işleri bende.")
    elif "vekil" in incoming_msg:
        reply.body("🧠 Vekil AL: Tüm sistemi yönetiyorum.")
    else:
        reply.body("⚡ Lütfen birini çağırın: müşteri / sağ kol / sol kol / vekil")

    return str(response)

if __name__ == "__main__":
    app.run(port=5000)
