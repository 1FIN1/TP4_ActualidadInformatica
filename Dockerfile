# Usamos la imagen de Python 3.13
FROM python:3.13-slim

# Definimos el directorio de trabajo
WORKDIR /app

# Copiamos e instalamos dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto de los archivos de la app
COPY . .

# Exponemos el puerto
EXPOSE 8000

# Comando por defecto
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
