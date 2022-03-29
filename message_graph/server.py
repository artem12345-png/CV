import streamlit as st
from main import get_graph, get_download_graph


def graph():
    pattern = st.text_input("Слово, которое мы хотим найти в сообщениях")
    time_from = st.text_input("от какого времени (указывать в формате год-месяц-день)")
    time_to = st.text_input("по какое время мы хотим найти (указывать в формате год-месяц-день)")
    max_thikness = st.text_input("параметр задает на сколько групп надо разбить уже отфильтрованные данные", value=10)
    border = st.text_input("порог фильтрации данных, если вы укажите 0,9 то получите 10% с конца"
                           "(то есть последние 10% наибольших данных)", value=0.9)
    if (pattern and time_from and time_to) != "":
        st.graphviz_chart(get_graph(pattern=pattern, time_from=time_from, time_to=time_to,
                                    max_thikness=int(max_thikness), border=float(border)))
        st.download_button(label="Скачать граф", data=get_download_graph())


graph()


