import configparser

class OCR_Config():

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')

    @staticmethod
    def init_config():
        config = configparser.ConfigParser()
        config['DEFAULT'] = {
            'request_url': 'https://aip.baidubce.com/rest/2.0/ocr/v1/handwriting',
            'request_raw_url': '',
            'access_token': '',
            'headers': 'application/x-www-form-urlencoded'
        }

        with open('config.ini', 'w') as configfile:
            config.write(configfile)

    def get_config(self):
        config = configparser.ConfigParser()
        config.read('config.ini')

        request_raw_url = config['DEFAULT']['request_raw_url']
        access_token = config['DEFAULT']['access_token']
        request_url = request_raw_url + "?access_token=" + access_token
        headers = {'content-type': config['DEFAULT']['headers']}

        print(request_url, headers)

    def renew_config(self):
        config = configparser.ConfigParser()
        config.read('config.ini')

        # config['DEFAULT']['request_url'] = 'https://new_request_url'


        with open('config.ini', 'w') as configfile:
            config.write(configfile)

# OCR_Config.init_config()