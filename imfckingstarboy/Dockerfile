# 1. Bazna slika
FROM python:3.10.1

# 2. Postavi radni direktorijum
WORKDIR /app

# 3. Kopiraj requirements.txt
COPY requirements.txt .

# 4. Instaliraj zavisnosti
RUN pip install --no-cache-dir -r requirements.txt

# 5. Kopiraj sve fajlove
COPY . .

# 6. Prikupi statičke fajlove
RUN python manage.py collectstatic --noinput

# 7. Expose port 8000
EXPOSE 8000

# 8. Defaultna komanda za pokretanje aplikacije
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "imfckingstarboy.wsgi:application"]
