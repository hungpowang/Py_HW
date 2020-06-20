from os import listdir, getcwd, system, remove, chdir, rmdir
from os.path import isfile, isdir, exists, dirname
from src.my_getter import get_instruction, get_index

ins = get_instruction()

while ins != 0 :
    system('cls')
    files = listdir('./')
    file_count = 0
    dir_count = 0
    l_file = []
    l_dir = []
    for f in files:
        if isfile(f):
            l_file.append(f)
            file_count += 1
        elif isdir(f):
            l_dir.append(f)
            dir_count += 1

    if ins == 1:
        for i, f in enumerate(l_file):
            print(i, f)
    elif ins == 2:
        for i, d in enumerate(l_dir):
            print(i, d)
    elif ins == 3:
        for i, f in enumerate(l_file):
            print(i, f)
        index = get_index(len(l_file), '請輸入檔案索引：')

        with open(l_file[index], encoding='utf-8') as f:
            print('================檔案開始================')
            print(f.read())
            print('================檔案結束================')
    elif ins == 4:
        for i, f in enumerate(l_file):
            print(i, f)
        index = get_index(len(l_file), '請輸入檔案索引：')
        remove(l_file[index])
    elif ins == 5:
        for i, f in enumerate(l_file):
            print(i, f)
        index = get_index(len(l_file), '請輸入檔案索引：')
        system(l_file[index])
    elif ins == 6:
        for i, d in enumerate(l_dir):
            print(i, d)
        index = get_index(len(l_dir), '請輸入資料夾索引：')
        current_dir = getcwd()
        dir = l_dir[index]
        dir = current_dir + '\\' + dir
        print(dir)
        chdir(dir)
    elif ins == 7:
        for i, d in enumerate(l_dir):
            print(i, d)
        index = get_index(len(l_dir), '請輸入資料夾索引：')
        current_dir = getcwd()
        dir = l_dir[index]
        print('Delete :', dir)
        dir = current_dir + '\\' + dir
        rmdir(dir)
    elif ins == 8:
        chdir(dirname(getcwd()))

    # get the next instruction
    ins = get_instruction()