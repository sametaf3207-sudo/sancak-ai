# Basit temizlik aracıdır. D/E hariç dizinleri tarayabilir, büyük/geçici dosyaları listeler.
# SİLME İŞLEMİNİ OTOMATİK YAPMAZ; önce liste çıkarır, sonra onay ister.
import os, sys

EXCLUDE_DRIVES = {'E:'}

def human(n):
    for u in ['B','KB','MB','GB','TB']:
        if n < 1024: return f"{n:.1f} {u}"
        n/=1024
    return f"{n:.1f} PB"

def list_candidates(root, min_mb=50):
    cands = []
    for dp,_,files in os.walk(root):
        for f in files:
            p = os.path.join(dp,f)
            try:
                s = os.path.getsize(p)
            except Exception:
                continue
            if s >= min_mb*1024*1024:
                cands.append((p,s))
    return sorted(cands, key=lambda x: -x[1])

if __name__ == '__main__':
    print('Temizlik listesi (silmeden önce yedek almayı unutmayın).')
    drives = [f"{chr(d)}:" for d in range(67, 91)]  # C..Z
    for d in drives:
        if os.path.exists(d+'\\') and d not in EXCLUDE_DRIVES:
            print(f"\nSürücü: {d}")
            try:
                items = list_candidates(d+'\\', 200)  # 200MB+
                for p,s in items[:50]:
                    print(human(s), '->', p)
            except Exception as e:
                print('Hata:', e)
    print('\nNot: E: hariç tutuldu. Otomatik silme yapılmaz; sadece rapor verir.')
