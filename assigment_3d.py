# -*- coding: utf-8 -*-
"""Assigment_3d.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1I8I_IqOv7fsX_Mm3iI46KMF2DJiTUpcr
"""

import pandas as pd

# Data for Malaysia tourist attractions including the 5 additional locations
data = [
    {
        "Name": "Petronas Twin Towers",
        "Description": "The tallest twin towers in the world.",
        "Category": "Landmark",
        "State": "Kuala Lumpur",
        "Opening Hours": "9:00 AM - 9:00 PM",
        "Admission Fee": "RM80",
        "Official Website": "http://www.petronastwintowers.com.my",
        "Latitude": 3.1578,
        "Longitude": 101.7116
    },
    {
        "Name": "Langkawi Sky Bridge",
        "Description": "An iconic cable-stayed bridge with stunning views of Langkawi.",
        "Category": "Nature",
        "State": "Langkawi",
        "Opening Hours": "10:00 AM - 6:00 PM",
        "Admission Fee": "RM50",
        "Official Website": "http://www.langkawiskybridge.com",
        "Latitude": 6.3208,
        "Longitude": 99.7210
    },
    {
        "Name": "Batu Caves",
        "Description": "A limestone hill with caves and Hindu temples.",
        "Category": "Cultural",
        "State": "Kuala Lumpur",
        "Opening Hours": "6:00 AM - 9:00 PM",
        "Admission Fee": "Free",
        "Official Website": "https://www.batucaves.com",
        "Latitude": 3.2364,
        "Longitude": 101.6831
    },
    {
        "Name": "Mount Kinabalu",
        "Description": "The highest peak in Malaysia and a UNESCO World Heritage site.",
        "Category": "Nature",
        "State": "Sabah",
        "Opening Hours": "24 Hours",
        "Admission Fee": "RM200",
        "Official Website": "https://www.mountkinabalu.com",
        "Latitude": 6.0820,
        "Longitude": 116.5583
    },
    {
        "Name": "Taman Negara",
        "Description": "One of the oldest rainforests in the world.",
        "Category": "Nature",
        "State": "Pahang",
        "Opening Hours": "7:00 AM - 5:00 PM",
        "Admission Fee": "RM100",
        "Official Website": "https://www.tamannegara.my",
        "Latitude": 4.4675,
        "Longitude": 102.4212
    },
    {
        "Name": "Thean Hou Temple",
        "Description": "A popular Chinese temple offering panoramic views of Kuala Lumpur.",
        "Category": "Cultural",
        "State": "Kuala Lumpur",
        "Opening Hours": "9:00 AM - 6:00 PM",
        "Admission Fee": "Free",
        "Official Website": "http://www.theanhou.com",
        "Latitude": 3.1300,
        "Longitude": 101.6831
    },
    {
        "Name": "George Town",
        "Description": "The capital of Penang, known for its well-preserved colonial architecture.",
        "Category": "Cultural",
        "State": "Penang",
        "Opening Hours": "24 Hours",
        "Admission Fee": "Free",
        "Official Website": "https://www.georgetownpenang.com",
        "Latitude": 5.4140,
        "Longitude": 100.3354
    },
    {
        "Name": "Legoland Malaysia",
        "Description": "An amusement park with Lego-themed attractions and rides.",
        "Category": "Amusement",
        "State": "Johor",
        "Opening Hours": "9:00 AM - 6:00 PM",
        "Admission Fee": "RM150",
        "Official Website": "http://www.legoland.com.my",
        "Latitude": 1.3983,
        "Longitude": 103.6282
    },
    {
        "Name": "Perhentian Islands",
        "Description": "Beautiful tropical islands with clear waters and sandy beaches.",
        "Category": "Nature",
        "State": "Terengganu",
        "Opening Hours": "9:00 AM - 5:00 PM",
        "Admission Fee": "RM70",
        "Official Website": "https://www.perhentianisland.com",
        "Latitude": 5.9751,
        "Longitude": 102.6961
    },
    {
        "Name": "Merdeka Square",
        "Description": "A historic square in the heart of Kuala Lumpur, known for its colonial architecture.",
        "Category": "Landmark",
        "State": "Kuala Lumpur",
        "Opening Hours": "24 Hours",
        "Admission Fee": "Free",
        "Official Website": "http://www.merdekasquare.com",
        "Latitude": 3.1450,
        "Longitude": 101.6930
    }
]

# Create a DataFrame from the list of dictionaries
df = pd.DataFrame(data)

# Save the data to a CSV file
csv_file = "malaysia_tourist_attractions.csv"
df.to_csv(csv_file, index=False)

print(f"CSV file created: {csv_file}")

import streamlit as st
import folium
import pandas as pd
from folium import FeatureGroup
from streamlit_folium import st_folium

# Load the data from the CSV file
file_path = "malaysia_tourist_attractions.csv"  # Ensure this file exists
data = pd.read_csv(file_path)

# Define marker colors based on categories
category_colors = {
    "Landmark": "blue",
    "Cultural": "red",
    "Nature": "green",
    "Amusement": "orange"
}

# Create a base map centered on Malaysia
map_malaysia = folium.Map(location=[4.2105, 101.9758], zoom_start=6)

# Create a feature group for each category
categories = data["Category"].unique()
feature_groups = {category: FeatureGroup(name=category) for category in categories}

# Add markers for each attraction into their respective feature groups
for _, row in data.iterrows():
    # Define the color for the marker based on the category
    marker_color = category_colors.get(row["Category"], "gray")

    # Construct the popup content
    popup_content = (
        f"<b>{row['Name']}</b><br>"
        f"<i>Description</i>: {row['Description']}<br>"
        f"<i>Category</i>: {row['Category']}<br>"
        f"<i>State</i>: {row['State']}<br>"
        f"<i>Opening Hours</i>: {row['Opening Hours']}<br>"
        f"<i>Admission Fee</i>: {row['Admission Fee']}<br>"
        f"<i>Website</i>: <a href='{row['Official Website']}' target='_blank'>"
        f"{row['Official Website']}</a>"
    )

    # Add marker to the corresponding feature group
    folium.Marker(
        location=[row["Latitude"], row["Longitude"]],
        popup=folium.Popup(popup_content, max_width=300),
        tooltip=row["Name"],  # Tooltip to show the name of the attraction
        icon=folium.Icon(color=marker_color, icon="info-sign")
    ).add_to(feature_groups[row["Category"]])

# Add feature groups to the map
for category, group in feature_groups.items():
    group.add_to(map_malaysia)

# Add layer control for toggling categories
folium.LayerControl().add_to(map_malaysia)

# Streamlit App
st.title("Interactive Map of Malaysia Tourist Attractions")

# Display the map
st.write("Toggle attraction categories using the layer control below the map.")
st_folium(map_malaysia, width=800, height=600)

# Display the total number of attractions at the bottom
total_attractions = len(data)
st.markdown("<hr>", unsafe_allow_html=True)
st.write(f"### Total Tourist Attractions: {total_attractions}")