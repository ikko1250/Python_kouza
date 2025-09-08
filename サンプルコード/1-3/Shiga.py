from pathlib import Path
from typing import Optional

import pandas as pd
from normalize_japanese_addresses import normalize


def extract_prefecture(address: Optional[str]) -> Optional[str]:
    """住所文字列から都道府県名のみを抽出して返す。取得失敗時はNone。

    normalize_japanese_addresses.normalize を level=1 で利用して
    都道府県のみを判定する。
    """
    if address is None:
        return None
    if not isinstance(address, str):
        return None
    addr = address.strip()
    if not addr:
        return None

    try:
        result = normalize(addr, level=1)
        pref = result.get("pref") if isinstance(result, dict) else None
        return pref if pref else None
    except Exception:
        # 正規化中にエラーが発生した場合は None を返す
        return None


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    csv_path = base_dir / "25.滋賀県_202507.csv"

    # 文字コードは日本語CSVで一般的なCP932を優先して読み込み
    # すべて文字列として読み込む（住所列の欠損や混在対策）
    df = pd.read_csv(csv_path, encoding="cp932", dtype=str)

    target_col = "事業者の住所"
    new_col = "事業者の住所_都道府県"

    if target_col not in df.columns:
        raise KeyError(f"CSVに '{target_col}' 列が見つかりませんでした。実際の列名: {list(df.columns)}")

    # 都道府県列を追加
    df[new_col] = df[target_col].apply(extract_prefecture)

    # 確認用出力（先頭数行のみ）
    print(df[[target_col, new_col]].head(10))


if __name__ == "__main__":
    main()
