\
    @echo off
    title Sancak - Vekil AL
    echo [1/4] Sanal ortam olusturuluyor...
    py -m venv venv
    if exist venv\Scripts\activate.bat (
        call venv\Scripts\activate.bat
    ) else (
        echo Sanal ortam aktivasyonu bulunamadi. Devam ediliyor...
    )
    echo [2/4] Kutuphaneler yukleniyor...
    pip install --upgrade pip
    pip install -r requirements.txt
    echo [3/4] Ortam degiskenleri icin config\.env dosyasini olusturun (config\.env)
    if not exist config\.env (
        copy config\.env.example config\.env >nul
        echo config\.env olusturuldu. OPENAI_API_KEY degerini duzenleyin.
        notepad config\.env
    )
    echo [4/4] Uygulama baslatiliyor...
    py app.py
    pause
