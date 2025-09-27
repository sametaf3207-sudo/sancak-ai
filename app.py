import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import openai

# Çevre değişkenlerini yükle
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route("/")
def home():
    return "Vekil AL çalışıyor!"

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message", "")
    if not user_msg:
        return jsonify({"error": "Mesaj bulunamadı"}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "Sen Vekil AL, kullanıcıya yardımcı bir asistan."},
                      {"role": "user", "content": user_msg}]
        )
        reply = response["choices"][0]["message"]["content"]
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
