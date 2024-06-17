# 中文
import os
import sys
from tqdm import tqdm
os.chdir(r'path')  # 
files = os.listdir('./')
# print('files', files)
count = 0
with tqdm(total=files.__len__(), desc="Processing") as pbar:
    for fileName in files:
        portion = os.path.splitext(fileName)
        if portion[1] == ".tif":  # gai
            newName = portion[0] + ".png"  # gai
            os.rename(fileName, newName)
        count += 1
        pbar.update(1)
print("Done!")
