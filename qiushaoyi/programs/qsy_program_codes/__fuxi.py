'''
    pandas 数据处理和清洗数据
'''

import pandas as pd
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def main():
    aqi_data = pd.read_csv('china_qsy_aqi.csv')
    clean_aqi_data = aqi_data[aqi_data['AQI'] > 0]
    # 清洗数据：保留aqi大于0的数据
    print(clean_aqi_data['AQI'].max,
          clean_aqi_data['AQI'].min,
          clean_aqi_data['AQI'].mean)

    # 前50最差城市和前50最好城市
    top50_cities = clean_aqi_data.sort_values(by='AQI').head(50)
    bottom50_cities = clean_aqi_data.sort_values(by='AQI', ascending=False).head(50)
    top50_cities.plot(kind='bar', x='City', y='AQI',
                      title='空气质量最好的50个城市',
                      figsize=(20, 10))
    plt.savefig('top50_aqi_bar_hh1.png')

    bottom50_cities.plot(kind='bar', x='City', y='AQI',
                         title='空气最差的50个城市',
                         figsize=(20, 10))
    plt.savefig('top50_aqi_bar_hh2.png')
    plt.show()

    # 保存为csv文件
    top50_cities.to_csv('top50_aqi.csv', index=False)
    bottom50_cities.to_csv('bottom50_aqi.csv')


if __name__ == '__main__':
    main()
