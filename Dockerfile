# استخدم نسخة خفيفة من Python
FROM python:3.10-slim

# تحديد مجلد العمل داخل الحاوية
WORKDIR /app

# نسخ ملفات المتطلبات وتثبيتها
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# نسخ جميع الملفات داخل المشروع
COPY . .

# تعيين المنفذ الذي يستمع عليه التطبيق (مهم جدًا لـ Render)
EXPOSE 8000
# أمر التشغيل النهائي (FastAPI مع uvicorn)

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

