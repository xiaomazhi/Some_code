import os
import random
import shutil
from tqdm import tqdm
data_path = "/root/mms/yolov10/data/VOCdevkit/VOC2007/JPEGImages"
save_path = "/root/mms/yolov10/data/VOCdevkit/VOC2007/images"
# path to destination folders
train_folder = os.path.join(save_path, 'train')
val_folder = os.path.join(save_path, 'val')
# test_folder = os.path.join(save_path, 'test')

# Define a list of image extensions
image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.tif', '.txt', '.xml']
imgs_list = []
# Create a list of image filenames in 'data_path'
imgs_list = [filename for filename in os.listdir(data_path) if os.path.splitext(filename)[-1] in image_extensions]
imgs_list.sort()
# Sets the random seed
random.seed(1)
#
# # Shuffle the list of image filenames
random.shuffle(imgs_list)

# determine the number of images for each set
train_size = int(len(imgs_list) * 0.9)

val_size = int(len(imgs_list) * 0.1)
# test_size = int(len(imgs_list) * 0)

# Create destination folders if they don't exist
for folder_path in [train_folder, val_folder]:#, test_folder
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Copy image files to destination folders
for i, f in tqdm(enumerate(imgs_list), desc="Processing images"):
# for i, f in enumerate(imgs_list):
    if i < train_size:
        dest_folder = train_folder
    elif i < train_size + val_size:
        dest_folder = val_folder
    # else:
    #     dest_folder = test_folder
    shutil.copy(os.path.join(data_path, f), os.path.join(dest_folder, f))


print('Done!')
