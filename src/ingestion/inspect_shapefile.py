
import geopandas as gpd

def inspect_shapefile(path):
    gdf = gpd.read_file(path)

    print("\n--- BASIC INFO ---")
    print("Shape:", gdf.shape)
    print("CRS:", gdf.crs)

    print("\n--- COLUMNS ---")
    print(gdf.columns)

    print("\n--- GEOMETRY TYPES ---")
    print(gdf.geometry.type.unique())

    print("\n--- SAMPLE DATA ---")
    print(gdf.head())

    return gdf


# roads = inspect_shapefile("data/raw/ORNELEM/LIO-2026-06-09")