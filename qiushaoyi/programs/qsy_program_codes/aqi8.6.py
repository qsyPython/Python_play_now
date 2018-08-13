'''
	作者：邱少一
	日期：2017/11/21
	功能：aqi计算 ：pandas 数据处理和清洗数据，   数据可视化matplotlib
	版本：1.0
'''

import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def main():
    aqi_data = pd.read_csv('china_qsy_aqi.csv')
    print('基本信息：', aqi_data.info())
    print('数据概览：', aqi_data.head())

    # 数据清洗只保留aqi大于0的数据 condition：aqi_data['AQI']>0
    clean_aqi_data = aqi_data[aqi_data['AQI'] > 0]
    # 基本统计
    print('AQI最大值：', clean_aqi_data['AQI'].max())
    print('AQI最小值：', clean_aqi_data['AQI'].min())
    print('AQI均值：', clean_aqi_data['AQI'].mean())

    # top 50
    top50_cities = clean_aqi_data.sort_values(by=['AQI']).head(50)
    top50_cities.plot(kind='bar', x='City', y='AQI', title='空气质量最好的50个城市',
                      figsize=(20, 10))  # kind统计的类型（bar为柱状图),figsize图像尺寸
    plt.savefig('top50_aqi_bar.png')
    plt.show()


if __name__ == '__main__':
    main()
