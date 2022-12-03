# flask项目初始化模版

## depends
. flask  
. flask-session  
. flask-sqlalchemy  
. psycopg2  
. redis  
. flask-migrate  
. gunicorn  
. flask-login  

## functions

### settings
. database  
. redis  
. other  

### redis
```
1. flask-session
2. SESSION_TYPE = 'redis'

session.get('key', 'not set')
session["name"] = None
```

### database
```
# 1. create_all, 无法修改表结构，实现数据库迁移
app = create_app()
with app.app_context():
    db.create_all()

# 2. flask_migrate
flask --app manage db init # 初始化，只执行一次
flask --app manage db migrate
flask --app manage db upgrade
```
### server
```
# -w 4,多进程
gunicorn --daemon -b 0.0.0.0:5000 manage:app
```
### docker
```
# 1
docker build -t flaskr:1.0 .
# 2, file: --env-file or -e PASSWORD=123456
docker run -d --name flaskr -p server_port:container_port -v /server/parh:/container/path --env-file env flaskr:1.0
```

### 用户认证
```

```