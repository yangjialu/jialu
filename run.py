import pytest


if __name__ == '__main__':
    pytest.main(["-m error", r"--html=report\test.html", r"--alluredir=report\allure"])