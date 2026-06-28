

def executive_summary(gdf):

    print("\n========== EXECUTIVE SUMMARY ==========\n")

    print("Municipalities :", len(gdf))

    print(
        "Average Road Density:",
        round(gdf["road_density"].mean(), 2)
    )

    print(
        "Highest Property Score:"
    )

    print(
        gdf.nlargest(
            5,
            "property_score"
        )[
            [
                "MUNICIPAL_NAME",
                "property_score"
            ]
        ]
    )
    print("Top Municipality:")
    print(gdf.sort_values("property_score", ascending=False)
          [["MUNICIPAL_NAME", "property_score"]].head(1))

    print("\nLowest Municipality:")
    print(gdf.sort_values("property_score")
          [["MUNICIPAL_NAME", "property_score"]].head(1))

    print("\nAverage Score:", gdf["property_score"].mean())