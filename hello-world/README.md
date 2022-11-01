# uvicorn
| Host | Description |
| --- | ----------- |
| 0.0.0.0 | Rede Local pode acessar - ipdamaquina/8000|
| 127.0.0.1 | Localhost Somente |

# gunicorn
 | Comandos | Description |
| --- | ----------- |
| guvicorn main:app| Comandos para executar Servidor|
| <b>-w [nº_workers]</b> |  Balancaemento de Carga|
| -k uvicorn.workers.UvicornWorker| Utiliza o uvicorn como worker|
