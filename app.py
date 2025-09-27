# SANCAK - Tam Sürüm (Starter) | Vekil AL + Temsilci + Basit Araçlar
import os
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
from openai import OpenAI

# .env yükle (lokal kullanım için). Render/Heroku gibi yerlerde Env Vars kullanın.
load_dotenv(os.path.join(os.path.dirname(__file__), "config", ".env"))

app = Flask(__name__, template_folder="templates")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
CHAT_MODEL = os.getenv("CHAT_MODEL", "gpt-4o-mini")

# Roller için sistem promptları
SYSTEMS = {
    "vekil": "Sen Vekil AL'sin: kısa, net, çözüm odaklısın; kararsız kalmazsın.",
    "temsilci": "Sen müşteri temsilcisisin: nazik, açıklayıcı, ikna edici ve sabırlısın.",
    "sagkol": "Sen sağ kolsun: sistem, bakım ve log konularında uzmansın.",
    "solkol": "Sen sol kolsun: muhasebe, fiyat, gelir-gider, raporlar konusuna hakimsin.",
    "guvenlik": "Sen güvenlik ekibisin: yasal/etik çerçevede güvenlik önerileri verirsin.",
    "guncelleme": "Sen güncelleme ekibisin: feature fikirleri ve yol haritası önerirsin."
}

def ai_answer(role: str, text: str) -> str:
    if not client:
        return "OpenAI anahtarı yok. Lütfen config/.env içine OPENAI_API_KEY ekleyin."
    try:
        sys_prompt = SYSTEMS.get(role, SYSTEMS["vekil"])
        resp = client.chat.completions.create(
            model=CHAT_MODEL,
            messages=[
                {"role":"system", "content": sys_prompt},
                {"role":"user", "content": text}
            ],
            max_tokens=600,
            temperature=0.5
        )
        return resp.choices[0].message.content.strip()
    except Exception as e:
        return f"Hata: {e}"

@app.get("/")
def home():
    return render_template("index.html")

@app.get("/health")
def health():
    return {"ok": True, "service": "sancak-full", "version": "1.0"}

@app.post("/chat")
def chat():
    data = request.get_json(silent=True) or {}
    text = (data.get("message") or "").strip()
    role = (data.get("role") or "vekil").strip().lower()
    if not text:
        return jsonify({"error": "message gerekli"}), 400
    reply = ai_answer(role, text)
    return jsonify({"role": role, "reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")), debug=True)
