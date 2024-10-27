from datetime import datetime, timedelta, time

import pandas as pd
import requests
import streamlit as st
from urllib3 import request

from bl import endpoint_dct, resolution_dct, cohort_dct, success_lst
from config import Config
from utils import UtcDate

endpoints = endpoint_dct.keys()
timeframes = resolution_dct.keys()
cohorts = cohort_dct.values()

if 'is_valid' not in st.session_state:
    st.session_state.disabled = True

def select_endpoint():
    key = st.session_state.selected_endpoint
    val = f'Ваш выбор: {endpoint_dct[key]}'
    container_2.write(val)

def validate_request():
    key = st.session_state.selected_endpoint
    st.session_state.is_valid = key is not None


def get_request_url() -> str:
    """Собрать запрос к сервису"""
    dt_from = datetime.combine(from_dt, from_tm)
    ts_from = UtcDate.dt2ts(dt_from)

    dt_to = datetime.combine(to_dt, to_tm)
    ts_to = UtcDate.dt2ts(dt_to)

    idx = list(cohort_dct.values()).index(cohort)
    cogort = list(cohort_dct.keys())[idx]

    resolution = resolution_dct[timeframe] // 60

    key = st.session_state.selected_endpoint
    endpoint = endpoint_dct[key]

    url = Config().base_url
    url = (f"{url}{endpoint}?from={ts_from}&to={ts_to}&countback={count_back}&resolution={resolution}&cogort={cogort}&"
           f"label={label}&success={success}")
    return url


st.set_page_config(
    page_title="Whale-cohort-2.0",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "Приложение для обращения к сервису **Whale-cohort-2.0**"
    }
)

st.title('Whale-Cohorts 2.0 Control Panel')
container_2 = st.sidebar.container()


endpoint = container_2.selectbox(
    "**Выбрать endpoint**",
    endpoints,
    index=None,
    placeholder="Select endpoint...",
    on_change=validate_request,
    key='selected_endpoint'
)

timeframe = container_2.selectbox(
    "**Выбрать период**",
    timeframes,
    index=0,
    placeholder="Select timeframe...",
    key='selected_timeframe'
)


cohort = container_2.selectbox(
    "**Выбрать когорту**",
    cohorts,
    index=2,
    placeholder="Select cohort...",
    key='selected_cohort'
)


success = container_2.selectbox(
    "**Выбрать успешность**",
    success_lst,
    index=0,
    placeholder="Select cohort...",
    key='selected_success'
)

label = container_2.radio(
    "**Метки кошельков**",
    options=['anylabel', 'nolabel'],
    # captions=['Любые', 'Без меток'],
    index=0,
    key='selected_label'
)

count_back = container_2.number_input(
    "**Количество точек**",
    min_value=1,
    value=24,
    key="selected count_back"
)

container_3 = st.sidebar.container()
with container_3.expander('Задайте начало периода'):
    # st.write('Введите метку времени или Дату + время начала')
    col31, col32 = st.columns([1, 1])
    from_dt = col31.date_input('Дата', format='DD.MM.YYYY', value=datetime.today() - timedelta(days=1), key="date_from")
    from_tm = col32.time_input('Время', value=time(0), key="time_from")

with container_3.expander('Задайте окончание периода'):
    col33, col34 = st.columns([1, 1])
    to_dt = col33.date_input('Дата', format='DD.MM.YYYY', value="today", key="date_to")
    to_tm = col34.time_input('Время', value=time(hour=23), key="time_to")


if st.sidebar.button("Выполнить запрос", disabled= not st.session_state.get('is_valid',False), key='do_btn'):
    url = get_request_url()
    st.write(url)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        t = data['t']
        c = data['c']
        df = pd.DataFrame({'ts': t, 'value': c})
        df_styled = df.style.format({'value': '{:,.3f}'})
        st.dataframe(df_styled, width=400)
        # st.table(df)


# start_date = st.date_input('Enter start date', value=datetime(2019,7,6))
# start_time = st.time_input('Enter start time')
# start_datetime = datetime.combine(start_date, start_time)

def main():
    pass

if __name__ == '__main__':
    main()
