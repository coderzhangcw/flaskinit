FROM python:3.10

WORKDIR /project

COPY . /project/

RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

ENTRYPOINT ["./gunicorn.sh"]