import configparser
import os

import requests


class OCR_Config():

    def __init__(self):
        self.config = configparser.ConfigParser()
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.config_file_path = os.path.join(dir_path, 'config.ini')
        self.config.read(self.config_file_path)

    @staticmethod
    def init_config():
        config = configparser.ConfigParser()
        config['DEFAULT'] = {
            'request_raw_url': 'https://aip.baidubce.com/rest/2.0/ocr/v1/handwriting',
            'access_token': '',
            'headers': 'application/x-www-form-urlencoded',
        }

        config['CONNECT'] = {
            'host': ''
        }

        with open('config.ini', 'w') as configfile:
            config.write(configfile)

    def get_req_config(self):
        request_raw_url = self.config['DEFAULT']['request_raw_url']
        access_token = self.config['DEFAULT']['access_token']
        request_url = request_raw_url + "?access_token=" + access_token
        headers = {'content-type': self.config['DEFAULT']['headers']}

        return request_url, headers

    def get_host_config(self):
        host = self.config['CONNECT']['host']

        return host

    def renew_config(self):
        host = self.get_host_config()
        response = requests.get(host)
        if response:
            res = response.json().get("access_token")
            self.config['DEFAULT']['access_token'] = res

        with open(self.config_file_path, 'w') as configfile:
            self.config.write(configfile)


# ocr1 = OCR_Config()
# ocr1.get_req_config()
