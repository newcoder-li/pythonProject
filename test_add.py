# -*- coding: utf-8 -*-
import pytest
import yaml

with open("datas/test_add.yaml") as f:
    data = yaml.safe_load(f)['objects']
    print(data)
    case = data['cases']
    case_1 = case[0]['case1']
    case_2 = case[1]['case2']
    case_3 = case[2]['case3']
    id = data['ids']


# 利用fixture进行类加载初始化操作
@pytest.mark.usefixtures("start")
class TestAdd:
    def setup(self):
        print("开始计算")

    def teardown(self):
        print("计算结束")

    @pytest.mark.parametrize(
        ("a", "b", "expect"), case_1, ids=id
    )
    # 等价类
    def test_01(self, start, a, b, expect):
        result = start.add(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expect

    @pytest.mark.parametrize(
        ("a", "b", "expect"), case_2, ids=id
    )
    # 0加任何数都等于它本身
    def test_02(self, start, a, b, expect):
        if a == 0 or b == 0:
            print(f"0加任何数都等于它本身")
        result = start.add(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expect

    @pytest.mark.parametrize(
        ("a", "b", "expect"), case_3, ids=id
    )
    # 非数字加法
    def test_03(self, start, a, b, expect):
        try:
            if isinstance(a or b, str):
                print(f"{a}或{b}不是数字")
            result = start.add(a, b)
        except TypeError:
            assert TypeError
