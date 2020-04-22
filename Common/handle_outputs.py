import os
import shutil

from Common import handle_path


class Handle_Outputs():

    # 用例执行前清除allure_report文件夹及文件夹下的文件
    def handle_delete_allure_report(self):
        # 切换到Outputs文件夹路径
        os.chdir(handle_path.OutPuts_dir)
        try:
            # 清除allure_report文件夹及文件夹下的文件
            shutil.rmtree('allure_report')
        except FileNotFoundError as e:
            print(f'allure_report目录不存在，详细信息如下：\n{e}')
        # 切换到项目路径
        os.chdir(handle_path.base_dir)

    # 用例执行前清除screenshots文件夹下.png格式的截图文件
    def handle_delete_screenshots(self):
        for i in os.listdir(handle_path.screenshot_dir):
            if 'png' in i:
                os.unlink(os.path.join(handle_path.screenshot_dir, i))
        # 切换到项目路径
        os.chdir(handle_path.base_dir)

    # 用例执行前清除logs文件夹下.log格式的文件
    def handle_delete_logs(self):
        for i in os.listdir(handle_path.logs_dir):
            if 'log' in i:
                os.unlink(os.path.join(handle_path.logs_dir, i))
        # 切换到项目路径
        os.chdir(handle_path.base_dir)


handle_outputs = Handle_Outputs()

if __name__ == '__main__':
    handle_outputs.handle_delete_allure_report()
