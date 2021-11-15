import configparser

class ConfigManager():
    def __init__(self) -> None:
        self.config = configparser.ConfigParser()
        
    def makeDefaultConfigFile(self) -> None:
        pass

    def readConfigFile(self) -> None:
        pass


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