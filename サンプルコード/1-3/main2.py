import pandas as pd

PlantCapa = 20
print(PlantCapa // 10) 
# -, +, *, /, **, //, %, が使える。

PlantCapa = pd.read_csv("1/サンプルコード/1-3/46鹿児島県_202507fit portal.csv") # CSVファイルを読み込み。


print(PlantCapa.head())
print(PlantCapa.head(30))


# 計算に使う列を数値化（文字列などが混在していても NaN に変換）
for col in ['発電出力（kW）', '太陽電池の合計出力（kW）']:
	PlantCapa[col] = pd.to_numeric(PlantCapa[col], errors='coerce')

# 0除算を回避（分母が0やNaNなら結果はNaN）
denom = PlantCapa['太陽電池の合計出力（kW）'].replace(0, pd.NA)

PlantCapa['出力比'] = PlantCapa['発電出力（kW）'] / denom


# 複数列を参照する場合はリストで渡す（二重ブラケット）
print(PlantCapa[['発電出力（kW）', '太陽電池の合計出力（kW）', '出力比']].head(100).to_string())