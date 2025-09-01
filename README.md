# CRUD Backend Django con Dev Containers

Este proyecto muestra cómo levantar un backend en **Django** dentro de un contenedor de desarrollo usando **VSCode** y **Docker**.  
Gracias a **Dev Containers**, podemos trabajar en un entorno aislado pero completamente accesible desde nuestro host, con la API y la base de datos listas para usar.

---

## 🚀 Requisitos previos

Antes de comenzar, asegúrate de tener instalado:
- [Visual Studio Code](https://code.visualstudio.com/)  
- Extensión **Remote - Containers** en VSCode  
👉 [Instalar aquí](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-containers)  
- [Docker Desktop](https://www.docker.com/get-started/)  

---

## 📦 Clonar e iniciar el proyecto

Clona el repositorio y ábrelo en VSCode:

```bash
git clone https://github.com/ImCrisam/crud_backend_django
cd crud_backend_django
code .
```

Cuando VSCode detecte el archivo `.devcontainer`, puede mostrar una notificación o puedes abrir el menú de comandos con **F1**.

Opciones disponibles:
- **Rebuild and Reopen in Container** → Crea el contenedor por primera vez o lo reconstruye si hubo cambios.
- **Reopen in Container** → Monta el proyecto en el contenedor ya existente.

Una vez abierto, el proyecto tendrá corriendo:
- API de Django en el puerto **8000**
- Base de datos Postgres en el puerto **5432**

Ambos servicios son accesibles desde tu host (Windows, Linux o macOS). La base de datos puede abrirse desde cualquier gestor SQL.

---

## 🔌 Puertos expuestos

El contenedor expone los siguientes puertos al host:
- **Django API**: `localhost:8000`
- **Postgres DB**: `localhost:5432`

Esto se define en el archivo `devcontainer.json`:

```json
"forwardPorts": [
  5432,
  8000
]
```

---

## 📑 Consultas de prueba

En el archivo `brands.http` encontrarás ejemplos de peticiones HTTP para probar la API.  
Con la extensión **REST Client** puedes ejecutarlas directamente desde VSCode.

---

## ⚙️ Configuración del Dev Container

La configuración básica del entorno de desarrollo está en `.devcontainer/devcontainer.json`.  
Ahí se definen comandos automáticos, extensiones y personalización del editor.

### Comandos automáticos
- **postCreateCommand** → Se ejecuta una sola vez cuando se crea el contenedor (por ejemplo, instalar dependencias).
- **postStartCommand** → Se ejecuta cada vez que se inicia el contenedor.

Esto permite automatizar el arranque del proyecto sin pasos manuales extra.

### Personalización de VSCode
Cada proyecto puede traer su propio set de extensiones y configuraciones, sin afectar tu instalación global de VSCode.

Ejemplo:

```json
"vscode": {
  "settings": {
    "workbench.colorTheme": "Visual Studio Dark"
  },
  "extensions": [
    "streetsidesoftware.code-spell-checker",
    "chrisvltn.log-wrapper-for-vscode",
    "ms-python.python",
    "ms-python.vscode-pylance",
    "humao.rest-client",
    "ms-azuretools.vscode-containers",
    "eamodio.gitlens",
    "omnilib.ufmt",
    "redhat.vscode-yaml",
    "GitHub.copilot-chat",
    "GitHub.copilot"
  ]
}
```

De esta manera, cada vez que abras el proyecto tendrás un VSCode configurado igual para todos los desarrolladores del equipo.

---

## 🛡️ Seguridad de archivos

No hay riesgo de perder tus avances.  
Los archivos se editan directamente en el contenedor, no en una copia temporal. Todo lo que trabajes queda guardado de forma segura en tu máquina.

---

## 📚 Resumen rápido

1. Instalar Docker y VSCode con la extensión de Dev Containers.
2. Clonar el repo y abrirlo en VSCode.
3. Seleccionar **Rebuild and Reopen in Container**.
4. Acceder a:
   - `http://localhost:8000` → Django API
   - `localhost:5432` → Postgres (desde gestor de bases de datos).
5. Usar `brands.http` para probar endpoints desde VSCode.

---

## 📡 Endpoints de la API

- `GET /api/brands/` → listar marcas
- `POST /api/brands/` → crear marca (name, description)
- `GET /api/brands/{id}/` → obtener una marca
- `PUT/PATCH /api/brands/{id}/` → actualizar una marca
- `DELETE /api/brands/{id}/` → eliminar una marca

---

## ⚠️ Notas de seguridad

El proyecto incluye un `FakeAuthMiddleware` para desarrollo local que simula autenticación.  
