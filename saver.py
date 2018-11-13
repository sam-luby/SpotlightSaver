from pathlib import Path
import shutil
import os
from PIL import Image

"""Program to sort Windows10 Spotlight pics"""


def delete_file(file):
    os.remove(file)


def copy_files(src_folder, dst_folder):
    if not os.path.isdir(dst_folder):       # if folder doesnt exist, create
        os.mkdir(dst_folder)

    files = os.listdir(path)                # list files in directory

    for file in files:                      # get absolute path+name of each file, copy to destination folder
        file_name = os.path.join(src_folder, file)
        new_file_name = os.path.join(dst_folder, file)
        if os.path.isfile(file_name):
            shutil.copy(file_name, new_file_name)


def rename_files(folder):
    i = 0
    for file in os.listdir(folder):         # rename each picture in folder
        old_file_name = os.path.join(folder, file)
        file_name = "Pic_" + str(i) + ".png"
        new_file_name = os.path.join(folder, file_name)
        if not os.path.exists(new_file_name):
            os.rename(old_file_name, new_file_name)
            i = i + 1


def move_files(src_folder, dst_folder):
    if not os.path.isdir(dst_folder):
        os.mkdir(dst_folder)
    for file in os.listdir(src_folder):
        file_name = os.path.join(src_folder, file)
        extension = os.path.splitext(file)[1]
        if extension == ".png":
            final_name = final_path + file
            shutil.move(file_name, final_name)


def remove_icons(folder):
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)

        # try/except block to catch OS error for non png files
        try:
            img = Image.open(file_path)
            width, height = img.size
            if width != 1920 or height != 1080:
                img.close()
                delete_file(file_path)
        except OSError:
            delete_file(file_path)
            print("Not a .png file")




homepath = str(Path.home())
path = homepath + "/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets"
temp_path = homepath + "\\Downloads\\tmp\\"


copy_files(path, temp_path)

newfiles = os.listdir(temp_path)
rename_files(temp_path)

final_path = homepath + "\\Downloads\\final\\"
move_files(temp_path, final_path)
remove_icons(final_path)



# TODO Merge copy and move files functions
# TODO Delete Duplicates