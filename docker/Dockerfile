# Usa una imagen base oficial de Python
FROM python:3.9

# Establece el directorio de trabajo en /code
WORKDIR /code

# Copia el archivo de requisitos y el archivo de configuración de Sphinx
COPY requirements.txt /code/
COPY docs/requirements.txt /code/docs/

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -r docs/requirements.txt

# Copia el resto del código de la aplicación
COPY . /code/

# Instala Sphinx
RUN apt-get update && apt-get install -y python3-sphinx

# Establece el PYTHONPATH
ENV PYTHONPATH=/code

# Expone el puerto 8000 para la aplicación FastAPI
EXPOSE 8000

# Comando para ejecutar la aplicación FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]