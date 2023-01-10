import requests

from bripinfo_api import settings


def test_deve_fornecer_o_status_ativo_da_api():
    api_domain = settings.API_DOMAIN
    response = requests.get(f"http://{api_domain}/status")

    assert response.status_code == 200


def test_deve_retornar_os_dados_do_registrobr_por_ip():
    api_domain = settings.API_DOMAIN
    response = requests.get(f"http://{api_domain}/consulta/ip?q=189.82.191.46")
    data = response.json()

    assert data.get("ref") == "AS7738"


def test_deve_retornar_404_quando_o_ip_nao_for_encontrato_ou_invalido():
    api_domain = settings.API_DOMAIN
    response = requests.get(f"http://{api_domain}/consulta/ip?q=189.82.19")

    assert response.status_code == 404


def test_deve_retornar_os_dados_do_registrobr_por_cnpj():
    api_domain = settings.API_DOMAIN
    response = requests.get(f"http://{api_domain}/consulta/cnpj?q=02041460000193")
    data = response.json()

    assert data.get("ref") == "AS7738"


def test_deve_retornar_404_quando_o_cnpj_nao_for_encontrato_ou_invalido():
    api_domain = settings.API_DOMAIN
    response = requests.get(f"http://{api_domain}/consulta/cnpj?q=23230204146000")

    assert response.status_code == 404
