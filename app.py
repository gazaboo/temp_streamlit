import streamlit as st


import pandas as pd
import random

plant_names = [
    "Oak", "Maple", "Pine", "Birch", "Willow", "Rose", "Sunflower", "Tulip", "Lily", "Daisy",
    "Cactus", "Fern", "Bamboo", "Palm", "Orchid", "Ivy", "Moss", "Lavender", "Aloe", "Yucca",
    "Spruce", "Fir", "Cedar", "Juniper", "Cypress", "Dogwood", "Magnolia", "Redwood", "Sequoia", "Baobab",
    "Hibiscus", "Jasmine", "Gardenia", "Lilac", "Azalea", "Hydrangea", "Peony", "Poppy", "Carnation", "Marigold",
    "Violet", "Dandelion", "Clover", "Mint", "Basil", "Rosemary", "Thyme", "Sage", "Parsley", "Dill",
    "Tomato", "Cucumber", "Pepper", "Eggplant", "Potato", "Carrot", "Broccoli", "Cabbage", "Lettuce", "Spinach",
    "Strawberry", "Raspberry", "Blueberry", "Blackberry", "Apple", "Orange", "Lemon", "Grape", "Banana", "Mango",
    "Fern", "Moss", "Bamboo", "Palm", "Orchid", "Ivy",
]

sizes = ["Small", "Medium", "Large"]
geographical_areas = ["North America", "South America", "Europe", "Asia", "Africa", "Australia"]

data = []
for _ in range(100):
    plant_name = random.choice(plant_names)
    size = random.choice(sizes)
    geographical_area = random.choice(geographical_areas)
    data.append([plant_name, size, geographical_area])

df = pd.DataFrame(data, columns=["plant name", "size", "geographical area"])


st.dataframe(df)