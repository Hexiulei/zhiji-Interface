import pytest
import random
import requests
import re
import logging
import time
now = time.strftime("%Y_%m_%d_%H")
logging.basicConfig(level=logging.DEBUG, filename='E:\pycharm\yingyan_project\logs\log_%s.txt' % now,
                    filemode='a', format='%(asctime)s - %(levelname)s: %(message)s')


class Test_class():

    def test_j01(self):
        log = logging.getLogger('test_j01')
        u"app登录"
        self.url_1 = 'http://app.91ylian.com/auth/login'
        self.body_post = {
            'client_id': '866413033303189',
            'phone_num': random.choice([15997792758, 17681891569]),
            'password': '123456'
                        }
        s = requests.session()
        self.url_2 = s.post(self.url_1, data=self.body_post)
        # self.url_2 = requests.post(self.url_1, data=self.body_post)
        t = re.findall(r'\b424348\b', self.url_2.text)
        log.info('终于可以啦啦啦：')
        try:
            assert t == ['424348']
        except AssertionError as err:
            print('error')
            assert t == ['424348']


if __name__ == "__main__":
    pytest.main()
