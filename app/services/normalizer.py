import pandas as pd
REQUIRED_COLUMNS = {
    "city": ["city", "City", "town"],
    "region": ["region", "Region"],
    "sites": ["sites", "site_count", "count", "number_of", "number_of_sites", "Number_of_", "no_of", "no_of_sites"]
}

def normalize_columns(df):
    rename_map = {}

    # Heuristic, case-insensitive mapping first
    for col in df.columns:
        key = col.strip().lower().replace(" ", "_")
        if "city" in key or "town" in key:
            rename_map[col] = "city"
            continue
        if "region" in key or "state" in key or "province" in key:
            rename_map[col] = "region"
            continue
        if (
            "site" in key or "count" in key or "number" in key or "no_" in key
        ):
            rename_map[col] = "sites"

    # Fallback to explicit alias list if anything still missing
    for standard, aliases in REQUIRED_COLUMNS.items():
        if standard not in rename_map.values():
            for col in df.columns:
                if col in aliases:
                    rename_map[col] = standard
                    break

    df = df.rename(columns=rename_map)

    missing = set(["city", "region", "sites"]) - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    df["city"] = df["city"].astype(str)
    df["region"] = df["region"].astype(str)
    df["sites"] = pd.to_numeric(df["sites"], errors="coerce").fillna(0)

    return df[["city", "region", "sites"]]
