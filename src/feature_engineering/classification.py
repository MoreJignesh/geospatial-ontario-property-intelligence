

import pandas as pd




def calculate_property_score(gdf):

    road = (
        gdf["road_density"] -
        gdf["road_density"].min()
    ) / (
        gdf["road_density"].max() -
        gdf["road_density"].min()
    )

    area = (
        gdf["area_sqkm"] -
        gdf["area_sqkm"].min()
    ) / (
        gdf["area_sqkm"].max() -
        gdf["area_sqkm"].min()
    )

    gdf["property_score"] = (
        road * 0.70 +
        area * 0.30
    ) * 100

    gdf["property_class"] = pd.qcut(
            gdf["property_score"],
            q=5,
            labels=[
                "Very Low",
                "Low",
                "Medium",
                "High",
                "Very High"
            ]
        )
    
    return gdf