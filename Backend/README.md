Dependecias : 

`sudo apt update`
`sudo apt install -y pkg-config build-essential default-libmysqlclient-dev`
`sudo apt install -y libmariadb-dev`


`sudo apt install python3-venv`

Crear entorno : 


`Backend: ~$ python3 -m venv .venv`

`source .venv/bin/activate`

`pip install -r requirements.txt`

o make venv , make install.

Ejecucion del servidor :

`fastapi dev src/main.py` o make run


DB :

db-up: crear base
db-down: apagar db
db-logs: ver logs
db-shell: Entrar a la base
