# LOAD DATA
#    ↓
# SUMMARY
#    ↓
# ANALYTICS
#    ↓
# VISUALS

import geopandas as gpd

from src.analytics.metrics import *
from src.analytics.report import executive_summary
from src.visualization.dashboard import road_density_map
from src.visualization.plots import (
    road_density_histogram,
    road_length_histogram,
    area_distribution,
    area_vs_density,
    area_vs_road_length,
    property_score_map,
)

# ----------------------------
# LOAD PROCESSED DATA ONLY
# ----------------------------

gdf = gpd.read_file(
    "data/processed/municipal_analytics.geojson"
)

# ----------------------------
# BASIC CHECKS
# ----------------------------

print("\nUnique municipality names:")
print(gdf["MUNICIPAL_NAME"].nunique())

print("\nTotal rows:")
print(len(gdf))

# ----------------------------
# ANALYTICS
# ----------------------------

executive_summary(gdf)

project_summary(gdf)
top_property_score(gdf)
bottom_property_score(gdf)

municipality_profile(gdf, "CITY OF TORONTO")

# ----------------------------
# VISUALS
# ----------------------------

property_score_map(gdf)
road_density_map(gdf)

# duplicates = (
#     gdf.groupby("MUNICIPAL_NAME")
#        .size()
#        .sort_values(ascending=False)
# )

# print(duplicates.head(20))

# print(gdf.columns.tolist())

# dataset_summary(gdf)

# road_density_summary(gdf)

# top_road_density(gdf)

# lowest_road_density(gdf)

# municipalities_without_roads(gdf)

# largest_municipalities(gdf)

# road_density_histogram(gdf)

# top10_road_density(gdf)

# area_vs_roads(gdf)


# road_density_histogram(gdf)
# road_length_histogram(gdf)
# area_distribution(gdf)
# area_vs_density(gdf)
# area_vs_road_length(gdf)

# municipality_profile(gdf, "CITY OF TORONTO")
# municipality_profile(gdf, "CITY OF OTTAWA")

# compare_municipalities(
#     gdf,
#     "CITY OF TORONTO",
#     "CITY OF OTTAWA"
# )