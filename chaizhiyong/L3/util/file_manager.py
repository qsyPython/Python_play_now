
import csv
class fileManager(object):

    def __init__(self):
        pass

    #按行写入 w_mode 写入模式
    def write_file_list(self,filePath,file_list,w_mode):
        try:
            with open(filePath, mode=w_mode, encoding='utf-8', newline='') as csvFile:
                writer = csv.writer(csvFile)
                for line in file_list:
                    writer.writerow(line)
        except Exception as e:
            return False
        else:
            #csvFile.close()
            return True
    # 按列读取
    def read_file_column_list(self,filePath,rowIndex):

        try:
            with open(filePath, 'r') as csvFile:
                reader = csv.reader(csvFile)
                column = [row[rowIndex] for row in reader]
        except Exception as e:
            print(Exception,':',e)
            return None
        else:
            #csvFile.close()
            return column

    # 按列读取
    def read_file_all_list(self,filePath):
        reader_list = []
        try:
            with open(filePath, 'r') as csvFile:
                reader = csv.reader(csvFile)
                for line in reader:
                    reader_list.append(line)
        except Exception as e:
            print(Exception,':',e)
            return None
        else:
            csvFile.close()
            return reader_list