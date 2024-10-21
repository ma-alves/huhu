# Não apagar esse caralho vsf criar função ou método em database.py

import json

with open('database.json') as d:
    data = json.load(d)

    with open('database.json', 'w') as file:
        json.dump(data, file, indent=2)
