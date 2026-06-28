
from src.config import OUTPUT_GEOJSON, OUTPUT_CSV

def export_geojson(gdf):
    gdf.to_file(OUTPUT_GEOJSON, driver="GeoJSON")
    print("\nGeoJSON exported.")

def export_csv(gdf):
    gdf.drop(columns="geometry").to_csv(OUTPUT_CSV, index=False)
    print("CSV exported.")