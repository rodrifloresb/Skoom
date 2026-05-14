## Dependencias
```bash
sudo apt update
```

```bash
sudo apt install -y pkg-config build-essential default-libmysqlclient-dev
```

```bash
sudo apt install -y libmariadb-dev
```

```bash
sudo apt install python3-venv python3-pip
```

## Instalacion

Crear entorno virtual

$ make venv 

Instalar dependencias:

$ make install

Crear/Levantar base de dato:

$ make db-up

Ejecutar servidor de desarrollo:

$ make run


