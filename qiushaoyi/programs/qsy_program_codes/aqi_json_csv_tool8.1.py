'''
	作者：邱少一
	功能：json和csv的读写处理
	日期：2017/12/12
	版本：1.0
	学习：OOP、IPO 、DOM。

'''
import json, csv, os, platform

'''
	处理json和csv
'''


def process_r_json_file(filepath):
    '''
        解码json文件
    '''
    with open(filepath, mode='r', encoding='utf-8') as f:
        result_list = json.load(f)
        # result_list.sort(key=lambda city: city['aqi'])  # 按照aqi顺序排序
        print('json文件内容：{}'.format(result_list))
        return result_list


def process_w_json_file(file_path, result_list):
    '''
        编码json文件
    '''
    with open(file_path, mode='w', encoding='utf-8') as f:
        json.dump(result_list, f, ensure_ascii=False)


def process_r_csv_file(filepath):
    '''
        解码csv文件
    '''
    with open(filepath, mode='r', encoding='utf-8', newline='') as f:
        reader = csv.reader(f)
        result_list = list(reader)
        # result_list.sort(key = lambda city:city['aqi']) # 按照aqi顺序排序
        print('csv文件内容：{}'.format(result_list))
        return result_list


def process_w_csv_file(filepath, lines_list):
    '''
        编码csv文件
        filepath:
        lines_list:每行显示的list为元素的list
    '''
    with open(filepath, mode='w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for line in lines_list:
            writer.writerow(line)


def main():
    '''
        主函数
    '''
    filepath = input('请输入文件名称: ')
    filename, file_text = os.path.splitext(filepath)
    # 区分文件格式
    if file_text == '.json':
        result_list = process_r_json_file(filepath)
        process_w_json_file('qsy.json', result_list)
    elif file_text == '.csv':
        result_list = process_r_csv_file(filepath)
        process_w_csv_file('qsy.csv', result_list)
    else:
        print('不支持当前格式')


if __name__ == '__main__':
    main()
