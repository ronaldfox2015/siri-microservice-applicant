# Usa una imagen base de Python 3.9-slim
FROM python:3.9-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Instala dependencias de sistema y Nginx
RUN apt-get update && \
    apt-get install -y curl && \
    apt-get install -y nginx && \
    apt-get clean

# Copia el archivo de configuración de Nginx al contenedor
COPY docker/dev/resources/nginx.conf /etc/nginx/nginx.conf
COPY app/requirements.txt /app

# Copia los archivos de la aplicación Flask al contenedor
COPY app /app

# Instala Flask
RUN pip install --upgrade pip && pip install -r requirements.txt
RUN pip install --upgrade pip
RUN pip install flask 
RUN export FLASK_APP=app.py
RUN export PYTHONPATH=/app
# Expone el puerto que usará Nginx
EXPOSE 5000 80

# Comando para iniciar Nginx y Gunicorn
CMD ["sh", "-c", "service nginx start && python app.py"]
