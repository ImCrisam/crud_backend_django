FROM python:bookworm

# Instalar dependencias del sistema necesarias para psycopg2 y otras libs
RUN apt-get update \
    && apt-get install -y \
       xdg-utils \
       gcc \
       libpq-dev 

# Carpeta de trabajo
WORKDIR /workspaces

# Copiar requirements.txt desde la raíz del proyecto
COPY ../requirements.txt .

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Mantener contenedor vivo (ajústalo después para correr tu app)
CMD ["sleep", "infinity"]
