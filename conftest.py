# -*- coding: utf-8 -*-
# @Author  : lidonghui
import pytest
from calc import Calculator


@pytest.fixture(scope="class")
def start():
    print("初始化操作")
    calc = Calculator()
    return calc
