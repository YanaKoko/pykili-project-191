#тут ничего не надо делать, но она должна быть скачана, иначе не заработает
import csv, datetime

def csv_dict_reader(file_obj):#читает словарь из таблицы
    reader = csv.DictReader(file_obj, delimiter=';')
    return reader



def my_date():#приводит дату к образцу словаря
    date = datetime.datetime.now()
    day = str(date.day)
    month = date.month
    monthes = {1:'января', 2:'февраля', 3:'марта', 4:'апреля',
               5:'мая', 6:'июня',7:'июля', 8:'августа',
               9:'сентября', 10:'октября', 11:'ноября', 12:'декабря'}
    month = monthes[month]
    return day, month

def my_holy(reader, day, month):#ищет нужный праздник
    for line in reader:
        if line['day'] == day and line['month'] == month:
            holy = line['holyday']
    return holy



def congrats():
    with open('holy.csv') as f_obj:#сюда вставить название файла 
        reader = csv_dict_reader(f_obj)
        day, month = my_date()
        congrats = my_holy(reader, day, month)
    return congrats 



