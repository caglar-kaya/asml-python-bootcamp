import streamlit as st
import pandas as pd
import numpy as np
import time

"""
# Main concepts of Streamlit
"""

"""
## 1. Display and style data
"""

"""
### 1.1. Use magic
"""

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

"""
### 1.2. Write a data frame
"""

st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))

st.table(dataframe.style.highlight_max(axis=0))

"""
### 1.3. Draw a bar chart
"""

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.bar_chart(chart_data)

"""
### 1.4. Draw a line chart
"""

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

"""
### 1.5. Plot a map
"""

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

"""
## 2. Widgets
"""

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

st.text_input("Your name", key="name")

st.write('Your name : ', st.session_state.name)

"""
### 2.1. Use checkboxes to show/hide data
"""

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data

"""
### 2.2. Use a selectbox for options
"""

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
        'Which number do you like best?',
         df['first column']
     )

'You selected: ', option

"""
## 3. Layout
"""

add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

st.write('You would like to be contacted via : ', add_selectbox)

add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

st.write('Your slider values : ', add_slider)
st.write('Your slider min choice : ', add_slider[0])
st.write('Your slider max choice : ', add_slider[1])

left_column, right_column = st.columns(2)

left_column.button('Press me!')

with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")

"""
### 3.1 Show progress
"""

'Starting a long computation...'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'
