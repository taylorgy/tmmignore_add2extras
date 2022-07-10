# python 3.8.3
# coding=utf-8

import os
import re
import sys

list_tmmignFolderKeys = ['sp','extra','bonus','mv','bd','pv','menu','preview','other','creditless','映像特典','次回予告']
list_videoSuffixes = ['mkv','avi','mp4','rmvb']

def main():
    if(len(sys.argv)==1):
        dir_root = os.getcwd()
    elif(len(sys.argv)==2):
        dir_root = sys.argv[1]
    else:
        print("Syntax Error! Please refer to README.md for help.")
        return False
    # print(dir_root)

    if not os.path.exists(dir_root):
        print("Please input a valid path!")
        return False
    else:
        # print(dir_root)
        print("\nWelcome to tmmignore assistance!\n")
        list_tmmignList = []
        list_tmmignList_new = []

        if os.path.exists("tmmignoreList.txt"):
            print("tmmignoreList.txt loaded.\n")
            with open("tmmignoreList.txt", 'r') as f:
                list_tmmignList = f.readlines()
                list_tmmignList = [ l[:-1] for l in list_tmmignList ]
        # print(list_tmmignList)

        g = os.walk(dir_root)
        for path,list_dir,_ in g:
            for dir in list_dir:
                currPath = os.path.join(path,dir)
                if currPath in list_tmmignList:
                    # print(currPath+" is already in the list.")
                    break
                flag_folderChecked = False
                for key in list_tmmignFolderKeys:
                    if flag_folderChecked:
                        break
                    if re.search(key, dir.lower()):
                        # print(currPath)
                        for file in os.listdir(currPath):
                            if flag_folderChecked:
                                break
                            if re.match(".tmmignore", file):
                                flag_folderChecked = True
                                list_tmmignList.append(currPath)
                                # print(currPath+" is already in the list.")
                                break
                            for suf in list_videoSuffixes:
                                if file.lower().endswith(suf):
                                    flag_folderChecked = True
                                    with open(os.path.join(currPath,".tmmignore"), 'w'):
                                        None
                                    list_tmmignList_new.append(currPath)
                                    list_tmmignList.append(currPath)
                                    print(currPath+" is added to the list.")
                                    break

        # print(list_tmmignList)
        # print(list_tmmignList_new)
        with open("tmmignoreList.txt", 'w') as f:
            # f.writelines(list_tmmignList)
            f.writelines([l+'\n' for l in list_tmmignList])
            # f.write('\n'.join(list_tmmignList))
        print("\nTmmignore list saved to tmmignoreList.txt.")
        print("Please keep this file as log (recommended).\n")
        if list_tmmignList_new:
            with open("tmmignoreList_new.txt", 'w') as f:
                f.writelines([l+'\n' for l in list_tmmignList_new])
            print("New folder(s) added to tmmignore list.")
            print("Check tmmignoreList_new.txt for details.\n")

        # print("Finish!")
        return True


if __name__ == "__main__":
    main()
