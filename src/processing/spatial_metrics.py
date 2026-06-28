import geopandas as gpd

import geopandas as gpd

# -----------------------------
# 1. MUNICIPAL AREA CALCULATION
# -----------------------------
def convert_crs_and_calculate_area(gdf):
    print("\n--- CRS CONVERSION ---")

    # Project to EPSG:3347 (Canada Albers Equal Area)
    gdf_proj = gdf.to_crs(epsg=3347)

    # Area calculations (correct units)
    gdf_proj["area_sqm"] = gdf_proj.geometry.area
    gdf_proj["area_sqkm"] = gdf_proj["area_sqm"] / 1_000_000

    print("\n--- AREA STATS ---")
    print(gdf_proj["area_sqkm"].describe())

    return gdf_proj


# -----------------------------
# 2. ROAD LENGTH BY MUNICIPALITY
# -----------------------------
def compute_road_length_by_municipality(roads_gdf, municipalities_gdf):
    print("\n--- ROAD LENGTH CALCULATION ---")

    # Ensure both datasets use SAME CRS
    roads_gdf = roads_gdf.to_crs(epsg=3347)
    municipalities_gdf = municipalities_gdf.to_crs(epsg=3347)

    # Calculate road length in KM (correct projection-based length)
    roads_gdf["road_length_km"] = roads_gdf.geometry.length / 1000

    # Spatial join (roads → municipalities)
    joined = gpd.sjoin(
        roads_gdf,
        municipalities_gdf,
        how="inner",
        predicate="intersects"
    )

    # Aggregate road length per municipality
    road_summary = (
        joined.groupby("index_right")["road_length_km"]
        .sum()
    )

    # Attach back to municipalities
    municipalities_gdf["road_length_km"] = road_summary

    # Fill missing municipalities with 0
    municipalities_gdf["road_length_km"] = municipalities_gdf["road_length_km"].fillna(0)

    print("\n--- ROAD STATS ---")
    print(municipalities_gdf["road_length_km"].describe())

    return municipalities_gdf


# -----------------------------
# 3. ROAD DENSITY (NEW KPI)
# -----------------------------
def calculate_road_density(gdf):
    print("\n--- ROAD DENSITY CALCULATION ---")

    if "area_sqkm" not in gdf.columns:
        raise ValueError("area_sqkm column missing. Run convert_crs_and_calculate_area first.")

    if "road_length_km" not in gdf.columns:
        raise ValueError("road_length_km column missing. Run compute_road_length_by_municipality first.")

    gdf["road_density"] = gdf["road_length_km"] / gdf["area_sqkm"]

    print("\n--- ROAD DENSITY STATS ---")
    print(gdf["road_density"].describe())

    return gdf


def compute_property_intelligence_score(gdf):
    print("\n--- PROPERTY INTELLIGENCE SCORE ---")

    df = gdf.copy()

    # -----------------------------
    # 1. NORMALIZE ROAD DENSITY
    # -----------------------------
    df["density_score"] = (
        df["road_density"] / df["road_density"].max()
    ) * 100

    # -----------------------------
    # 2. NORMALIZE ROAD LENGTH
    # -----------------------------
    df["road_score"] = (
        df["road_length_km"] / df["road_length_km"].max()
    ) * 100

    # -----------------------------
    # 3. COMPOSITE SCORE
    # -----------------------------
    df["property_intelligence_score"] = (
        (0.6 * df["density_score"]) +
        (0.4 * df["road_score"])
    )

    print("\n--- SCORE STATS ---")
    print(df["property_intelligence_score"].describe())

    return df


def classify_municipality(df):
    conditions = [
        df["property_intelligence_score"] >= 75,
        df["property_intelligence_score"] >= 40
    ]

    choices = ["Urban", "Suburban"]

    df["classification"] = "Rural"
    df.loc[conditions[0], "classification"] = "Urban"
    df.loc[conditions[1], "classification"] = "Suburban"

    return df


