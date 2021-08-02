import os
import shutil
import time
def main ():
    deletedFolders = 0
    deletedFiles = 0
    path = "C:/Users/Vaishnavi/Desktop/python projects/REMOVE FOLDER/"
    days=30
    seconds= time.time() -(days *24 *60 *60)
    if os.path.exists(path):
        for root_folder, folders, files in os.walk(path):
            if seconds>= get_file_or_folder(root_folder):
                remove_folder(root_folder)
                deletedFolders+=1
                break
            else:
                for folder in folders:
                    folder_path= os.path.join(root_folder, folder)
                    if seconds> get_file_or_folder(folder_path):
                        remove_folder(folder_path)
                        deletedFolders+=1

        for 