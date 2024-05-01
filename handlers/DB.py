import gspread, time
from datetime import datetime as dt

sa = gspread.service_account('_Key_.json') #подключение в  json файлу библиотеки
sh = sa.open("Vote_data")  #открытие таблицы с таким-то названием

user_int=['Регистрация прошла успешно📅!','Вы уже зарегистрированы','Отлично, начнем регистрацию⚡\nВведите свой номер в формате: 89271234567','Ваш номер не найден в базе данных. Попробуйте еще раз или обратитесь к администратору']
token="7001582759:AAHQ3IcSCZ96WeEvL-HRpbR2DiJC4wxhBmk"
sh1=sh.get_worksheet(0)
sh2=sh.get_worksheet(1)


def on_hold(sec: int): time.sleep(sec) # функция задержки 

def check(user_id: str)->bool: #проверка на наличие id пользователя в системе
    try:
        if sh1.find(str(user_id)) is None: return True
        else: return False
    except gspread.exceptions.APIError:
        on_hold(5)
        return check(user_id)

def get_users()->list:
    try: return sh1.get_all_values()[1:]
    except gspread.exceptions.APIError:
        on_hold(5)
        return get_users()

def get_dates()-> list:
    try: return sh2.col_values(1)[1:]
    except gspread.exceptions.APIError:
        on_hold(5)
        return get_dates()

def check_for_day(list_: list)-> bool:
    try:
        for item in list_: 
            if dt.strptime(item, "%d.%m.%Y").date()==dt.now().date():
                if dt.today().hour == 18: return True
                elif dt.today().hour == 21: return True
                else: return False
    except KeyboardInterrupt: print(f'Работа приостановлена.....')
    except Exception as e: print(f'ошибка вида: {e}')



def register_user(user_data: list): #регистрация пользователя
    try: sh1.update_cell(len(sh1.get_values())+1, 1, user_data[0]) #определяем место ввода(последняя свободная, столбец, значение)
    except gspread.exceptions.APIError:
        on_hold(30)
        return register_user(user_data)


