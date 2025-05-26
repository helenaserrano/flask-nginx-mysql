# Imagen base oficial de Python
FROM python:3.11-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar e instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de los archivos
COPY app.py .

# Exponer el puerto para Flask
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
