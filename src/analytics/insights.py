

def generate_insights(gdf):

    print("\n========== KEY INSIGHTS ==========")

    print("\nTop 10 municipalities by score:")
    print(
        gdf.sort_values("final_score", ascending=False)
        [["MUNICIPAL_NAME", "final_score"]]
        .head(10)
    )

    print("\nMost urban areas:")
    print(
        gdf.sort_values("road_density", ascending=False)
        [["MUNICIPAL_NAME", "road_density"]]
        .head(10)
    )

    print("\nMost rural areas:")
    print(
        gdf.sort_values("road_density")
        [["MUNICIPAL_NAME", "road_density"]]
        .head(10)
    )