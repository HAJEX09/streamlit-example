import streamlit as st

# Используем текст с большим размером шрифта
x = st.markdown('<span style="font-size: 24px;">Большой текст</span>', unsafe_allow_html=True)

# Определяем переменную для хранения значения чекбокса
checkbox_value = st.checkbox("x")


# Связываем чекбокс с текстом
if checkbox_value:
    st.write("Чекбокс нажат")
else:
    st.write("Чекбокс не нажат")


# Создание флажка
is_expanded = st.markdown('<span style="font-size: 24px;"><input type="checkbox"> Нажми на меня</span>', unsafe_allow_html=True)


# Если флажок отмечен, отобразить контент
if is_expanded:
    st.write("Уважаемые пользователи,")
    st.write("Хотелось бы обратить ваше внимание на несколько важных аспектов, связанных с данным проектом. Пожалуйста, ознакомьтесь с этим дисклеймером, прежде чем использовать программу.")
    st.write("")
    st.write("Рак кожи - распространенное заболевание, которым страдает большое количество людей.")
    st.write("Выживаемость пациентов, у которых меланома выявлена на ранней стадии, составляет около 98 процентов.")
    st.write("Выживаемость пациентов, у которых болезнь достигает лимфатических узлов, снижается до 62 процентов.")
    st.write("Выживаемость пациентов, у которых болезнь метастазирует в отдаленные органы, падает до 18 процентов.")
    st.write("Раннее выявление имеет решающее значение!!!")
    st.write("")
    st.write("Этот веб-приложение предназначено исключительно в помощь людям. Оно создано с целью помочь пользователям получить предварительную оценку состояния кожи на основе изображения. Программа является инструментом, который может помочь вам в раннем обнаружении потенциальных проблем.")
    st.write("")
    st.write("Важно понимать, что результаты, полученные с помощью программы, не могут заменить профессиональную медицинскую консультацию. Рекомендуется обратиться к квалифицированному врачу для окончательной оценки и диагностики.")
    st.write("")
    st.write("Точность определения заболеваний кожи в большой степени зависит от качества предоставленного изображения. Изображения должны быть четкими, высокого разрешения, хорошо освещенными и предоставлять детальный вид места на коже, которое вас беспокоит. Помните, что низкое качество изображения может существенно ухудшить точность анализа.")
    st.write("")
    st.write("Предоставляемая информация и услуги основываются на технологии машинного обучения и не могут гарантировать 100% точности. Я не несу ответственности за любые возможные ошибки и неточности.")
    st.write("")
    st.write("Пользователи этого приложения несут полную ответственность за свои действия и решения, связанные с их здоровьем. При обнаружении любых изменений на коже или сомнениях, всегда обращайтесь к квалифицированному медицинскому специалисту.")
    st.write("")
    st.write("Пожалуйста, используйте эту систему ответственно, оценивайте ее возможности и ограничения адекватно. Заботьтесь о своем здоровье и не забывайте про регулярные медицинские осмотры.")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
