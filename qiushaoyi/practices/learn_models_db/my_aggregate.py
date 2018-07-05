'''
测试db文件的聚合功能：使用时，先引入 GroupConcat 这个类。
我们想把 level, info 一样的 聚到到一起，按时间和发生次数倒序排列，并含有每次日志发生的时间。

ErrorLogModel.objects.values('level', 'info').annotate(
    count=Count(1), time=GroupConcat('time', ordering='time DESC', separator=' | ')
).order_by('-time', '-count')
'''
from django.db.models import Aggregate,CharField

class GroupConcat(Aggregate):
    function = 'GROUP_CONCAT'
    template = '%(function)s(%(distinct)s%(expressions)s%(ordering)s%(separator)s)'
    def __init__(self,expression,distinct=False, ordering=None, separator=',', **extra):
        super(GroupConcat,self).__init__(
            expression,
            distinct='DISTINCT ' if distinct else '',
            ordering=' ORDER BY %s' % ordering if ordering is not None else '',
            separator=' SEPARATOR "%s"' % separator,
            output_field=CharField(),
            **extra
        )
