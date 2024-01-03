from pywinauto import Application
from contextlib import redirect_stdout

#Путь до приложения

app = Application(backend='uia').start('путь до приложения')
app_window = app.window(title='Название окна приложения')

#Открытие начального меню

app_window.wait('ready', timeout=20000)
menu = app_window.child_window(best_match='Main Menu', control_type='Button').click()

#Открытие магазина плагинов

app_window.wait('ready', timeout=20000)
plug = app_window.child_window(title="Plugin store", control_type="TabItem").select()
app_window.wait('ready', timeout=40000)

with open("D:/!Script/!scripts_for_tests/New folder/3.txt", "w", encoding="utf8") as f:
    with redirect_stdout(f):
        app_window.child_window(title="Plugin store", control_type="TabItem").print_control_identifiers()
        #app.window(best_match='Dialog').print_control_identifiers()
exit = app_window.child_window(title="Exit", control_type="MenuItem").select()
