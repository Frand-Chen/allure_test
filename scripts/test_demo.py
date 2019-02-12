# -*- coding=utf-8 -*-
import allure
import pytest

class Test_allure:
    def setup(self):
        print(1)
    def teardown(self):
        print(2)

    @allure.step(title='步骤001')
    @allure.severity(allure.severity_level.CRITICAL)
    # @allure.severity("critical")
    def test_fun1(self):
        allure.attach('描述', '我是测试步骤001的描述～～～')
        assert 1

    @allure.step(title="步骤二")
    @allure.severity('blocker')
    def test_fun2(self):
        allure.attach('描述', '我是测试步骤002的描述～～～')
        print(4)
        assert 0

