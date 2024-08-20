### Assignment : Docker 
![alt text](img1.png)
**Github : https://github.com/maipk39196/docker---flask---mysql**

## **Step 1 setup directory**

## **Step 2 Dockerfile for build images**
ทำการสร้าง image สำหรับ sdpx/api และ sdpx/db  

dockerfile - sdpx/api
```
FROM python:3.12-alpine

WORKDIR /api-docker
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]
```
build image command with image name : ตรวจสอบให้แน่ใจว่าอยู่ใน path ที่มี dockerfile
```
docker build -t sdpx/api .
```
**Build Image Finished**
## **Step 3 Create docker-compose file for build containers**
docker-compose.yml
```
version: '3'

services:
  api-dev:
    image: sdpx/api
    ports:
      - 8081:80

  api-test:
    build: 
      context: app
      dockerfile: Dockerfile
    ports:
      - 8082:80
```
Build container command :
```
docker-compose up -d --build
```
## **Step 4**
