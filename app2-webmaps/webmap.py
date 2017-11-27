import folium 
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
ev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


map  = folium.Map(location = [45.523, -122.675], tiles="Mapbox Bright",zoom_start=6)

fgv = folium.FeatureGroup(name="VOlcanoes")

for lt,ln,el in zip(lat,lon,ev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln],radius=6,popup=str(el)+" m",
        fill_color = color_producer(el),fill=True, color='grey',fill_opacity=0.7))

map.add_child(fgv)
map.add_child(folium.LayerControl())
map.save("webmap.html")
