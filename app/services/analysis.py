def analyze_data(df, threshold: int):
    if df.empty:
        raise ValueError("Dataset is empty")

    total_sites = int(df["sites"].sum())

    top_region = (
        df.groupby("region")["sites"]
        .sum()
        .idxmax()
    )

    cities_above_threshold = (
        df.groupby("city")["sites"]
        .sum()
        .loc[lambda x: x > threshold]
        .index
        .tolist()
    )

    avg_sites_per_region = float(
        df.groupby("region")["sites"]
        .sum()
        .mean()
    )

    return {
        "total_sites": total_sites,
        "top_region": top_region,
        "cities_above_threshold": cities_above_threshold,
        "average_sites_per_region": avg_sites_per_region
    }
