# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
import logging
import redis
import mysql.connector
import re
import unittest

logging.basicConfig(level=logging.INFO)

"""
   获取cookie里的yunsid
   """


def get_yun_sid(browers):
    cookies = browers.get_cookies()
    for cookie_dict in cookies:
        if cookie_dict['name'] == 'yunsid':
            return cookie_dict['value']
    logging.error('>>>>>>>>>>该页面cookies中不包含yunsid，返回 ""')
    return ''


class LoginTest(unittest.TestCase):

    def setUp(self):
        config_file = open('login_config.properties', 'r', encoding='utf-8')
        r = config_file.readlines()
        logging.info('>>>>>>>>>>读取配置文件完成')
        self.config_dict = {}
        # 组装字典数据
        for s in r:
            if s.startswith('#') or s == '' or s == '\n':
                continue
            s = re.sub(r'\s+=\s+', '$equals$', s)
            tmp_str = s.split("=")
            logging.info(tmp_str)
            self.config_dict[tmp_str[0]] = tmp_str[1].replace('\n', '')
        self.redis = redis.Redis(host=self.config_dict['redis.host'],
                            password=self.config_dict['redis.password'],
                            port=self.config_dict['redis.port'])
        self.jdbc = mysql.connector.connect(host=self.config_dict['jdbc.host'],
                                       user=self.config_dict['jdbc.username'],
                                       password=self.config_dict['jdbc.password'],
                                       database=self.config_dict['jdbc.database'])
        # if self.config_dict['chrome.drive.path'].strip() != '':
        #     logging.info('>>>>>>>>>>chrome驱动路径为 {}'.format(self.config_dict['chrome.drive.path'].strip()))
        #     self.browers = webdriver.Chrome(self.config_dict['chrome.drive.path'])
        if self.config_dict['ie.drive.path'].strip() != '':
            logging.info('>>>>>>>>>>IE驱动路径为 {}'.format(self.config_dict['ie.drive.path'].strip()))
            self.browers = webdriver.Ie(self.config_dict['ie.drive.path'])
            self.browers.implicitly_wait(5)

    """执行登录操作"""

    def test_execute(self):
        browers = self.browers
        config_dict = self.config_dict
        redis = self.redis
        jdbc = self.jdbc
        browers.implicitly_wait(5)
        browers.get(config_dict['login.url'])
        browers.find_element_by_xpath(config_dict['login.page.prompt']).click()
        browers.find_element_by_id(config_dict['login.username.id']).send_keys(config_dict['login.username'])
        browers.find_element_by_id(config_dict['login.pwd.id']).send_keys(config_dict['login.pwd'])
        # 获取cookie中的sid，并获取redis中的图片验证码
        yunsid = get_yun_sid(browers)
        logging.info('>>>>>>>>>>获得yunsid:{}'.format(yunsid))
        valied_code = redis.hget((config_dict['session.prefix'] + yunsid), 'VALID_CODE')
        logging.info('>>>>>>>>>>从redis中获取图片验证码为:{}'.format(valied_code))
        browers.find_element_by_id(config_dict['login.valid.id']).send_keys(str(valied_code))
        browers.find_element_by_xpath(config_dict['login.button']).click()
        # 读取用户输入的手机号
        verify_phone = browers.find_element_by_id(config_dict['verify.phone.id']).get_attribute('value')
        logging.info('>>>>>>>>>>当前登录用户手机号码为：{}'.format(verify_phone))
        # 发送验证码
        browers.find_element_by_id(config_dict['verify.phone.sender']).click()
        logging.info('>>>>>>>>>>发送验证码中')
        verify_phone_code = ''
        i = 1
        while i < 6 and verify_phone_code == '':
            sleep(2)
            logging.info('>>>>>>>>>>当前手机验证码为空，第{}次查询数据库……'.format(i))
            cursor = jdbc.cursor()
            query_sql = str(config_dict['jdbc.query']).replace('$equals$', '=').format(verify_phone)
            cursor.execute(query_sql)
            logging.info('>>>>>>>>>>查询数据库：{}'.format(query_sql))
            jdbc_result = cursor.fetchall()
            logging.info('>>>>>>>>>>查询结果为：{}'.format(jdbc_result))
            if type(jdbc_result) == list:
                for rows in jdbc_result:
                    if rows[0] is not None:
                        verify_phone_code = rows[0]
                        break
            i += 1
        if verify_phone_code == '':
            logging.info('>>>>>>>>>>未查询到有效手机验证码，系统自动退出！！！')
            return
        logging.info('>>>>>>>>>>短信验证码为:{}'.format(verify_phone_code))
        browers.find_element_by_id(config_dict['yzm.input.id']).send_keys(verify_phone_code)
        browers.find_element_by_xpath(config_dict['yzm.button']).click()
        title = browers.title
        count = 1
        while count < 4 and title != config_dict['success.title']:
            sleep(2)
            logging.info('>>>>>>>>>>还未登录成功，当前页面为：{}，等待2秒'.format(title))
            title = browers.title
            count += 1
        if title != config_dict['success.title']:
            logging.info('>>>>>>>>>>登录失败，结束重试')
        else:
            logging.info('>>>>>>>>>>登录成功!!!')
        self.assertEqual(title, config_dict['success.title'])

    def tearDown(self):
        self.browers.quit()


if __name__ == '__main__':
    logging.info('>>>>>>>>>>开始执行测试用例')
    unittest.main()





