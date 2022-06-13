import os
import random
path = r'C:/Users/User/PycharmProjects/dz_7'
folder = 'some data'
path_folder = os.path.join(path, folder)
if not os.path.exists(path_folder):
    os.mkdir(path_folder)
latters = [chr(cod) for cod in range(ord('a'), ord('z') + 1)]
for _ in range(10 ** 3):
    f_name = ''.join(random.sample(latters, random.randint(3, 6)))
    f_content = bytes(random.randint(0, 10 ** 5))
    with open(os.path.join(path_folder, f'{f_name}.bin'), 'wb') as f:
        f.write(f_content)
