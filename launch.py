

import pytest
from airtest.core.api import *

import os
from airtest.utils.logger import get_logger
from airtest.utils.logger import logging
from readme.ReadYaml import GetYamlData
from page import *
'''yaml_file=os.path.dirname(os.path.abspath(__file__))
config_file=os.path.join(yaml_file,'config/device.yaml')
if not os.path.isfile(config_file):
    raise FileNotFoundError('config/device.yaml not found')'''
"""data=GetYamlData('config/device.yaml').get_data()
# 设置设备连接
IPADD=data['Android']['AndroidIP']
deviceName=data['Android']['deviceName']
appPackages=data['Android']['appPackage']"""

class APP:
    #@pytest.fixture(scope='session', autouse=True)
    def start_app(self):
        try:
            connect_device(f"Android://{GetYamlData.get_android_ip('')}/{GetYamlData.get_device_name('')}")
            start_app(GetYamlData.get_app_package(''))
            logger = get_logger('airtest')
            logger.setLevel(logging.INFO)
        except:
            logging.info('连接设备失败')

        return MainPage


# 进行其他操作
    def stop_app(self):
        try:
            time.sleep(15)
            stop_app(GetYamlData.get_app_package(''))
        except:
            logging.info('停止app失败')
