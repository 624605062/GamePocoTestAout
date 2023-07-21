import os
import yaml


class GetYamlData:
    #使用OS模块查找文件绝对路径
    def __init__(self,yaml_filepath):
        self.yaml_filepath=os.path.dirname(os.path.abspath(__file__))+'/'+yaml_filepath
    def get_data(self):
        try:
            with open(self.yaml_filepath,'r',encoding='utf-8') as f:
                data=yaml.safe_load(f)
                return data
        except FileExistsError as e:
            print(e)
    def get_value(self,key,value):
        data=self.get_data()
        return data[key][value]
    def get_android_ip(self):
        data=GetYamlData('../config/device.yaml').get_data()
        return data['Android1']['AndroidIP']
    def get_device_name(self):
        data=GetYamlData('../config/device.yaml').get_data()
        return data['Android1']['deviceName']
    def get_app_package(self):
       data=GetYamlData('../config/device.yaml').get_data()
       return data['Android1']['appPackage']
    def get_app_activity(self):
        data=GetYamlData('../config/device.yaml').get_data()
        return data['Android1']['appActivity']

