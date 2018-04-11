# coding:gbk
# ------------------------------------------------
#   python�ն���ʾ��ɫ�ַ��࣬���Ե��ò�ͬ�ķ���
# ѡ��ͬ����ɫ.ʹ�÷�����ʾ������ͺ���������.
# ------------------------------------------------
#
# ��ʾ��ʽ: \033[��ʾ��ʽ;ǰ��ɫ;����ɫm
# ------------------------------------------------
# ��ʾ��ʽ             ˵��
#   0                 �ն�Ĭ������
#   1                 ������ʾ
#   4                 ʹ���»���
#   5                 ��˸
#   7                 ������ʾ
#   8                 ���ɼ�
#   22                �Ǵ���
#   24                ���»���
#   25                ����˸
#
#   ǰ��ɫ             ����ɫ            ��ɫ
#     30                40              ��ɫ
#     31                41              ��ɫ
#     32                42              ��ɫ
#     33                43              �Sɫ
#     34                44              ��ɫ
#     35                45              �Ϻ�ɫ
#     36                46              ����ɫ
#     37                47              ��ɫ
# ------------------------------------------------
class Colored(object):
    # ��ʾ��ʽ: \033[��ʾ��ʽ;ǰ��ɫ;����ɫm
    # ֻдһ���ֶα�ʾǰ��ɫ,����ɫĬ��
    RED = '\033[31m'  # ��ɫ
    GREEN = '\033[32m'  # ��ɫ
    YELLOW = '\033[33m'  # ��ɫ
    BLUE = '\033[34m'  # ��ɫ
    FUCHSIA = '\033[35m'  # �Ϻ�ɫ
    CYAN = '\033[36m'  # ����ɫ
    WHITE = '\033[37m'  # ��ɫ
    BLACK = '\033[30m'  # ��ɫ

    #: no color
    RESET = '\033[0m'  # �ն�Ĭ����ɫ

    def color_str(self, color, s):
        return '{}{}{}'.format(
            getattr(self, color),
            s,
            self.RESET
        )

    def red(self, s):
        return self.color_str('RED', s)

    def green(self, s):
        return self.color_str('GREEN', s)

    def yellow(self, s):
        return self.color_str('YELLOW', s)

    def blue(self, s):
        return self.color_str('BLUE', s)

    def fuchsia(self, s):
        return self.color_str('FUCHSIA', s)

    def cyan(self, s):
        return self.color_str('CYAN', s)

    def white(self, s):
        return self.color_str('WHITE', s)