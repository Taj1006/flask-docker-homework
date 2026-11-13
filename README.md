# Flask Docker Homework

งานตามโจทย์เพิ่มเติมใน Colab บทที่ 2: รับข้อความผ่าน HTTP POST แสดงผลบนเว็บ และบันทึกต่อท้าย `/app/log.txt` ภายใน container โดยใช้ UTF-8

## รัน

```bash
docker compose up --build
```

เปิด http://localhost:5000 กรอกข้อความ แล้วกด **ส่งข้อมูล (Submit)**

## ตรวจสอบ log ใน container

เปิด Terminal อีกหน้าต่างแล้วรัน:

```bash
docker compose exec web_app cat /app/log.txt
```

ส่งข้อความหลายครั้งเพื่อดูว่าข้อความเดิมยังอยู่และข้อความใหม่ถูกเพิ่มต่อท้าย
ไฟล์ log จะเกิดขึ้นหลังส่งข้อความครั้งแรก และอยู่ใน container จึงควรคัดลอกก่อนลบ container:

```bash
docker compose cp web_app:/app/log.txt ./log.txt
```

## ภาพหลักฐานที่ต้องส่ง

1. หน้าเว็บฟอร์มกรอกข้อความ
2. หน้า Message received หลังส่งข้อความ
3. Terminal ที่รัน `docker compose up --build` และ Terminal ที่แสดงผล `cat /app/log.txt` ภายใน container

ใช้ภาพจากการรันจริง และใส่ภาพในโฟลเดอร์ `screenshots/` ได้
Docker Compose รุ่นใหม่ใช้ `docker compose` แทนคำสั่ง `docker-compose` ใน Colab

## หยุด

```bash
docker compose down
```

## ส่งงาน

อัปโหลด `app.py`, `Dockerfile`, `requirements.txt`, `docker-compose.yml`, `log.txt` ที่คัดลอกจากการรันจริง และภาพหลักฐานไปยัง GitHub แล้วแนบลิงก์ repository ใน Google Classroom
