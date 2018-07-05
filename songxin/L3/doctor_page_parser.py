import pandas as pd


class DoctorPageParser(object):

    def doctor_page_parser(self):
        all_doctor_url = set()
        # df = pd.read_csv('D:\PythonProject\gitClone\Python_play_now\songxin\L3\/all_doctor_csv', error_bad_lines=False,sep=',')
        # print('用read_table读取csv文件：', df)
        # for d in df:
        #     all_doctor_url.add(str(d))
        # print(len(d))

        with open("all_doctor_csv", "r") as large_file:
            for line in large_file:
                arr = line.split(',')
                for a in arr:
                    all_doctor_url.add(a)
                    # print(a)
        print(len(all_doctor_url))


doctor_parser = DoctorPageParser()
doctor_parser.doctor_page_parser()