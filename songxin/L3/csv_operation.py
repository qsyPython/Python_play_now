import csv

class CSVOperation(object):

    def process_cvs_w_file(self, file_path, file_list):
        '''
         把数据写成csv文件
        '''
        with open(file_path, mode='a', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(file_list)
