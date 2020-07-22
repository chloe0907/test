import allure

@allure.feature("登录模块")
class TestLogin:

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("登录成功")
    def test_login_success(self):
        print("这是登录，测试用例，登录成功")
        pass

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("登录失败")
    def test_login_fail_a(self):
        print("这是登录，测试用例，登录失败")
        pass


    TEST_CASE_LINK='https://www.tapd.cn/33641957/bugtrace/bugreports/my_view'
    @allure.link("https://www.tapd.cn/33641957/bugtrace/bugs/view?bug_id=1133641957001003653&url_cache_key=f08f976f7d7a2218adcafc314251340e", name="bug链接")
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.testcase(TEST_CASE_LINK, name="登录测试用例")
    @allure.story("用户名缺失title")
    #--allure-link-pattern=issue:https://www.tapd.cn/33641957/bugtrace/bugs/view?bug_id={}
    @allure.issue("1133641957001003653", "这是个issue")
    def test_login_fail_b(self):
        with allure.step("请输入用户名"):
            print("用户名缺失")
        with allure.step("请输入密码"):
            print("密码缺失")
        with allure.step("点击登录"):
            print("点击登录")
        pass

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("密码缺失title")
    def test_login_fail_c(self):
        # allure.attach("这是一个文本信息", attachment_type=allure.attachment_type.TEXT)
        # allure.attach("<body>这个一段body块</body>", "HTML测试块", attachment_type=allure.attachment_type.HTML)
        allure.attach.file("D:\\PycharmProjects\\test\\allureDemo\\resource\c1a1e51592203ede61e94887364bfbf0.jpg", name="这是一张图片", attachment_type=allure.attachment_type.JPG)
        print("密码缺失")
        pass
