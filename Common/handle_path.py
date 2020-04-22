import os

# 本文件路径，包括文件名
os.path.abspath(__file__)

# 本文件父目录路径
os.path.dirname(os.path.abspath(__file__))

# 项目根路径
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 获取OutPuts目录
OutPuts_dir = os.path.join(base_dir, "OutPuts")

# 获取logs目录
logs_dir = os.path.join(OutPuts_dir, "logs")

# 获取pageshots目录
screenshot_dir = os.path.join(OutPuts_dir, "pageshots")

# 获取reports目录
reports_dir = os.path.join(OutPuts_dir, "reports")

# 获取TestDatas目录
testdatas_dir = os.path.join(base_dir, "TestDatas")

# 获取TestCases目录
testcases_dir = os.path.join(base_dir, "TestCases")

# 获取caps目录
caps_dir = os.path.join(base_dir, "caps")

if __name__ == '__main__':
    print(screenshot_dir)
