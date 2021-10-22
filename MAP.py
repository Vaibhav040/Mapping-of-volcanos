import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_production(elevation):
    if elevation < 1000:
        return "darkgreen"
    elif 1000 <= elevation < 2000:
        return "green"
    elif elevation >= 3000:
        return "red"       
    else:
        return "orange"    

map = folium.Map(locaton=[31.283705468004786, 77.16339078510579],zoom_start=6, tiles="Stamen Terrain")

fgv = folium.FeatureGroup(name="volcano")

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.Marker(location=[lt, ln], popup=el, icon=folium.Icon(color=color_production(el))))

fgp = folium.FeatureGroup(name="population")


fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), 
style_function=lambda x: {'fillcolor':'green' if x ['properties']['POP2005'] < 10000000 
else 'orange' if 10000000 <= x ['properties']['POP2005']<20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("MAP.html")