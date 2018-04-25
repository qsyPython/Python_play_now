from aip import AipSpeech
import pygame
import time

""" 你的 APPID AK SK  个人开发key，请勿乱用"""
APP_ID = '6504962'
API_KEY = 'ogCRv6RoBvgMYak5Fxa53njg'
SECRET_KEY = 'Aw1DWipvMGZgIGSkUxG2DEC8BFGQBgLl'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

def playMusic():
    pygame.mixer.init()
    print("开始朗读")
    pygame.time.delay(1000)
    track = pygame.mixer.music.load('auido.mp3')
    pygame.mixer.music.play()
    time.sleep(10)
    pygame.mixer.music.stop()


# 定义语音合成
result  = client.synthesis('长亭外,古道边,芳草碧连天。', 'zh', 1, {
    'vol': 5,
})
# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('auido.mp3', 'wb') as f:
        f.write(result)

playMusic()