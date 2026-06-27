
from src.ingestion.inspect_shapefile import inspect_shapefile
from src.processing.basic_geometry import geometry_summary
from src.processing.spatial_metrics import convert_crs_and_calculate_area

from src.processing.spatial_metrics import calculate_road_density
from src.processing.spatial_metrics import compute_road_length_by_municipality
import geopandas as gpd
from src.processing.spatial_metrics import compute_property_intelligence_score

file_path = "data/raw/Municipal_Boundary_-_Lower_and_Single_Tier.geojson"

# Load
gdf = inspect_shapefile(file_path)

# Inspect
geometry_summary(gdf)

# Transform + calculate area (IMPORTANT FIX)
gdf_projected = convert_crs_and_calculate_area(gdf)

print("\nProjected dataset ready:", gdf_projected.head())

road_path = "data/raw/ORNELEM/LIO-2026-06-09/ORN_ROAD_NET_ELEMENT.shp"

roads = gpd.read_file(road_path)


gdf_with_roads = compute_road_length_by_municipality(
    roads,
    gdf_projected
)

# 3. KPI
gdf_final = calculate_road_density(gdf_with_roads)

print(gdf_final[["area_sqkm", "road_length_km", "road_density"]].head())

gdf_scored = compute_property_intelligence_score(gdf_final)

print(
    gdf_scored[[
        "area_sqkm",
        "road_length_km",
        "road_density",
        "property_intelligence_score"
    ]].head()
)