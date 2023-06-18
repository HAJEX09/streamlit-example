import streamlit as st

# Создание выпадающего меню
selected_option = st.selectbox('Выберите опцию', ('Опция 1', 'Опция 2', 'Опция 3'))

# Вывод выбранной опции
st.write('Выбранная опция:', selected_option)
