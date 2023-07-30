# импортируем библиотеки
import pandas as pd
import numpy as np
import streamlit as st
import xlrd

# импортируем пакет
import dill

# функция запуска веб-интерфейса
def run():
    from PIL import Image
    image = Image.open('logo.jpg')
    
    st.sidebar.image(image)
    
    question = ("Выберите действие:")
    
    add_selectbox = st.sidebar.selectbox(question, ("Загрузка данных", "Построение модели", "Прогнозирование неуспеваемости"))
    
    sidebar_ttl = ("Методика прогнозирования\n"
                  "академической неуспеваемости студентов.")
    
    if add_selectbox == "Загрузка данных":
        st.sidebar.info(sidebar_ttl)
        st.title(<center>"Загрузка данных"</center>)
              
        file_abit_upload_ttl = ("Загрузите Excel-файл с данными абитуриентов\n"
                          "для построения модели:")
        file_abit_upload = st.file_uploader(file_abit_upload_ttl,
                                       type = ['xls' or 'xlsx'],
                                       accept_multiple_files = False,
                                       help = 'принимаются файлы с расширением xls или xlsx')
        
        if file_abit_upload is not None:
            df_abit = pd.DataFrame()
            data_abit = pd.read_excel(file_abit_upload,
                                      sheet_name = "Абитуриенты",
                                      header = 9)
            df_abit = pd.concat([df_abit, data_abit],
                                ignore_index = True)           
            # вывод данных на веб-странице
            check_abit = st.checkbox('Посмотреть данные абитуриентов')
            if check_abit:
                st.success("Данные абитуриентов:")
                st.write(df_abit)

        file_stud_upload_ttl = ("Загрузите Excel-файл с данными студентов\n"
                          "для построения модели:")
        file_stud_upload = st.file_uploader(file_stud_upload_ttl,
                                       type = ['xls' or 'xlsx'],
                                       accept_multiple_files = False,
                                       help = 'принимаются файлы с расширением xls или xlsx')
        
        if file_stud_upload is not None:
            df_stud = pd.DataFrame()
            data_stud = pd.read_excel(file_stud_upload,
                                      sheet_name = "Обучающиеся",
                                      header = 3)
            df_stud = pd.concat([df_stud, data_stud],
                                ignore_index = True)
            # вывод данных на веб-странице
            st.success("Данные абитуриентов:")
            st.write(df_stud)    
        
    if add_selectbox == "Построение модели":
        st.sidebar.info(sidebar_ttl)
        st.title("Построение модели")

    if add_selectbox == "Прогнозирование неуспеваемости":
        st.sidebar.info(sidebar_ttl)
        st.title("Прогнозирование неуспеваемости")

if __name__ == '__main__':
    run()
