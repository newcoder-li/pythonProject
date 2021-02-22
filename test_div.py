import pytest
import yaml

# 导入test_div中的测试数据
with open("./datas/test_div.yaml") as f:
    data = yaml.safe_load(f)['objects']
    print(data)
    case = data['cases']
    case_1 = case[0]['case1']
    case_2 = case[1]['case2']
    case_3 = case[2]['case3']
    case_4 = case[3]['case4']
    case_5 = case[4]['case5']
    case_6 = case[5]['case6']
    id = data['ids']


# 利用fixture进行类加载初始化操作
@pytest.mark.usefixtures("start")
class TestDiv:
    def setup(self):
        print("开始计算")

    def teardown(self):
        print("计算结束")

    @pytest.mark.parametrize(
        ("a", "b", "expect"), case_1, ids=id
    )
    # 等价类
    def test_01(self, start, a, b, expect):
        result = start.div(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expect

    @pytest.mark.parametrize(
        ("a", "b", "expect"), case_2, ids=id
    )
    # 任何数除以它本身等于1
    def test_02(self, start, a, b, expect):
        if a == b:
            print(f"{a}和{b}相等除数等于1")
        result = start.div(a, b)
        if isinstance(result, float):
            result = round(result, 0)
        assert result == expect

    @pytest.mark.parametrize(
        ("a", "b", "expect"), case_3, ids=id
    )
    # 非数字除法
    def test_03(self, start, a, b, expect):
        try:
            if isinstance(a or b, str):
                print(f"{a}或{b}不是数字")
            result = start.div(a, b)
        except TypeError:
            assert TypeError

    @pytest.mark.parametrize(
        ("a", "b", "expect"), case_4, ids=id
    )
    # 任何数除以1都是它本身
    def test_04(self, start, a, b, expect):
        result = start.div(a, b)
        assert result == expect

    @pytest.mark.parametrize(
        ("a", "b", "expect"), case_5, ids=id
    )
    # 除数不能为0
    def test_05(self, start, a, b, expect):
        try:
            if b == 0:
                print("除数不能为0")
            result = start.div(a, b)
        except ZeroDivisionError:
            assert ZeroDivisionError

    @pytest.mark.parametrize(
        ("a", "b", "expect"), case_6, ids=id
    )
    # 0除以任何数均为0
    def test_06(self, start, a, b, expect):
        if a == 0:
            print("0除以任何数均为0")
            result = start.div(a, b)
        if isinstance(result, float):
            result = round(result, 1)
        assert result == expect
