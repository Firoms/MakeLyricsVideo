import configparser
from time import strftime


class ConfigManager():
    def __init__(self) -> None:
        self.config = configparser.ConfigParser()

    def makeDefaultConfigFile(self) -> None:
        self.config['System'] = {}
        self.config['System']['Version'] = '0.8'
        self.config['System']['update'] = strftime('%Y-%m-%d %H:%M:%S')

        # self.config['Writing'] = {}
        # self.config['Writing']['PreFace'] = {}
        # self.config['Writing']['PreFace']['Title & Singer'] = {}
        # self.config['Writing']['PreFace']['Maker'] = {}
        # self.config['Writing']['TitlePage'] = {}
        # self.config['Writing']['TitlePage']['Title'] = {}
        # self.config['Writing']['TitlePage']['Title']['FontName'] = '1'
        # self.config['Writing']['TitlePage']['Title']['FontSize'] = '1'
        # self.config['Writing']['TitlePage']['Title']['PosX'] = '1'
        # self.config['Writing']['TitlePage']['Title']['PosY'] = '1'
        # self.config['Writing']['TitlePage']['Title']['Color'] = '1'
        # self.config['Writing']['TitlePage']['Singer'] = {}
        # self.config['Writing']['LyricsPage'] = {}
        # self.config['Writing']['LyricsPage']['CurLyrics'] = {}
        # self.config['Writing']['LyricsPage']['NextLyrics'] = {}
        # self.config['Writing']['LastPage'] = {}
        # self.config['Writing']['LastPage']['Thanks For'] = {}
        # self.config['Writing']['LastPage']['Listening'] = {}

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
    version_read(config)

def version_read(config):

    ver = config['system']['version']
    title = config['system']['title']
    print(title,ver)

config_generator()
config_read()
'''
