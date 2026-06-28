

# it can have functions like:

# remove exact duplicate rows
# fix invalid geometries
# standardize municipality names (trim spaces, uppercase if needed)


def clean_spatial_data(gdf):

    print("\n========== CLEANING ==========")

    before = len(gdf)

    # Remove exact duplicate rows
    gdf = gdf.drop_duplicates()

    # Repair invalid geometries
    invalid_before = (~gdf.geometry.is_valid).sum()

    if invalid_before > 0:
        print(f"Repairing {invalid_before} invalid geometries...")
        gdf["geometry"] = gdf.geometry.buffer(0)

    invalid_after = (~gdf.geometry.is_valid).sum()

    print(f"Rows Before : {before}")
    print(f"Rows After : {len(gdf)}")
    print(f"Invalid Before : {invalid_before}")
    print(f"Invalid After : {invalid_after}")

    return gdf