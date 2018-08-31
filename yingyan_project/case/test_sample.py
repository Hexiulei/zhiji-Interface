import pytest
import logging
import time
now = time.strftime("%Y_%m_%d_%H")
logging.basicConfig(level=logging.DEBUG,
                    filename='E:\pycharm\yingyan_project\logs\log_%s.txt' % now,
                    filemode='a',
                    format='%(asctime)s - %(levelname)s: %(message)s')


def func(x):
    return x + 1


def test_answer():
    log = logging.getLogger('func')
    assert func(3) == 4
    log.info('sadasda1')


if __name__ == "__main__":
    pytest.main()
