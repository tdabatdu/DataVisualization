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

##Static Setup
state_geo = requests.get('https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/us-states.json').text
df = pd.read_csv('SturmData_csv.txt')

#content for the maps to loop through
sets = [
    ['debtfree', 'Year Women Property Rights Protected from Husband Debt'],
    ['effectivemwpa', 'Year Women Gained Control Over Their Property'],
    ['earnings', 'Year Women Gained Control of Their Wages'],
    ['wills', 'Year Women Gained Independent Estate'],
    ['soletrader', 'Year Women Gained Right to Business Without Husband']   
    ]


#function to produce the maps
def map(column, desc, color):
    #create map
    m = folium.Map(location=[39, -98], zoom_start=4)
    
    #choropleth
    folium.Choropleth(
        geo_data=state_geo,
        name='choropleth',
        data=df,
        columns=['state', column],
        key_on='feature.id',
        fill_color=color,
        fill_opacity=1,
        line_opacity=.1,
        line_weight = 2,
        nan_fill_color='White',
        legend_name=desc,
    ).add_to(m)
    
    #geo data
    gdf = gpd.read_file(state_geo)

    #account for nulls
    nans = df[df[column].isna()]['state'].values
    gdf_nans=gdf[gdf['id'].isin(nans)]
    
    #show nulls
    sp = StripePattern(angle=45, color='grey', space_color='white')
    sp.add_to(m)
    folium.GeoJson(data=gdf_nans, style_function=lambda x :{'fillPattern': sp}).add_to(m)
    folium.LayerControl().add_to(m)
    
    m.save(column + color + '.html')
    #print('Map Save')

    #open map in browser.  This appears to be the best way to do this.  
    webbrowser.open(column + color + '.html')


#main, loop through all the maps, gray scale at the end
if __name__ == '__main__':
    
    #Loop through all the maps
    for set in sets:
        map(set[0], set[1], 'Reds')
        
        
    #example for the grayscale print    
    print('Example for Grayscale Print')
    map(sets[3][0],'Example for Grayscale print', 'Greys')
        
        
        
        
        
        
        
        
    