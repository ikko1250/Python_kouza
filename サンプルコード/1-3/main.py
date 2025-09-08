import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import japanize_matplotlib 

df = pd.read_csv("/home/ubuntu/cur/program/Teaching/1/サンプルコード/1-3/46鹿児島県_202507fit portal.csv")

print("=== データの最初の5行 ===")
print(df.head())

print("\n=== 列名一覧 ===")
print(df.columns)

print("\n=== 発電出力の統計情報 ===")
print(df[['発電出力（kW）']].describe())

df_u1000 = df[df['発電出力（kW）'] <= 1000]

sns.histplot(df_u1000, x='発電出力（kW）', bins=30)
plt.title("Histogram of Power Output(<=1000kW)")
plt.savefig("/home/ubuntu/cur/program/Teaching/1/サンプルコード/1-3/発電出力_histogram(<=1000kW).png")
plt.clf() 

vals = "太陽光"
df_pv = df_u1000[df_u1000['発電設備区分'] == vals]

print("\n=== 太陽光発電(1000kW以下)の統計情報 ===")
print(df_pv[['発電出力（kW）']].describe())

sns.histplot(df_pv, x='発電出力（kW）', bins=30, color="orange")
plt.title("Histogram of Power Output(<=1000kW) for Solar Power")
plt.savefig("/home/ubuntu/cur/program/Teaching/1/サンプルコード/1-3/発電出力_histogram(<=1000kW)_solar.png")
plt.clf() 

print(df[df['発電出力（kW）'] == df['発電出力（kW）'].max()].to_string())