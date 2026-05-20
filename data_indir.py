from sklift.datasets import fetch_hillstrom
import pandas as pd

print("Veri internetten çekiliyor, lütfen azıcık bekle... ☕")

# Veriyi sklift kütüphanesinden orijinal haliyle alıyoruz
dataset = fetch_hillstrom()

# Veriyi yan yana birleştirip güzel bir tablo (DataFrame) yapıyoruz
df = pd.DataFrame(dataset['data'])
df['target'] = dataset['target']
df['treatment'] = dataset['treatment']

# "hillstrom_kampanya_verisi.csv" olarak indirir.
df.to_csv('hillstrom_kampanya_verisi.csv', index=False)

print("İşlem tamam! Şu an VS Code klasörünün içinde 'hillstrom_kampanya_verisi.csv' dosyası oluştu.")

# terminalde çalıştır --> python3 data_indir.py