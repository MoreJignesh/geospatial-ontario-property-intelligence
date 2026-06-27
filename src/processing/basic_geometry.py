def geometry_summary(gdf):
    print("\n--- MUNICIPALITY SUMMARY ---")

    print("Total municipalities:", len(gdf))

    print("\nType distribution:")
    print(gdf["MUNICIPAL_TYPE"].value_counts())

    print("\nCRS:", gdf.crs)

    print("\nMissing geometries:", gdf.geometry.isna().sum())