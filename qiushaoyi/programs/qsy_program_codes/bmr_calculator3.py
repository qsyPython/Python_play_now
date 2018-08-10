'''
	作者：少一
	版本：1.0
	日期：2017/11/11
	功能：
	3.0 增加功能：用户可以在一行输入所有信息，带单位的信息输出
    4.0 增加功能：可能出问题的代码，进行try的异常处理操作
'''


def main():
    '''
        主函数
    '''
    y_or_n = input('是否退出 基础代谢率 程序(y/n)?')

    while y_or_n != 'y':
        print('请输入一下信息，用空格分割')
        input_str = input('性别(男或女或未知) 体重(kg) 身高(cm) 年龄：\n')
        str_list = input_str.split(' ')

        try:
            gender = str_list[0]
            weight = float(str_list[1])
            height = float(str_list[2])
            age = int(str_list[-1])

            if gender == '男':
                bmr = (13.7 * weight) + (5.0 * height) - (6.8 * age) + 66
            elif gender == '女':
                bmr = (9.6 * weight) + (1.8 * height) - (4.7 * age) + 655
            else:
                bmr = -1

            if bmr != -1:
                print('您的性别：%s, 体重：%.2fkg, 身高：%.2fcm ,年龄：%d岁 \n 您的基础代谢率：%s' % (gender, weight, height, age, bmr))
            else:
                print('暂不支持该性别')

        except ValueError:
            print('请输入正确信息')
        except IndexError:
            print('输入信息过少')
        except:
            print('程序异常!')

        # 退出循环
        y_or_n = 'y'


if __name__ == '__main__':
    main()
