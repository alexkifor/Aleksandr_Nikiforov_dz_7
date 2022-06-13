import os
import pprint
folder = 'some data'
path = r'C:\Users\User\PycharmProjects\dz_7'
folder_path = os.path.join(path, folder)
size_files = []
out_dict = {}
for r, d, f in os.walk(folder_path):
    for file in f:
        size = os.stat(os.path.join(r, file)).st_size
        size_files.append(size)
out_dict.setdefault(10, (len([size for size in size_files if 0 <= size <= 10])))
i = 10
while i <= max(size_files):
    count = len([size for size in size_files if i < size <= 10*i])
    out_dict.setdefault(10*i, count)
    i *= 10
pretty = pprint.PrettyPrinter(width=30)
pretty.pprint(out_dict)
