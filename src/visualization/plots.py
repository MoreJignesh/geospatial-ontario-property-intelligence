# Histogram of road density
# Histogram of area
# Scatter: area vs road density
# Scatter: area vs road length
# Interactive choropleth map



import plotly.express as px
import matplotlib.pyplot as plt

def plot_top_municipalities(gdf):

    top = gdf.sort_values("property_score", ascending=False).head(10)

    plt.figure(figsize=(10,5))
    plt.barh(top["MUNICIPAL_NAME"], top["property_score"])
    plt.gca().invert_yaxis()

    plt.title("Top 10 Municipalities by Property Score")
    plt.xlabel("Score")

    plt.tight_layout()
    plt.show()

def property_score_map(gdf):

    fig = px.choropleth(
        gdf,
        geojson=gdf.geometry,
        locations=gdf.index,
        color="property_score",
        hover_name="MUNICIPAL_NAME",
        projection="mercator",
        title="Ontario Property Intelligence Score"
    )

    fig.update_geos(fitbounds="locations", visible=False)

    fig.show()



# import plotly.express as px


# def road_density_histogram(gdf):

#     fig = px.histogram(
#         gdf,
#         x="road_density",
#         nbins=30,
#         title="Distribution of Road Density"
#     )

#     fig.show()


# def road_length_histogram(gdf):

#     fig = px.histogram(
#         gdf,
#         x="road_length_km",
#         nbins=30,
#         title="Distribution of Road Length"
#     )

#     fig.show()


# def area_distribution(gdf):

#     fig = px.histogram(
#         gdf,
#         x="area_sqkm",
#         nbins=30,
#         title="Municipality Area Distribution"
#     )

#     fig.show()


# def area_vs_density(gdf):

#     fig = px.scatter(
#         gdf,
#         x="area_sqkm",
#         y="road_density",
#         hover_name="MUNICIPAL_NAME",
#         title="Area vs Road Density"
#     )

#     fig.show()


# def area_vs_road_length(gdf):

#     fig = px.scatter(
#         gdf,
#         x="area_sqkm",
#         y="road_length_km",
#         hover_name="MUNICIPAL_NAME",
#         title="Area vs Road Length"
#     )

#     fig.show()


# def top10_road_density(gdf):
#     """
#     Top municipalities by road density.
#     """

#     top10 = (
#         gdf.sort_values(
#             "road_density",
#             ascending=False
#         )
#         .head(10)
#     )

#     fig = px.bar(
#         top10,
#         x="road_density",
#         y="MUNICIPAL_NAME",
#         orientation="h",
#         title="Top 10 Municipalities by Road Density"
#     )

#     fig.show()


# def area_vs_roads(gdf):
#     """
#     Scatter plot of municipality area vs road length.
#     """

#     fig = px.scatter(
#         gdf,
#         x="area_sqkm",
#         y="road_length_km",
#         hover_name="MUNICIPAL_NAME",
#         title="Municipality Area vs Road Length"
#     )

#     fig.show()