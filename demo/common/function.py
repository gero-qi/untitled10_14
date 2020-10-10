import configparser
import os


def project_path():
    return os.path.split(os.path.realpath(__file__))[0].split('c')[0]

def config_url():
    config = configparser.ConfigParser()
    config.read(project_path() + "config.ini")
    return config.get('testUrl', 'url')

if __name__ == '__main__':
    print("项目的路径为："+project_path())
    print("测试地址为：" + config_url())
