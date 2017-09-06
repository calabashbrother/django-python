# 说明 #
### 正在学习中 持续更新 ###
### 本项目用于从零开始学习Python web开发（使用Django框架） ###
### 正在学习的小伙伴可以相互探讨 大神就别在此浪费时间了 ###
- 初始化 开启服务

        python manage.py migrate
        python manage.py runserver
	

	默认http://127.0.0.1:8000
   

- 安装mysqlclient

        pip install mysqlclient

- model

	  1. 创建models.py文件 定义model 
	  2. 在settings.py 中 INSTALLED_APPS 添加 'mysite' 应用
	  3. python manage.py makemigrations mysite
	  4. python manage.py migrate
    
    
    
