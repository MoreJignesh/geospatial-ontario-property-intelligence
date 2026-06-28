

import plotly.express as px


def road_density_map(gdf):

    fig = px.choropleth(
        gdf,
        geojson=gdf.geometry,
        locations=gdf.index,
        color="road_density",
        hover_name="MUNICIPAL_NAME",
        projection="mercator",
        title="Ontario Road Density"
    )

    fig.update_geos(
        fitbounds="locations",
        visible=False
    )

    fig.show()

    