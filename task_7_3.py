import os
import shutil
path = r'C:\Users\User\PycharmProjects\dz_7\my_project'
result_dir = 'templates'
result_path = os.path.join(path, result_dir)
dev_path = []
if not os.path.exists(result_path):
    os.mkdir(result_path)
for r, d, f in os.walk(path):
    for file in f:
        if file.endswith('.html'):
            dev_path.append(os.path.join(r, file))
for path in dev_path:
    result_path_dir = os.path.join(result_path, os.path.basename(os.path.dirname(path)))
    if not os.path.exists(result_path_dir):
        os.mkdir(result_path_dir)
    result_path_dir_file = os.path.join(result_path_dir, os.path.basename(path))
    shutil.copy(path, result_path_dir_file)








