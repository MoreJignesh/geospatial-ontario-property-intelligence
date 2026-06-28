# CRS transformation
# Area calculation
# Road length
# Road density


# Load Raw Data
#       ↓
# Profile
#       ↓
# Validate
#       ↓
# Clean
#     ↓
# Repair Geometries
#     ↓
# Dissolve Municipalities
#     ↓
# Spatial Processing
#     ↓
# Road Analytics
#     ↓
# Land Cover Analytics
#     ↓
# Property Intelligence Score
#     ↓
# Visualizations
#     ↓
# Export


import geopandas as gpd

from src.ingestion.inspect_shapefile import inspect_shapefile
from src.processing.basic_geometry import geometry_summary
from src.processing.dissolve import dissolve_municipalities
from src.profiling.data_profile import dataset_profile
from src.validation.spatial_validation import validate_spatial_data
from src.cleaning.spatial_cleaning import clean_spatial_data

from src.processing.spatial_metrics import (
    convert_crs_and_calculate_area,
    compute_road_length_by_municipality,
    calculate_road_density,
)

from src.export.export_data import (
    export_geojson,
    export_csv,
)
from src.feature_engineering.property_score import calculate_property_score
from src.utils.logger import logger
from src.feature_engineering.final_score import calculate_final_score
from src.visualization.plots import plot_top_municipalities
from src.visualization.choropleth import plot_property_score_map



# ----------------------------
# Load Municipal Boundaries
# ----------------------------

municipality_path = "data/raw/Municipal_Boundary_-_Lower_and_Single_Tier.geojson"

municipalities = inspect_shapefile(municipality_path)

# ----------------------------
# Profile Dataset
# ----------------------------

dataset_profile(municipalities)

# ----------------------------
# Validate Dataset
# ----------------------------

validate_spatial_data(municipalities)

# ----------------------------
# Clean Dataset
# ----------------------------

municipalities = clean_spatial_data(municipalities)

municipalities = dissolve_municipalities(municipalities)

# ----------------------------
# Processing
# ----------------------------

municipalities = convert_crs_and_calculate_area(municipalities)

# ----------------------------
# Load Road Network
# ----------------------------

road_path = "data/raw/ORNELEM/LIO-2026-06-09/ORN_ROAD_NET_ELEMENT.shp"

roads = gpd.read_file(road_path)

roads = roads.to_crs(municipalities.crs)

# ----------------------------
# Road Analytics
# ----------------------------

municipalities = compute_road_length_by_municipality(
    roads,
    municipalities,
)

municipalities = calculate_road_density(
    municipalities
)


# ----------------------------
# Export
# ----------------------------


logger.info("Road density calculated successfully.")

municipalities = calculate_property_score(
    municipalities
)

# Rank municipalities
municipalities["rank"] = municipalities["property_score"].rank(ascending=False)

print("\nTOP 10 MUNICIPALITIES")
print(
    municipalities.sort_values("property_score", ascending=False)
    [["MUNICIPAL_NAME", "property_score", "road_density", "area_sqkm"]]
    .head(10)
)

geometry_summary(municipalities)

# ----------------------------
# FEATURE ENGINEERING (FINAL SCORE)
# ----------------------------

municipalities = calculate_property_score(municipalities)

plot_top_municipalities(municipalities)

plot_property_score_map(municipalities)
# ----------------------------
# EXPORT
# ----------------------------

export_geojson(municipalities)
export_csv(municipalities)

logger.info("Pipeline completed successfully.")

# municipalities.to_file(
#     "data/processed/municipal_analytics.geojson",
#     driver="GeoJSON"
# )

# print("Processing complete!")