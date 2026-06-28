

def municipality_rankings(gdf):

    ranking = (
        gdf[
            [
                "MUNICIPAL_NAME",
                "property_score",
                "property_class",
                "road_density",
                "area_sqkm"
            ]
        ]
        .sort_values(
            "property_score",
            ascending=False
        )
    )

    return ranking