## 模型字段修改
1. 修改 `models.py` 中的模型类
2. 生成迁移文件: `python manage.py makemigrations`
3. 将迁移改动写入到数据库 `python manage.py migrate`