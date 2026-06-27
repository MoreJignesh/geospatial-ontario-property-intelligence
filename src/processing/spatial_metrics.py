import geopandas as gpd

def convert_crs_and_calculate_area(gdf):
    print("\n--- CRS CONVERSION ---")

    # Convert to projected CRS (for Canada)
    gdf_proj = gdf.to_crs(epsg=3347)

    # Calculate area in square meters
    gdf_proj["area_sqm"] = gdf_proj.geometry.area

    # Convert to square km
    gdf_proj["area_sqkm"] = gdf_proj["area_sqm"] / 1_000_000

    print("\n--- AREA STATS ---")
    print(gdf_proj["area_sqkm"].describe())

    return gdf_proj