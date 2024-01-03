from pywinauto import Application
from contextlib import redirect_stdout
from pywinauto import keyboard

#Открытие приложения

app = Application(backend='uia').start('путь до лаунчера приложения')
app_window = app.window(title='название главного окна приложения')

#Открытие начального меню

app_window.wait('ready', timeout=20000)
menu = app_window.child_window(best_match='Main Menu', control_type='Button').click()

#Открытие магазина плагинов

app_window.wait('ready', timeout=20000)
plug = app_window.child_window(title="Plugin store", control_type="TabItem").select()

#Написать в поиск плагин
app_window.wait('ready', timeout=40000)
search = app_window.child_window(auto_id="2429728", control_type="Edit").click()


#Закрытие программы
exit = app_window.child_window(title="Exit", control_type="MenuItem").select()
