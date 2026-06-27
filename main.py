from src.ingestion.inspect_shapefile import inspect_shapefile
from src.processing.basic_geometry import geometry_summary
from src.processing.spatial_metrics import convert_crs_and_calculate_area

file_path = "data/raw/Municipal_Boundary_-_Lower_and_Single_Tier.geojson"

gdf = inspect_shapefile(file_path)

geometry_summary(gdf)

gdf_projected = convert_crs_and_calculate_area(gdf)