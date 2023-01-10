import os

# Configs
# ------------------------------------------------------------------------------
CONFIG = {
    'registro_br': {
        'main_file': 'https://ftp.registro.br/pub/numeracao/origin/nicbr-asn-blk-latest.txt',
        'sha256_mainfile': 'https://ftp.registro.br/pub/numeracao/origin/nicbr-asn-blk-latest.txt.sha256'
    }
}

# General
# ------------------------------------------------------------------------------
API_DOMAIN = os.environ.get("API_DOMAIN", default="localhost:8000")
