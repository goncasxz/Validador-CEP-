import re

FAIXAS_CEP = {
    "Sorocaba": ("18000-000", "18109-999"),
    "Votorantim": ("18110-000", "18119-999"),
    "Capela do Alto": ("18195-000", "18199-999"),
    "Sao Roque": ("18130-000", "18146-999"),
    "Itu": ("13300-000", "13314-999"),
    "Campinas": ("13000-000", "13139-999"),
    "Boituva": ("18550-000", "18559-999"),
    "Jundiai": ("13200-000", "13219-999"),
    "Piracicaba": ("13400-000", "13431-999"),
    "Limeira": ("13480-000", "13489-999"),
    "Americana": ("13465-000", "13479-999")
}

def validar_cep(cep, cidade):
    cep_limpo = re.sub(r'\D', '', cep)

    if len(cep_limpo) != 8 or cidade not in FAIXAS_CEP:
        return False

    cep_formatado = f"{cep_limpo[:5]}-{cep_limpo[5:]}"
    inicio, fim = FAIXAS_CEP[cidade]

    return inicio <= cep_formatado <= fim