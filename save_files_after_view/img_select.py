import shutil
import matplotlib.pyplot as plt
from PIL.Image import open
from glob import glob

INPUT_DIR = 'out_dir'
OUTPUT_DIR = 'imgs_to_upload'

all_files = glob(INPUT_DIR + '/*')

for i , each_file in enumerate(all_files):
    img = open(each_file)
    plt.figure(figsize=(3 , 3) , dpi = 250)
    plt.imshow(img)
    plt.show()

    save = input(f'Want to save img-{i}?')

    if save == 'y':
        shutil.copy(each_file , OUTPUT_DIR)

    else:
        continue

