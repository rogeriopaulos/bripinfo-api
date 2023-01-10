import ipaddress
import re

import requests
from fastapi import FastAPI, HTTPException

from bripinfo_api import settings

app = FastAPI()

_remote_file = settings.CONFIG['registro_br']['main_file']


@app.get("/status")
def api_status():
    return {"detail": "It's alive!!! 👍"}


@app.get("/consulta/ip")
def query_by_ip(q: str):
    response = requests.get(_remote_file)
    content = [line.split('|') for line in response.text.splitlines()]
    dataset = [
        {
            'ref': line[0],
            'name': line[1],
            'cnpj': line[2],
            'ips': list(line[3:])
        }
        for line in content]
    try:
        result = next(isp for isp in dataset for ip in isp['ips']
                      if ipaddress.ip_address(q) in ipaddress.ip_network(ip))
        result['registrobr_info'] = f'https://registro.br/tecnologia/ferramentas/whois/?search={q}'
        return result
    except ValueError:
        raise HTTPException(status_code=404, detail="Invalid IP address")


@app.get("/consulta/cnpj")
def query_by_cnpj(q: str):
    response = requests.get(_remote_file)
    content = [line.split('|') for line in response.text.splitlines()]
    dataset = [
        {
            'ref': line[0],
            'name': line[1],
            'cnpj': line[2],
            'ips': list(line[3:])
        }
        for line in content]
    try:
        return next(isp for isp in dataset if re.sub("[^0-9]", "", isp.get('cnpj')).startswith(q))
    except StopIteration:
        raise HTTPException(status_code=404, detail="Invalid CNPJ")
