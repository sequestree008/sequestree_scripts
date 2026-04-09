import streamlit as st
import leafmap.foliumap as foliumap
import folium
from branca.colormap import linear
from leafmap.foliumap import SplitControl
import config

def run(rasters, caption, range_min, range_max):

    biomass_rasters = rasters

    col1, col2 = st.columns(2)
    with col1:
        left_year = st.selectbox("Left Map (Year)", list(biomass_rasters.keys()), index=0)
    with col2:
        right_year = st.selectbox("Right Map (Year)", list(biomass_rasters.keys()), index=len(biomass_rasters)-1)

    m = foliumap.Map(center=[14.65, 121.05], zoom=12, basemap=None, tiles=None)

    print(f"The year selected is {left_year} || {right_year}")
    print(f"Left year files: {biomass_rasters[left_year]}")
    print(f"Right year files: {biomass_rasters[right_year]}")
    print(f"TiTiler endpoint: {config.TITILER_SERVER}")
    
# Assuming your function looks like: def run(files, caption, min, max):
import leafmap.foliumap as leafmap

# 1. Create the map (check if you use 'm' or 'map')
m = leafmap.Map() 

try:
    # 2. Try the split map using the 'files' you passed in
    m.split_map(
        left_layer=files[left_year], 
        right_layer=files[right_year],
        left_args={'palette': 'Greens', 'name': 'Left'},
        right_args={'palette': 'Greens', 'name': 'Right'}
    )
except Exception as e:
    st.error(f"Actual GIS Error: {e}")
    st.write("Checking the first file link:")
    st.write(list(files.values())[0]) # This prints the first link to see if it's 'clean'
    
   # m.split_map(
    #   left_layer=biomass_rasters[left_year],
      #  right_layer=biomass_rasters[right_year],
      #  left_args={'palette': 'Greens', 
           #        'vmin': range_min, 
           #        'vmax': range_max,
           #        'titiler_endpoint': config.TITILER_SERVER},
      #  right_args={'palette': 'Greens', 
             #       'vmin': range_min, 
           #         'vmax': range_max,
           #         'titiler_endpoint': config.TITILER_SERVER},
    #)
    #colormap = linear.Greens_09.scale(0, 2500)
    #colormap.caption = caption

    #m.add_colorbar(colors=colormap.colors, vmin=range_min, vmax=range_max, caption=caption)

    m.to_streamlit(height=600)

