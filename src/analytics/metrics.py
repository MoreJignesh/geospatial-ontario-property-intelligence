import pandas as pd


def dataset_summary(gdf):
    """Print basic dataset information."""

    print("\n========== DATASET SUMMARY ==========")

    print(f"Total municipalities : {len(gdf)}")

    print(f"Columns : {len(gdf.columns)}")

    print("\nColumns")

    print(list(gdf.columns))


def road_density_summary(gdf):

    print("\n========== ROAD DENSITY ==========")

    print(gdf["road_density"].describe())


def top_road_density(gdf, n=10):

    print(f"\n========== TOP {n} ROAD DENSITY ==========")

    cols = [
        "MUNICIPAL_NAME",
        "road_density",
        "road_length_km",
        "area_sqkm",
    ]

    print(
        gdf[cols]
        .sort_values("road_density", ascending=False)
        .head(n)
    )


def lowest_road_density(gdf, n=10):

    print(f"\n========== LOWEST {n} ROAD DENSITY ==========")

    cols = [
        "MUNICIPAL_NAME",
        "road_density",
        "road_length_km",
        "area_sqkm",
    ]

    print(
        gdf[cols]
        .sort_values("road_density")
        .head(n)
    )


def municipalities_without_roads(gdf):

    no_roads = gdf[gdf["road_length_km"] == 0]

    print("\n========== MUNICIPALITIES WITHOUT ROADS ==========")

    print(f"Count : {len(no_roads)}")


def largest_municipalities(gdf, n=10):

    print(f"\n========== LARGEST {n} MUNICIPALITIES ==========")

    cols = [
        "MUNICIPAL_NAME",
        "area_sqkm",
        "road_length_km",
    ]

    print(
        gdf[cols]
        .sort_values("area_sqkm", ascending=False)
        .head(n)
    )

def municipality_profile(gdf, municipality_name):
    """Display metrics for a single municipality."""

    result = gdf[
        gdf["MUNICIPAL_NAME"]
        .str.upper()
        == municipality_name.upper()
    ]

    if result.empty:
        print(f"{municipality_name} not found.")
        return

    print(result[[
        "MUNICIPAL_NAME",
        "MUNICIPAL_TYPE",
        "area_sqkm",
        "road_length_km",
        "road_density"
    ]])


def project_kpis(gdf):

    print("\n========== PROJECT KPIs ==========")

    print(f"Municipalities: {len(gdf)}")

    print(f"Average Area (km²): {gdf['area_sqkm'].mean():.2f}")

    print(f"Average Road Density: {gdf['road_density'].mean():.2f}")

    print(f"Total Road Length: {gdf['road_length_km'].sum():,.0f} km")

    print(f"Municipalities Without Roads: {(gdf['road_length_km']==0).sum()}")


def compare_municipalities(gdf, municipality1, municipality2):

    comparison = gdf[
        gdf["MUNICIPAL_NAME"].isin(
            [municipality1, municipality2]
        )
    ]

    print(comparison[
        [
            "MUNICIPAL_NAME",
            "area_sqkm",
            "road_length_km",
            "road_density",
        ]
    ])



def top_property_score(gdf):

    print("\n========== TOP PROPERTY SCORE ==========")

    print(
        gdf[
            [
                "MUNICIPAL_NAME",
                "property_score",
                "road_density",
            ]
        ]
        .sort_values(
            "property_score",
            ascending=False,
        )
        .head(10)
    )


def bottom_property_score(gdf):

    print("\n========== LOWEST PROPERTY SCORE ==========")

    print(
        gdf[
            [
                "MUNICIPAL_NAME",
                "property_score",
                "road_density",
            ]
        ]
        .sort_values(
            "property_score"
        )
        .head(10)
    )


def project_summary(gdf):

    print("\n========== PROJECT SUMMARY ==========")

    print(f"Municipalities : {len(gdf)}")

    print(f"Unique Municipalities : {gdf['MUNICIPAL_NAME'].nunique()}")

    print(f"Average Area : {gdf['area_sqkm'].mean():.2f} km²")

    print(f"Average Road Density : {gdf['road_density'].mean():.2f}")

    print(f"Average Property Score : {gdf['property_score'].mean():.2f}")