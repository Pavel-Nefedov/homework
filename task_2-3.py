import os

name_project = 'my_project'
structure_project = [
   'settings',
   'mainapp',
   'authapp',
]
for_settings = [
    '__init__.py',
    'dev.py',
    'prod.py',
]
for_main_auth =[
    '__init__.py',
    'models.py',
    'views.py',
]
#создаю главную папку, название проекта
os.mkdir(name_project)

#перехожу в нее
os.chdir(name_project)

#создаю в этой папке остальные файлы
for i in structure_project:
   os.mkdir(i)

#перехожу в нужную папку по ключу, по другому не получается(
os.chdir(structure_project[0])
for file in for_settings:
    open(file, "w")
os.chdir('..')
#print("Текущая деректория:", os.getcwd())

#number_puck: ключ папки, name_puck: имя папки
#у main и auth одинаковая структура поэтому для них функцию
def main_auth(number_puck, name_puck):
    os.chdir(number_puck)
    for file in for_main_auth:
        open(file, "w")
    os.makedirs(os.path.join('templates', name_puck))
    os.chdir('templates')
    os.chdir(name_puck)
    open('base.html', "w")
    open('index.html', "w")

    #print("Текущая деректория:", os.getcwd())
    # подскажи как можно сделать не писав трижды выход из диреектории?))
    os.chdir('..')
    os.chdir('..')
    os.chdir('..')
    #print("Текущая деректория:", os.getcwd())

main_auth(structure_project[1], 'mainapp')
main_auth(structure_project[2], 'authapp')