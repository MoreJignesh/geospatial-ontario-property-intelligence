


import numpy as np
import pandas as pd


def calculate_property_score(gdf):

    print("\n========== PROPERTY INTELLIGENCE SCORE ==========")

    road_score = (
        gdf["road_density"]
        / gdf["road_density"].max()
    )

    area_score = (
        gdf["area_sqkm"]
        / gdf["area_sqkm"].max()
    )

    gdf["property_score"] = (
        road_score * 0.7
        + area_score * 0.3
    ) * 100

    gdf["property_score"] = gdf["property_score"].round(2)

    return gdf


