from os import listdir, getcwd

def get_instruction():
	'''
	Get a legal instruction number
	'''
    print("工作路徑: ", getcwd(), end='')
    print("""
            (0) 離開程式
            (1) 列出檔案
            (2) 列出資料夾
            (3) 顯示檔案內容
            (4) 刪除檔案
            (5) 執行檔案
            (6) 進入資料夾
            (7) 刪除資料夾
            (8) 回上層資料夾""" )
    while True:
        try: 
            ins = int(input('操作: '))
        except ValueError:
            print("Please input an integer(0~8)")
            continue
        if -1 < ins < 9:
            break
    return ins


def get_index(len, query):
	'''
	Get a legal index within given 'len'
	'''
    while True:
        try: 
            index = int(input(query))
        except ValueError:
            print("Please input an integer less than", len)
            continue
        if -1 < index < len:
            break
    return index


#def get_file_name():
#    '''
#    Keep ask a file name until get a legal one
#    '''
#    while True:
#        filename = input("Please input the file name: ")
#        if exists(filename):
#            break
#        else:
#            print("It\'s not a legal file name.")
#    return filename
#
#def get_dir():
#    '''
#    Keep ask a directory until get a legal one
#    '''
#    while True:
#        dir = input("Please input the directory: ")
#        if isdir(dir):
#            break
#        else:
#            print("The path does't exist")
#    return dir
