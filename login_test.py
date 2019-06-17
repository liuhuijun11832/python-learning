# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep

config_file = open('login_config.properties', 'r', encoding='utf-8')
r = config_file.readlines()
print(type(r))
config_dict = {}
s1 = r[0].split('=')

# 组装字典数据
for s in r:
    if s.startswith('#'):
        continue
    tmp_str = s.split('=')
    config_dict[tmp_str[0]] = tmp_str[1].replace('\n', '')

print(config_dict['ie_drive_path'])
print(type(config_dict))
print(config_dict)
if config_dict['chrome_drive_path'].strip() != '':
    print(config_dict['chrome_drive_path'], end='')
    browers = webdriver.Chrome((config_dict['chrome_drive_path']))
