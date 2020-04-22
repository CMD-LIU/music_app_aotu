import pytest

from Common.handle_outputs import handle_outputs

if __name__ == '__main__':
    '''
       运行前删除allure_report文件夹及文件
       运行前删除pageshots文件夹下截图
       运行前删除logs文件夹下日志
    '''
    handle_outputs.handle_delete_allure_report()
    handle_outputs.handle_delete_screenshots()
    handle_outputs.handle_delete_logs()

    '''
      执行标记smoke的用例
      失败重运行2次，间隔时间5秒
      生成.xml格式的报告
      生成.html格式的报告
      生成allure报告的相关文件
    '''
    pytest.main([
        # "-m", "smoke",
        "--reruns", "2", "--reruns-delay", "5",
        "--junitxml=OutPuts/reports/result.xml",
        "--html=OutPuts/reports/result.html",
        "--alluredir=OutPuts/allure_report"
    ])
