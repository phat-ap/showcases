import streamlit as st
import plotly.graph_objects as go

# Sample data for the bar charts
data1 = {'x': ['A', 'B', 'C'], 'y': [10, 15, 20]}
data2 = {'x': ['D', 'E', 'F'], 'y': [7, 11, 17]}
data3 = {'x': ['G', 'H', 'I'], 'y': [5, 12, 14]}
data4 = {'x': ['J', 'K', 'L'], 'y': [9, 16, 13]}

# Function to create a Plotly bar chart
def create_bar_chart(data, title):
    fig = go.Figure(data=[go.Bar(x=data['x'], y=data['y'])])
    fig.update_layout(title=title, xaxis_title='Category', yaxis_title='Value')
    return fig

# Streamlit layout
st.title("Responsive Dashboard with Plotly Charts")

# Create a two-column layout that collapses to a single column on mobile
cols = st.columns(2)

# Display the first row of charts
with cols[0]:
    st.plotly_chart(create_bar_chart(data1, 'Chart 1'), use_container_width=True)
with cols[1]:
    st.plotly_chart(create_bar_chart(data2, 'Chart 2'), use_container_width=True)

# Display the second row of charts
with cols[0]:
    st.plotly_chart(create_bar_chart(data3, 'Chart 3'), use_container_width=True)
with cols[1]:
    st.plotly_chart(create_bar_chart(data4, 'Chart 4'), use_container_width=True)
