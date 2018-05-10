import re

class phoneOp(object):
    def __init__(self, phoneNumber):
        self.phoneNumber = phoneNumber;

    def __str__(self):
        return self.phoneNumber

    def checkPhoneNumber(self,number):
        p2 = re.compile('^0\d{2,3}\d{7,8}$|^1[358]\d{9}$|^147\d{8}')
        phonematch = p2.match(number)
        if phonematch:
            return True
        else:
            return False

    # 判断电话号码属于那个运营商
    def number_operator(self,number):
        while True:
            CN_mobile = [134, 135, 136, 137, 138, 139, 150, 151, 152, 157, 158, 159, 182, 183, 184, 187, 188, 147, 178,
                         1705]
            CN_union = [130, 131, 132, 155, 156, 185, 186, 145, 176, 1709]
            CN_dianxin = [133, 153, 180, 181, 189, 177, 1700]
            first_three = int(number[0:3])
            first_four = int(number[0:4])
            if len(number) == 11:
                if first_three in CN_mobile or first_four in CN_mobile:
                    print('这个号码是中国移动的!')
                    break
                elif first_three in CN_union or first_four in CN_union:
                    print('这个号码是中国联通的!')
                    break
                elif first_three in CN_dianxin or first_four in CN_dianxin:
                    print('这个号码是中国电信的!')
                    break
                else:
                    print('这个号码不知道是那个运营商!')
                    break
            else:
                print('请输入正确的电话号码')
                break


#现代人的特征
class person(object):
    __author__ = "柴志勇"  #作者
    #__slots__ = ('name', 'phoneNumber') #唯一性
    def __init__(self,name,phoneNumber):#构造函数
        self.__name = name
        self.__phoneNumber = phoneNumber

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name = value

    @property
    def phoneNumber(self):
        return self.__phoneNumber

    @phoneNumber.setter
    def phoneNumber(self, value):
        self.__phoneNumber = value;
