# импортируем библиотеки
import pandas as pd
import numpy as np
import streamlit as st
import xlrd
import io
from pandas import ExcelWriter
from io import BytesIO

# импортируем пакет
import dill

# функция запуска веб-интерфейса
def run():
    from PIL import Image
    image = Image.open('logo.jpg')
    
    st.sidebar.image(image)
    
    question = ("Выберите действие:")
    
    add_selectbox = st.sidebar.selectbox(question, ("Загрузка данных",
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

        df_abit = pd.DataFrame()
        df_stud = pd.DataFrame()
        df_mon_all = pd.DataFrame()
        df_mon_neud = pd.DataFrame()
        df_mon_neat = pd.DataFrame()
        df_mon_usp = pd.DataFrame()
        
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

        
        
        if len(df_abit.index) > 0 and len(df_mon_all.index) > 0 and len(df_stud.index) > 0:
            if len(df_mon_all.index) == len(df_mon_neat.index) + len(df_mon_neud.index) + len(df_mon_usp.index):
                go_2 = st.button('Записать данные в один файл')
                if go_2:
        # подготовка данных
        # подготовка абитуриенты
                    # удалим дубликаты абитуриентов
                    # совпадающие по первым 8 столбцам
                    data_ab_dd = df_abit.drop_duplicates(subset = ['ФИО',
                                                                   'Пол',
                                                                   'Дата рождения',
                                                                   'Тип УЛ',
                                                                   'Серия УЛ',
                                                                   'Номер УЛ',
                                                                   'Дата выдачи УЛ',
                                                                   'Кем выдано УЛ'])
                    # в столбцах с результатами
                    # Русский язык ЕГЭ и Математика ЕГЭ
                    # заменим пропуски и значения меньше 36 баллов
                    # значением 0 баллов
                    ege_rus = np.where((data_ab_dd['Ря'].isnull()) |
                                       (data_ab_dd['Ря'] < 36),
                                       0,
                                       data_ab_dd['Ря'])
                    ege_math = np.where((data_ab_dd['М'].isnull()) |
                                        (data_ab_dd['М'] < 36),
                                        0,
                                        data_ab_dd['М'])
                    # сконструируем столбец 'Обязательные ЕГЭ'
                    ege = pd.DataFrame(ege_rus + ege_math,
                                       columns = ['Обязательные ЕГЭ'])
                    # присвоим столбцу 'Обязательные ЕГЭ'
                    # такие же индексы как у массива data_ab_dd
                    ege_index = ege.set_index(data_ab_dd.index)
                    # присоеденим сконструированный столбец 'Обязательные ЕГЭ'
                    # к массиву data_ab_dd справа
                    data_ab_dd_ege = pd.concat([data_ab_dd, ege_index],
                                               axis = 1)
                    # отберем только нужные столбцы для слияния таблиц
                    data_ab_mer = data_ab_dd_ege[['ФИО',
                                                  'Пол',
                                                  'Дата рождения',
                                                  'Нуждается в общежитии',
                                                  'Полученное образование',
                                                  'Ср. балл док-та об образовании',
                                                  'Обязательные ЕГЭ']]

        # подготовка данных
        # подготовка студенты
                    # сконструируем столбец 'Тип договора'
                    data_st_eaisu = df_stud.copy()
                    data_st_eaisu['Тип договора'] = df_stud['Вид затрат'] + ' ' + df_stud['Целевой прием']
                    dct_tip_dog = {'бюджет да':'целевик',
                                   'бюджет нет':'бюджетник',
                                   'по договору нет':'платник'}
                    data_st_eaisu['Тип договора'] = data_st_eaisu['Тип договора'].map(dct_tip_dog)
                    # переименуем столбцы 'Формирующее подр.', 'Направление подготовки (специальность)' и 'Планируемый срок'
                    data_st_rn = data_st_eaisu.rename(columns = {'Формирующее подр.':'Факультет',
                                                                 'Планируемый срок':'Срок обучения',
                                                                 'Направление подготовки (специальность)':'Направление подготовки'})
                    # отберем только нужные столбцы для слияния таблиц
                    data_st_mer = data_st_rn[['ФИО',
                                              'Пол',
                                              'Дата рождения',
                                              'Гражданство',
                                              'Группа',
                                              'Факультет',
                                              'Направление подготовки',
                                              'Срок обучения',
                                              'Тип договора']]

        # подготовка данных
        # подготовка мониторинг
                    # массив мониторинга (все студенты)
                    data_m_all = df_mon_all.copy()
                    # в массив мониторинга (имеют неудовл)
                    # добавим справа столбец "Неуспеваемость"
                    # с одинаковым значением "1" по всем строкам
                    data_m_neud_neusp = df_mon_neud.assign(Неуспеваемость = 1)
                    # в массив мониторинга (не аттестовано)
                    # добавим справа столбец "Неуспеваемость"
                    # с одинаковым значением "1" по всем строкам
                    data_m_neat_neusp = df_mon_neat.assign(Неуспеваемость = 1)
                    # в массив мониторинга (успевают)
                    # добавим справа столбец "Неуспеваемость"
                    # с одинаковым значением "0" по всем строкам
                    data_m_usp_neusp = df_mon_usp.assign(Неуспеваемость = 0)
                    # объединим все массивы мониторинга
                    data_m = pd.concat([data_m_neud_neusp,
                                        data_m_neat_neusp,
                                        data_m_usp_neusp],
                                       ignore_index = True)
                    # отберем только нужные столбцы для слияния таблиц
                    data_m_mer = data_m[['ФИО',
                                         'Пол',
                                         'Дата рождения',
                                         'Неуспеваемость']]

        # подготовка данных
        # слияние данных
                    # выполним слияние таблиц данных студентов и мониторинга
                    data_st_m_mer = data_st_mer.merge(data_m_mer,
                                                      how = 'inner',
                                                      on = None,
                                                      left_on = None,
                                                      right_on = None,
                                                      left_index = False,
                                                      right_index = False,
                                                      sort = False,
                                                      suffixes = ('_x', '_y'),
                                                      copy = None,
                                                      indicator = False,
                                                      validate = None)
                    # выполним слияние таблиц данных студентов и мониторинга
                    # с данными абитуриентов
                    data_mer = data_st_m_mer.merge(data_ab_mer,
                                                   how = 'left',
                                                   on = None,
                                                   left_on = None,
                                                   right_on = None,
                                                   left_index = False,
                                                   right_index = False,
                                                   sort = False,
                                                   suffixes = ('_x', '_y'),
                                                   copy = None,
                                                   indicator = False,
                                                   validate = None)

        # формирование матриц данных
                    # сформируем матрицу идентификаторов
                    Data_id = data_mer[['ФИО',
                                        'Группа']]
                    # сформируем матрицу наблюдений
                    Data_X = data_mer[['Пол',
                                       'Нуждается в общежитии',
                                       'Полученное образование',
                                       'Гражданство',
                                       'Факультет',
                                       'Направление подготовки',
                                       'Срок обучения',
                                       'Тип договора',
                                       'Ср. балл док-та об образовании',
                                       'Обязательные ЕГЭ']]
                    Data_Y = data_mer['Неуспеваемость']
                    Data_XY = pd.concat([Data_X, Data_Y],
                                        axis = 1,
                                        join = "inner")
                    # сформируем матрицу данных
                    Data = pd.concat([Data_id, Data_XY],
                                     axis = 1,
                                     join = "inner")

        # создание возможности скачать массивы одним файлом
                    # напишем функцию для конвертирования всех массивов
                    # в один файл Excel
                    def dfs_tabs(df_list, sheet_list, file_name):
                        output = BytesIO()
                        output.name = file_name
                        writer = pd.ExcelWriter(output, engine = 'xlsxwriter')
                        for dataframe, sheet in zip(df_list, sheet_list):
                            dataframe.to_excel(writer, sheet_name = sheet) 
                        writer.close()
                        processed_data = output.getvalue()
                        return processed_data
                    # создадим список массивов 
                    dfs = [data_ab_dd,
                           data_ab_mer,
                           data_st_mer,
                           data_m_all,
                           data_m_neud_neusp,
                           data_m_neat_neusp,
                           data_m_usp_neusp,
                           data_m_mer,
                           data_mer,
                           Data,
                           Data_id,
                           Data_XY
                          ]
                    # создадим список названий листов
                    sheets = ['Абитуриенты (без дубликатов)',
                              'Абитуриенты (для анализа)',
                              'Студенты (для анализа)',
                              'Мониторинг (все данные)',
                              'Мониторинг (имеют неудовл)',
                              'Мониторинг (не аттестовано)',
                              'Мониторинг (успевающие)',
                              'Мониторинг (для анализа)',
                              'Выборка',
                              'Матрица данных',
                              'Матрица идентификаторов',
                              'Матрица наблюдений'
                             ]
                    # создадим кнопку для скачивания файла
                    df_xlsx = dfs_tabs(dfs, sheets, 'Исходные данные.xlsx')
                    st.download_button(label = 'Скачать файл',
                                       data = df_xlsx,
                                       file_name = 'Исходные данные.xlsx')
                    
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
