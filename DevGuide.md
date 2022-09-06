# 应用开发指南

## 本地开发环境
### 创建虚拟环境
```
python3 -m venv venv
```
### 激活虚拟环境
```bash
. venv/bin/activate
```
### 安装FastApi
```bash
pip install fastapi
pip install "uvicorn[standard]"
```

### 运行
```
uvicorn main:app --reload
```
> 命令含义如下:

> main：main.py 文件（一个 Python「模块」）。

> app：在 main.py 文件中通过 app = FastAPI() 创建的对象。

> --reload：让服务器在更新代码后重新启动。仅在开发时使用该选项。

###  展示
http://127.0.0.1:8000

### 接口文档
http://127.0.0.1:8000/docs
