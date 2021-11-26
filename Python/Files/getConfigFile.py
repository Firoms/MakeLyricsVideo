import configparser
from time import strftime


class ConfigManager():
    def __init__(self) -> None:
        self.config = configparser.ConfigParser()

    def makeDefaultConfigFile(self) -> None:
        self.config['System'] = {}
        self.config['System']['Version'] = '0.8'
        self.config['System']['update'] = strftime('%Y-%m-%d %H:%M:%S')
        self.config['System']['Maker'] = 'Lyrics WFS'

        defaultWritings = {
            'PreFace - Title & Singer': ['GodoB.ttf', '60', '40', '40', '#5d7530'],
            'PreFace - Maker': ['GodoM.ttf', '60', '2200', '40', '#123152'],
            'TitlePage - Title': ['GodoB.ttf', '150', '170', '400', 'Black'],
            'TitlePage - Singer': ['GodoM.ttf', '100', '1300', '800', '#575759'],
            'LyricsPage - CurLyrics1': ['godoMaum.ttf', '180', '200', '370', 'Black'],
            'LyricsPage - CurLyrics2': ['godoMaum.ttf', '180', '200', '670', 'Black'],
            'LyricsPage - NextLyrics': ['godoMaum.ttf', '180', '200', '1130', '#575759'],
            'LastPage - Thanks For': ['godoMaum.ttf', '500', '510', '300', 'Black'],
            'LastPage - Listening': ['godoMaum.ttf', '500', '670', '650', 'Black']
        }

        for key, val in defaultWritings.items():
            self.config[f'{key}'] = {}
            self.config[f'{key}']['Font'] = val[0]
            self.config[f'{key}']['FontSize'] = val[1]
            self.config[f'{key}']['PosX'] = val[2]
            self.config[f'{key}']['PosY'] = val[3]
            self.config[f'{key}']['Color'] = val[4]

        with open('config.ini', 'w', encoding='cp949') as configfile:
            self.config.write(configfile)

    def readConfigFile(self) -> None:
        pass


if __name__ == "__main__":
    CM = ConfigManager()
    CM.makeDefaultConfigFile()

'''
import configparser
from time import strftime


def config_generator():
    # 설정파일 만들기
    config = configparser.ConfigParser()

    # 설정파일 오브젝트 만들기
    config['system'] = {}
    config['system']['title'] = 'Neural Networks'
    config['system']['version'] = '1.2.42'
    config['system']['update'] = strftime('%Y-%m-%d %H:%M:%S')

    config['video'] = {}
    config['video']['width'] = '640'
    config['video']['height'] = '480'
    config['video']['type'] = 'avi'

    # 설정파일 저장
    with open('config.ini', 'w', encoding='utf-8') as configfile:
        config.write(configfile)


def config_read():
    
    # 설정파일 읽기
    config = configparser.ConfigParser()    
    config.read('config.ini', encoding='utf-8') 

    # 설정파일의 색션 확인
    # config.sections())
    ver = config['system']['version']
    title = config['system']['title']
    print(title, ver)

config_generator()
config_read()
'''
