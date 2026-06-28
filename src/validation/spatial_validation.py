# Checks to include:

# CRS exists
# Valid geometries
# Missing geometries
# Duplicate municipality names
# Duplicate IDs


def validate_spatial_data(gdf):

    print("\n========== SPATIAL VALIDATION ==========")

    print(f"CRS : {gdf.crs}")

    print(f"Missing Geometries : {gdf.geometry.isna().sum()}")

    print(f"Invalid Geometries : {(~gdf.geometry.is_valid).sum()}")

    print(f"Duplicate OGF_ID : {gdf['OGF_ID'].duplicated().sum()}")

    print(f"Duplicate Municipality Names : {gdf['MUNICIPAL_NAME'].duplicated().sum()}")
