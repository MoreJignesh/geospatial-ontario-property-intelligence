
# What does the dataset contain?
# Are there missing values?
# How many unique municipalities?
# What are the geometry types?

import pandas as pd


def dataset_profile(gdf):

    print("\n========== DATA PROFILE ==========")

    print(f"Rows : {len(gdf)}")
    print(f"Columns : {len(gdf.columns)}")

    print("\nColumn Names")
    print(gdf.columns.tolist())

    print("\nData Types")
    print(gdf.dtypes)

    print("\nMissing Values")
    print(gdf.isna().sum())

    print("\nGeometry Types")
    print(gdf.geometry.geom_type.value_counts())

    print("\nUnique Municipality Names")
    print(gdf["MUNICIPAL_NAME"].nunique())

    print("\nDuplicate Municipality Records")

    duplicates = (
        gdf.groupby("MUNICIPAL_NAME")
           .size()
           .sort_values(ascending=False)
    )

    print(duplicates.head(20))


