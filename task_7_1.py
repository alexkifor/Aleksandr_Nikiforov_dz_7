import os
path = r'C:/Users/User/PycharmProjects/dz_7'
main_dir = 'my_project'
second_dir = ['setting', 'mainapp', 'adminapp', 'authapp']
def create_folder(path):
    if not os.path.exists(path):
        os.mkdir(path)
full_path = os.path.join(path, main_dir)
create_folder(full_path)
for i in second_dir:
    path_second_dir = os.path.join(full_path, i)
    create_folder(path_second_dir)
