import os

projectname = input('Введите название проекта: ')
folders = [(f'{projectname}'),['settings', 'mainapp', ['templates', [ 'mainapp', ]], 'authapp',['templates',  ['authapp',  ]]]]


def build_folders(lst):
  project = os.path.abspath(os.curdir)
  print (project)
  for i in range(len(lst)):
    if type(lst[i]) is str:
      if not os.path.exists(lst[i]):
          os.mkdir(f'{project}/'+ lst[i])
    else:
      os.chdir(f'{project}/'+ lst[i - 1])
      build_folders(lst[i])
  os.chdir('..')

build_folders(folders)