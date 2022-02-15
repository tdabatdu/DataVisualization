'''
@author: Tyler Dabat
'''

import requests
import pandas as pd
import geopandas as gpd
import numpy as np
import folium
from folium.plugins import StripePattern
from IPython.display import HTML, display
import webbrowser
from shapely.geometry import Polygon, shape
import json
import pickle
#import scipy.special
from bokeh.layouts import gridplot
from bokeh.plotting import figure, show


df = pd.DataFrame(pd.read_csv('capitals_lat_lon_csv.txt', sep='\t'))
m = folium.Map(location=[39, -98], zoom_start=4)

def part1():
    markers = df.apply(mapMarker, 1)
    m.save('Part1.html')
    webbrowser.open('Part1.html')
    
def mapMarker(row):
    #print(np.array(row[['Latitude', 'Longitude']].values))
    #No idea why it wont let me cast it to an array, but this works
    folium.Marker([row['Latitude'], row['Longitude']], popup=row['Capital']).add_to(m)
    
    
def part2():  
    pointa = [-19.023542,31.346251]
    pointb = [33.882100,30.677808]
    pointc = [31.348264,-40.503359]
    
    africa = Polygon([pointc,pointa,pointb]) 
    m2 = folium.Map([30, 30], zoom_start=.5)
    folium.GeoJson(africa).add_to(m2)
    
    m2.save('Part2.html')
    webbrowser.open('Part2.html')
    
    #shapely assumes flat 2d space, so this can be used for area
    print('Area of Triangle:',africa.area)
    
    
def part3():
    geoText = '{"type":"FeatureCollection","features":[{"type":"Feature","id":"KS","properties":{"name":"Kansas"},"geometry":{"type":"Polygon","coordinates":[[[-102.040682,39.985985],[-102.012998,37.029699],[-94.635262,37.029699],[-94.967468,39.847971]]]}},{"type":"Feature","id":"NE","properties":{"name":"Nebraska"},"geometry":{"type":"Polygon","coordinates":[[[-104.048849,41.023665],[-104.037540,42.989664],[-96.981191,42.741012],[-95.511118,40.052574],[-102.035980,40.02661],[-102.047288,40.989530]]]}} ]}'
    
    with open('part3.json', 'w') as file:
        file.write(geoText)
        file.close
    
    with open('part3.json', 'r') as input_:
        #print(input_)
        geo = input_.read()

    
    m3 = folium.Map(location=[39, -98], zoom_start=4)
    
    #choropleth
    folium.Choropleth(
        geo_data=geo,
        name='choropleth',
        #data=df,
        #columns=['state', column],
        key_on='feature.id',
        fill_color='Blues',
        fill_opacity=1,
        line_opacity=.1,
        line_weight = 2,
        nan_fill_color='White',
        #legend_name=desc,
    ).add_to(m3)
    
    m3.save('Part3.html')
    webbrowser.open('Part3.html')
    
    
def part4():
    state_geo = json.loads(requests.get('https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/us-states.json').text)
    df = pd.read_csv('states.txt')
    df = df.apply(happiness_gen, 1)
    df.loc[len(df.index)] = [48,"AK", 1]
    df.loc[len(df.index)] = [49,"HI", 99]
    
    
    for feature in state_geo["features"]:
        #print(feature["id"])
        #print(df.loc[df["state"] == feature["id"]]["happy"].values[0])
        feature["properties"]["Happiness"] = int(df.loc[df["state"] == feature["id"]]["happy"].values[0])
        
    
    m4 = folium.Map(location=[39, -98], zoom_start=3)
    
    #choropleth
    map = folium.Choropleth(
        geo_data=state_geo,
        name='choropleth',
        data=df,
        columns=['state', 'happy'],
        key_on='feature.id',
        fill_color='Blues',
        fill_opacity=1,
        line_opacity=.1,
        line_weight = 2,
        nan_fill_color='White',
        legend_name='Happiness Index',
    ).add_to(m4)
    
    map.geojson.add_child(folium.features.GeoJsonTooltip(['name', 'Happiness'], labels=True))
    
    m4.save('Part4.html')
    webbrowser.open('Part4.html')
    
    
def happiness_gen(row):
    #THought I might sneak this in here
    if row['state'] == 'NC':
        row['happy'] = 101
    else:
        row['happy'] = np.random.randint(0,100)
    
    return row


def part5():
    print()

    rnd = np.random.exponential(1, 500)
    hist, edges = np.histogram(rnd, density=True, bins=25)

    x = np.linspace(-2, 2, 1000)

    p5 = make_plot("Exponential Distribution", hist, edges, x )
    
    show(p5)
    
    
    
    
def make_plot(title, hist, edges, x):
    plot = figure(title=title, tools='', background_fill_color="#fafafa")
    plot.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:],
           fill_color="orange", line_color="white", alpha=0.5)
    plot.y_range.start = 0
    #no legend even though doc has code for it
    #plot.legend.location = "center_right"
    plot.legend.background_fill_color = "#fefefe"
    plot.xaxis.axis_label = 'x'
    plot.yaxis.axis_label = 'Pr(x)'
    #plot.grid.grid_line_color="white"
    return plot
    
    

if __name__ == '__main__':
    #Part 1
    print('Part 1 opens Part1.html in browser')
    part1()
    
    print('Part 2 opens Part2.html in browser')
    part2()
    
    #Part 3
    print('Part 3 opens Part3.html in browser')
    part3()
    
    #Part 4
    print('Part 4 opens Part4.html in browser')
    part4()
    
    print('Part 5 hopefully also opens in the browser, but in a different way')
    part5()

    
    
    
