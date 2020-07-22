import pytest
import yaml

class TestData:


    @pytest.mark.parametrize("a, b", yaml.safe_load(open("./data.yaml")))
    def test_data(self, a, b):
        # a = 10
        # b = 20
        # data = yaml.load(open("./data.yaml"))
        # data1 = yaml.safe_load(open("./data.yaml"))
        # print(data1)
        # print(data)
        print(a+b)

    @pytest.mark.parametrize('env', yaml.safe_load(open('./env.yaml')))
    def test_env(self, env):

        print(yaml.safe_load(open('./env.yaml')))

        if 'test' in env:
            print("测试环境")
            print("测试环境地址是：", env["test"])
        elif 'dev' in env:
            print("开发环境")
            print("开发环境地址是：", env["dev"])