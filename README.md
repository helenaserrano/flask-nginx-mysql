# Helm Chart: my-app

Este Chart despliega una aplicación compuesta por tres componentes:

- **Frontend**
- **Backend**
- **Database** (PostgreSQL)

## Estructura

Este chart utiliza subdirectorios en `templates/` para organizar los recursos de cada componente. La base de datos utiliza un PVC para persistencia de datos.

## Instalación

```bash
helm install my-app ./my-app

