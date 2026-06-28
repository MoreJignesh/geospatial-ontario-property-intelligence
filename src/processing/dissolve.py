import geopandas as gpd


def dissolve_municipalities(gdf):

    print("\n========== DISSOLVING MUNICIPALITIES ==========")

    print(f"Rows Before : {len(gdf)}")

    dissolved = (
        gdf
        .dissolve(
            by="MUNICIPAL_NAME",
            as_index=False
        )
    )

    print(f"Rows After : {len(dissolved)}")

    return dissolved