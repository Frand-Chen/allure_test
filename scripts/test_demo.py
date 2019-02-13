# -*- coding=utf-8 -*-
import allure
import pytest

class Test_allure:
    def setup(self):
        print(1)
    def teardown(self):
        print(2)

    @allure.step(title='步骤001')
    @allure.severity('blocker')
    # @allure.severity(allure.severity_level.CRITICAL)
    def test_fun1(self):
        allure.attach('描述', '我是测试步骤00333333的描述～～～')
        assert 1

    @allure.step(title="步骤二")
    @allure.severity('blocker')
    def test_fun2(self):
        # allure.attach('描述', '我是测试步骤00444的描述～～～')
        imgfile = open(r'F:\allure_test1\picture1.png','rb').read()
        print(type(imgfile))
        # print(imgfile)
        allure.attach('成功截图', str(imgfile),allure.attachment_type.PNG)
        print(4)
        assert 1

