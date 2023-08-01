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
    
    add_selectbox = st.sidebar.selectbox(question, ("Загрузка данных",
                                                    "Подготовка данных",
                                                    "Обработка данных",
                                                    "Построение модели",
                                                    "Прогнозирование неуспеваемости"))
    
    sidebar_ttl = ("Методика прогнозирования\n"
                  "академической неуспеваемости студентов.")

# загрузка данных
    
    if add_selectbox == "Загрузка данных":
        st.sidebar.info(sidebar_ttl)
        st.title("Загрузите Excel-файлы с данными из ЕАИСУ")
              
        file_abit_upload_ttl = ("Абитуриенты:")
        file_abit_upload = st.file_uploader(file_abit_upload_ttl,
                                       type = ['xls' or 'xlsx'],
                                       help = 'перетащите сюда файл, скачанный из модуля "Абитуриенты"')
        
        if file_abit_upload is not None:
            df_abit = pd.read_excel(file_abit_upload,
                                    sheet_name = "Абитуриенты",
                                    header = 9)        
            # вывод данных на веб-странице
            check_abit = st.checkbox('Посмотреть данные абитуриентов')
            if check_abit:
                st.write(df_abit)

        files_mon_all_upload_ttl = ("Мониторинг (все студенты):")
        files_mon_all_upload = st.file_uploader(files_mon_all_upload_ttl,
                                                type = ['xls' or 'xlsx'],
                                                accept_multiple_files = True,
                                                help = 'перетащите сюда файлы, скачанные из модуля "Мониторинг образовательного процесса"')
        
        if files_mon_all_upload is not None:
            df_mon_all = pd.DataFrame()
            for file_mon_all_upload in files_mon_all_upload:
                data_mon_all = pd.read_excel(file_mon_all_upload,
                                             sheet_name = "Список студентов",
                                             header = 3)
                df_mon_all = pd.concat([df_mon_all, data_mon_all],
                                       ignore_index = True)
        if len(df_mon_all.index) > 0:
            # вывод на веб-странице данных мониторинга (все студенты)
            check_mon_all = st.checkbox('Посмотреть данные мониторинга (все студенты)')
            if check_mon_all:
                st.write(df_mon_all) 
                
        files_mon_neat_upload_ttl = ("Мониторинг (не аттестованы):")
        files_mon_neat_upload = st.file_uploader(files_mon_neat_upload_ttl,
                                                type = ['xls' or 'xlsx'],
                                                accept_multiple_files = True,
                                                help = 'перетащите сюда файлы, скачанные из модуля "Мониторинг образовательного процесса"')
        
        if files_mon_neat_upload is not None:
            df_mon_neat = pd.DataFrame()
            for file_mon_neat_upload in files_mon_neat_upload:
                data_mon_neat = pd.read_excel(file_mon_neat_upload,
                                             sheet_name = "Список студентов",
                                             header = 3)
                df_mon_neat = pd.concat([df_mon_neat, data_mon_neat],
                                       ignore_index = True)
        if len(df_mon_neat.index) > 0:
            # вывод на веб-странице данных мониторинга (не аттестованы)
            check_mon_neat= st.checkbox('Посмотреть данные мониторинга (не аттестованы)')
            if check_mon_neat:
                st.write(df_mon_neat)
       
        files_mon_neud_upload_ttl = ('Мониторинг (имеют "неудовл"):')
        files_mon_neud_upload = st.file_uploader(files_mon_neud_upload_ttl,
                                                type = ['xls' or 'xlsx'],
                                                accept_multiple_files = True,
                                                help = 'перетащите сюда файлы, скачанные из модуля "Мониторинг образовательного процесса"')
        
        if files_mon_neud_upload is not None:
            df_mon_neud = pd.DataFrame()
            for file_mon_neud_upload in files_mon_neud_upload:
                data_mon_neud = pd.read_excel(file_mon_neud_upload,
                                             sheet_name = "Список студентов",
                                             header = 3)
                df_mon_neud = pd.concat([df_mon_neud, data_mon_neud],
                                       ignore_index = True)
        if len(df_mon_neud.index) > 0:
            # вывод на веб-странице данных мониторинга (имеют "неудовл")
            check_mon_neud = st.checkbox('Посмотреть данные мониторинга (имеют "неудовл")')
            if check_mon_neud:
                st.write(df_mon_neud)
                
        files_mon_usp_upload_ttl = ("Мониторинг (успевают):")
        files_mon_usp_upload = st.file_uploader(files_mon_usp_upload_ttl,
                                                type = ['xls' or 'xlsx'],
                                                accept_multiple_files = True,
                                                help = 'перетащите сюда файлы, скачанные из модуля "Мониторинг образовательного процесса"')
        
        if files_mon_usp_upload is not None:
            df_mon_usp = pd.DataFrame()
            for file_mon_usp_upload in files_mon_usp_upload:
                data_mon_usp = pd.read_excel(file_mon_usp_upload,
                                             sheet_name = "Список студентов",
                                             header = 3)
                df_mon_usp = pd.concat([df_mon_usp, data_mon_usp],
                                       ignore_index = True)
        if len(df_mon_usp.index) > 0:
            # вывод на веб-странице данных мониторинга (успевают)
            check_mon_usp = st.checkbox('Посмотреть данные мониторинга (успевают)')
            if check_mon_usp:
                st.write(df_mon_usp)

        file_stud_upload_ttl = ("Студенты:")
        file_stud_upload = st.file_uploader(file_stud_upload_ttl,
                                            type = ['xls' or 'xlsx'],
                                            help = 'перетащите сюда файл, скачанный из модуля "Студенты"')
        
        if file_stud_upload is not None:
            df_stud = pd.read_excel(file_stud_upload,
                                    sheet_name = "Обучающиеся",
                                    header = 3)
            # вывод данных на веб-странице
            check_stud = st.checkbox('Посмотреть данные студентов')
            if check_stud:
                st.write(df_stud)

        if len(df_mon_all.index) == len(df_mon_neat.index) + len(df_mon_neud.index) + len(df_mon_usp.index):
            go_2 = st.button('Обработать данные')
            if go_2:
                st.write(":smile:")                

# подготовка данных
    
    if add_selectbox == "Подготовка данных":
        st.sidebar.info(sidebar_ttl)
        st.title("Подготовка данных")

# обработка данных
    
    if add_selectbox == "Обработка данных":
        st.sidebar.info(sidebar_ttl)
        st.title("Обработка данных")
    
# построение модели
    
    if add_selectbox == "Построение модели":
        st.sidebar.info(sidebar_ttl)
        st.title("Построение модели")

# прогнозирование неуспеваемости
    
    if add_selectbox == "Прогнозирование неуспеваемости":
        st.sidebar.info(sidebar_ttl)
        st.title("Прогнозирование неуспеваемости")

if __name__ == '__main__':
    run()
