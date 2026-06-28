

def calculate_final_score(gdf):

    # normalize
    gdf["road_density_norm"] = (
        gdf["road_density"] - gdf["road_density"].min()
    ) / (
        gdf["road_density"].max() - gdf["road_density"].min()
    )

    gdf["area_norm"] = (
        gdf["area_sqkm"] - gdf["area_sqkm"].min()
    ) / (
        gdf["area_sqkm"].max() - gdf["area_sqkm"].min()
    )

    # FINAL SCORE (weighted model)
    gdf["final_score"] = (
        gdf["road_density_norm"] * 0.7 +
        gdf["area_norm"] * 0.3
    ) * 100

    return gdf

