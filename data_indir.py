from sklift.datasets import fetch_hillstrom
import pandas as pd

dataset = fetch_hillstrom()

df = pd.DataFrame(dataset['data'])
df['target'] = dataset['target']
df['treatment'] = dataset['treatment']

df.to_csv('hillstrom_kampanya_verisi.csv', index=False)


# terminalde çalıştır --> python3 data_indir.py