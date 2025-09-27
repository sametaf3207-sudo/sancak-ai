# Müşteri Temsilcisi mantığı için basit yardımcı (ileride genişletilebilir).
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MODEL = os.getenv("CHAT_MODEL", "gpt-4o-mini")

TEMPLATE = "Sen müşteri temsilcisisin. Kullanıcının derdini kısa ve net çöz, ilgili yerlerde Vekil AL'a devretmeyi öner."

def handle(message: str) -> str:
    try:
        r = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role":"system","content":TEMPLATE},
                {"role":"user","content":message}
            ],
            temperature=0.4,
            max_tokens=400
        )
        return r.choices[0].message.content.strip()
    except Exception as e:
        return f"Temsilci hata: {e}"
