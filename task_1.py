import os

name_project = 'my_project'
structure_project = [
   'settings',
   'mainapp',
   'adminapp',
   'authapp',
]
#создаю главную папку, название проекта
if not os.path.exists(name_project):
   os.mkdir(name_project)

#перехожу в нее
os.chdir(name_project)

#создаю в этой папке остальные файлы
for i in structure_project:
   os.mkdir(i)


