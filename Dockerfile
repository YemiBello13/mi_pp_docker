# Etapa 1: Imagen base con Python
# Usamos una imagen oficial de Python. 'slim' es una versión más ligera.
FROM python:3.9-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de dependencias primero para aprovechar el cache de Docker
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de la aplicación
COPY ./app ./app

# Exponer el puerto en el que la aplicación Flask se ejecutará
EXPOSE 5000

# Comando para ejecutar la aplicación cuando el contenedor inicie
CMD ["python", "app/main.py"]