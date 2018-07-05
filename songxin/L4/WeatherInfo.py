class WeatherInfo(object):

    def __init__(self):
        self.city_name = ""
        self.date = ""
        self.weather_condition = ""
        self.temperature = ""
        self.wind = ""
        self.pm = ""
        self.pic_url = ""

    def set_city_name(self, city_name):
        self.city_name = city_name

    def get_city_name(self):
        return self.city_name

    def set_date(self, date):
        self.date = date

    def get_date(self):
        return self.date

    def set_weather_condition(self, weather_condition):
        self.weather_condition = weather_condition

    def get_weather_condition(self):
        return self.weather_condition

    def set_temperature(self, temperature):
        self.temperature = temperature

    def get_temperature(self):
        return self.temperature

    def set_wind(self, wind):
        self.wind = wind

    def get_wind(self):
        return self.wind

    def set_pm(self, pm):
        self.pm = pm

    def get_pm(self):
        return self.pm

    def set_pic_url(self, pic_url):
        self.pic_url = pic_url

    def get_pic_url(self):
        return self.pic_url