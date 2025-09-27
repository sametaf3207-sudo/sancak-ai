from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()
app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_msg = request.json.get("message")

        response = client.chat.completions.create(
            model="gpt-4o-mini",  # hızlı ve ucuz model
            messages=[
                {"role": "system", "content": "Sen yardımcı bir vekil asistansın."},
                {"role": "user", "content": user_msg}
            ]
        )

        bot_reply = response.choices[0].message.content
        return jsonify({"reply": bot_reply})

    except Exception as e:
        return jsonify({"reply": f"Hata: {str(e)}"})
