import os

def get_filenames_in_folder(folder_path):
    filenames = set()
    for file in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file)):
            filenames.add(file)
    return filenames
def compare_folders0(folder_path1, folder_path2):
    filenames1 = get_filenames_in_folder(folder_path1)
    filenames2 = get_filenames_in_folder(folder_path2)

    if filenames1 == filenames2:
        print("同")
    else:
        print("不同")
def compare_folders(folder_path1, folder_path2):
    filenames1 = get_filenames_in_folder(folder_path1)
    filenames2 = get_filenames_in_folder(folder_path2)

    extra_files_in_folder1 = filenames1 - filenames2
    extra_files_in_folder2 = filenames2 - filenames1

    if extra_files_in_folder1:
        print(f"文件夹1中多出来的文件: {extra_files_in_folder1}")
    if extra_files_in_folder2:
        print(f"文件夹2中多出来的文件: {extra_files_in_folder2}")
def compare_and_delete_folders(folder_path1, folder_path2):
    filenames1 = get_filenames_in_folder(folder_path1)
    filenames2 = get_filenames_in_folder(folder_path2)

    extra_files_in_folder1 = filenames1 - filenames2
    extra_files_in_folder2 = filenames2 - filenames1

    for file in extra_files_in_folder1:
        file_path = os.path.join(folder_path1, file)
        os.remove(file_path)
        print(f"删除文件夹1中多出来的文件: {file}")

    for file in extra_files_in_folder2:
        file_path = os.path.join(folder_path2, file)
        os.remove(file_path)
        print(f"删除文件夹2中多出来的文件: {file}")

if __name__ == "__main__":
    folder_path1 = "/root/build_datasets/Aerial_building/ann_dir/val"
    folder_path2 = "/root/build_datasets/Aerial_building/img_dir/val"

    # compare_folders0(folder_path1, folder_path2)
    compare_folders0(folder_path1, folder_path2)
