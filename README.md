# wuhan2020 Donation Platform

# precondition
* Python 3
	- Windows用户，推荐安装名为 Miniconda 的Python发行版
	- [Miniconda](https://docs.conda.io/en/latest/miniconda.html) [Python 3.7 - Miniconda3 Windows 64-bit](https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe)

# step

## step-01 - Python包安装

### setup-01 - Miniconda(conda用户)
```bash
conda install --file requirements-conda.txt -y
pip install -r requirements-pip.txt
```

### setup-01 - 官方Python(pip用户)
```bash
pip install -r requirements-conda.txt
pip install -r requirements-pip.txt
```

## step-02 - 初始化
```bash
# 数据库初始化(创建表)
python manage.py migrate
# 创建管理用户(用户名、手机号、密码)
python manage.py createsuperuser
```

## step-03 - 运行
```bash
python manage.py runserver 0.0.0.0:8989
```

## step-04 - 访问
- 前台页面: http://127.0.0.1:8989/
- ApiRoot: http://127.0.0.1:8989/api/
- 管理后台: http://127.0.0.1:8989/admin/

## tips
* 如果Windows平台的官方Python用户，使用pip安装Python包报错，错误提示信息中带有“MicroSoft Vistual C++”等信息，一般是因为所安装的库底层使用了C/C++代码加速，需要C/C++环境编译，此时推荐的解决办法是安装Miniconda。
	- 安装Miniconda时，推荐勾选添加到环境变量Path
	- Mac OSX 和 Linux 用户无需安装Miniconda，出现编译问题时，需要安装 gcc/g++ 等编译工具 和 python-dev 库。
* 国内用户使用pip安装包慢时，可以使用豆瓣源加速
	- 单个包-示例: `pip install -i https://pypi.doubanio.com/simple/ --trusted-host pypi.doubanio.com <package>`
	- 清单文件-示例: `pip install -i https://pypi.doubanio.com/simple/ --trusted-host pypi.doubanio.com -r requirements.txt`
