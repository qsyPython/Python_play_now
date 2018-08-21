'''
	作者：邱少一
	功能：网络爬虫：============= csv结构化数据分析工具:pandas：成绩、股票分析，数据清洗功能
	日期：2017/12/12
	版本：1.0
	学习：Pandas 的数据结构是：Series，类似于excel的 单维或多维数据

'''
import pandas as pd


def main():
    '''
        主函数
    '''
    # _data10_series = pd.Series(range(10))
    # print(_data10_series,_data10_series.index,_data10_series.values,
    # _data10_series.head(3),_data10_series.tail())

    aqi_data = pd.read_csv('china_qsy_aqi.csv')
    print('基本信息：\n', aqi_data.info())
    print('数据预览：\n', aqi_data.head())

    # 读取单列数据或多列数据
    print('以aqi的单列:\n', aqi_data['AQI'],
          '以aqi和city的多列:\n', aqi_data[['AQI', 'City']])

    # 基本统计
    print('AQI最大值', aqi_data['AQI'].max(),
          'AQI最小值', aqi_data['AQI'].min(),
          'AQI均值', aqi_data['AQI'].mean())

    # AQI最好的top10
    top10_cities = aqi_data.sort_values(by=['AQI']).head(10)
    bottom10_cities = aqi_data.sort_values(by=['AQI'], ascending=False).head(10)
    print('\n空气质量最好的10个城市：\n', top10_cities, '\n空气质量最差的10个城市：\n', bottom10_cities)

    # 保存csv文件
    top10_cities.to_csv('top10_aqi.csv', index=False)
    bottom10_cities.to_csv('bottom10_aqi.csv', index=False)


if __name__ == '__main__':
    main()
