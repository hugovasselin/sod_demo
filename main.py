from bokeh.plotting import figure
import matplotlib.pyplot as plt
import streamlit as st
import altair as alt
from vega_datasets import data


source = data.cars()

st.title("My first app")

st.write("Here's our first attempt at using data to create a table")

st.markdown("### This is a [markdown](https://github.github.com/gfm)")

name = st.text_input("Enter your name", "Type here...")

st.markdown(f"<p style='color:red'>Hello my name is {name}</p>", unsafe_allow_html=True)

slider = st.slider("Slider title", 0, 100, 50)
check = st.checkbox("Checkbox title", ["Add a constant", "Add beta 1", "Add beta 2"])
radio = st.radio("Radio title", ["Yes", "No"])
txt = st.text_input("Type here")
txt_area = st.text_area("Type here")


button = st.button("Button name")

if button:
    st.balloons()
    
cols = st.columns(2)

with cols[0]:
    st.write("This is the first column")
    
with cols[1]:
    st.write("This is the second column")

brush = alt.selection(type='interval')

points = alt.Chart(source).mark_point().encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q',
    color=alt.condition(brush, 'Origin:N', alt.value('lightgray'))
).add_selection(
    brush
)

bars = alt.Chart(source).mark_bar().encode(
    y='Origin:N',
    color='Origin:N',
    x='count(Origin):Q'
).transform_filter(
    brush
)

total = points & bars
st.altair_chart(total)



p = figure()
p.circle(source['Horsepower'], source['Miles_per_Gallon'])
st.bokeh_chart(p)

st.header("Visualization")

st.subheader("Matplotlib")

plt.figure(figsize=(12,8))
plt.scatter(source['Horsepower'], source['Miles_per_Gallon'])
st.pyplot(plt)
