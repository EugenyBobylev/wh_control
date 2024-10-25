from datetime import datetime
from typing import Callable

import streamlit as st

from bl import endpoint_dct

endpoints = endpoint_dct.keys()

placeholder = st.empty()


def select_endpoint():
    key = st.session_state.selected_endpoint
    val = f'Ваш выбор: {endpoint_dct[key]}'
    cnt2.write(val)


# Define the on_change function
def on_change1():
    # Replace the placeholder with the actual widget
    cnt2.write("This is a widget", "123")


st.title('Whale-Cohorts 2.0 Control Panel')
cnt2 = st.sidebar.container()
cnt2.selectbox(
    "**Выбрать endpoint**",
    endpoints,
    index=None,
    placeholder="Select endpoint...",
    on_change=select_endpoint,
    key='selected_endpoint'
)


date = st.sidebar.date_input("Select a time")
st.sidebar.write("Selected time:", date)


start_date = st.date_input('Enter start date', value=datetime(2019,7,6))
start_time = st.time_input('Enter start time')

start_datetime = datetime.combine(start_date, start_time)


def main():
    pass


if __name__ == '__main__':
    main()
