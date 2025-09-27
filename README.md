# SANCAK - Tam Sürüm Starter

## Hızlı Başlangıç (Windows)
1) Zip'i çıkarın, klasöre girin.
2) `run.bat` çift tıklayın (ilk kurulumda .env oluşturur; anahtarınızı girin).
3) Tarayıcı: http://127.0.0.1:5000

## Render/Heroku
- Build: `pip install -r requirements.txt`
- Start: `gunicorn app:app --bind 0.0.0.0:$PORT`
- Ortam değişkenlerine `OPENAI_API_KEY` ekleyin (panelden).

## Notlar
- `utils/cleanup.py` otomatik silmez; sadece büyük dosyaları listeler. Silmeden önce yedek alın.
- `vpn_al.py` bir iskelet/stub'tur; gerçek VPN entegrasyonu gerekir.
- Güvenlik için anahtarlarınızı asla repoya koymayın.
