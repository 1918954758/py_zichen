# -*- coding utf-8 -*-
# @ProjectName: py_zichen
# @Script: InstallVirtualEnv
# @Discription: 安装虚拟环境
# @Author: 子辰
# @Date: 2020-09-08 22:55
# @Software: PyCharm

"""
搭建虚拟环境
    1. 创建一个目录
    2. cmd进入这个目录
    3. 执行 pip install pipenv 安装虚拟环境
    4. 使用当前系统的Python3创建环境 pipenv --three
    5. 激活虚拟环境 pipenv shell
    6. 显示Python解释器信息 pipenv --py     可以查看虚拟环境python解释器位置
    7. 推出虚拟环境 exit
    8. 进入当前的虚拟环境 pipenv shell
    9. 查看虚拟环境包的情况 pipenv list
    10. 打开pycharm -> File -> Open(打开第一步创建的那个目录)
    11. 将虚拟环境解释器与pycharm绑定  settings -> project: 创建目录的名字 -> Prject Interpreter -> 向下的三角 -> show all
        -> 右上角的 + -> 可以看到是否绑定好，如果没有绑定号，我们可以手动绑定

"""

"""
pipenv常见操作：
    # 1. 包下载
        # 下载包之前，需要将国外下载源改为国内下载源
        # url = "https://pipi.tuna.tsinghua.edu.cn/simple"
        # 更改的配置文件在最开始创建的那个目录里面，有个叫 Pipfile的文件
    (补充，如果在爬虫的时候，解析H5页面，需要下载 lxml包  install lxml)
    下载指令：需要打开cmd，进入虚拟环境，然后在执行以下指令，下载包
            pipenv install requests
            pipenv install requests==2.21.0
    # 2. 查看当前下载包的情况
        pip list
    # 3. 查看当前包依赖情况
        pipenv graph
    # 4. 更新包
        pipenv update requests  # 更新requests当前包
        pipenv update           # 更新所有包
    # 5. 卸载包
        pipenv uninstall requests   # 卸载requests包
        pipenv uninstall --all      # 卸载全部包，并从Pipfile中移除
    # 6. 其他操作
        pipenv check    # 检查安全漏洞
    # 7. 更详细的资料可以参考文档：
        https://pypi.org/project/pipenv/
"""
