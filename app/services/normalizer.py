import pandas as pd
REQUIRED_COLUMNS = {
    "city": ["city", "City", "town"],
    "region": ["region", "Region"],
    "sites": ["sites", "site_count", "count"]
}

def normalize_columns(df):
    rename_map = {}

    for standard, aliases in REQUIRED_COLUMNS.items():
        for col in df.columns:
            if col in aliases:
                rename_map[col] = standard
                break

    df = df.rename(columns=rename_map)

    missing = set(REQUIRED_COLUMNS.keys()) - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    # Ensure proper dtypes for downstream analysis
    df["city"] = df["city"].astype(str)
    df["region"] = df["region"].astype(str)
    df["sites"] = pd.to_numeric(df["sites"], errors="coerce").fillna(0)

    return df[["city", "region", "sites"]]
