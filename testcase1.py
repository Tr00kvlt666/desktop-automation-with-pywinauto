from pywinauto import Application
from contextlib import redirect_stdout
from pywinauto import keyboard

#Открытие приложения

app = Application(backend='uia').start('путь до приложения')
app_window = app.window(title='название главного окна приложения')

#Открытие начального меню

app_window.wait('ready', timeout=20000)
menu = app_window.child_window(best_match='Main Menu', control_type='Button').click()

#Открытие магазина плагинов

app_window.wait('ready', timeout=20000)
plug = app_window.child_window(title="Plugin store", control_type="TabItem").select()
app_window.wait('ready', timeout=40000)

#Открытие магазина плагинов

rigis = app_window.child_window(title="РИГИС", control_type="TabItem").select()
del_1 = app_window.child_window(best_match="Delete", control_type="TabItem").select()
