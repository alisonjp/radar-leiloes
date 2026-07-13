import os
import re
from pathlib import Path

from supabase import create_client

url = os.environ["SUPABASE_URL"]
key = os.environ["SUPABASE_SERVICE_ROLE_KEY"]

supabase = create_client(url, key)

arquivo = Path("amostra_lote_7393.html")
conteudo = arquivo.read_text(encoding="utf-8")


def moeda_para_numero(valor):
    valor = valor.replace(".", "").replace(",", ".")
    return float(valor)


titulo = re.search(
    r"<h1>(APARTAMENTO.*?|CASA.*?|TERRENO.*?)</h1>",
    conteudo,
    re.DOTALL
)

cidade = re.search(
    r"<b>Cidade:</b>\s*([^<]+)",
    conteudo
)

bairro = re.search(
    r"Bairro:\s*([^\.]+)",
    conteudo
)

endereco = re.search(
    r"<b>Endereço:</b>\s*([^<]+)",
    conteudo
)

data_1 = re.search(
    r"Data 1º Leilão:</strong>\s*([^<]+)",
    conteudo
)

valor_1 = re.search(
    r"Data 1º Leilão:.*?Lance Inicial:</strong>\s*R\$([0-9\.\,]+)",
    conteudo,
    re.DOTALL
)

data_2 = re.search(
    r"Data 2º Leilão:</strong>\s*([^<]+)",
    conteudo
)

valor_2 = re.search(
    r"Data 2º Leilão:.*?Lance Inicial:</strong>\s*R\$([0-9\.\,]+)",
    conteudo,
    re.DOTALL
)

avaliacao = re.search(
    r"Valor de Avaliação:</strong>\s*R\$([0-9\.\,]+)",
    conteudo
)

dados = {
    "titulo": titulo.group(1).strip(),
    "tipo_imovel": "APARTAMENTO",
    "cidade": cidade.group(1).strip(),
    "bairro": bairro.group(1).strip(),
    "endereco": endereco.group(1).strip(),
    "valor_avaliacao": moeda_para_numero(avaliacao.group(1)),
    "data_1_leilao": data_1.group(1).strip(),
    "valor_1_leilao": moeda_para_numero(valor_1.group(1)),
    "data_2_leilao": data_2.group(1).strip(),
    "valor_2_leilao": moeda_para_numero(valor_2.group(1)),
    "url_lote": "https://www.mullerleiloes.com.br/item/7393/detalhes?page=1",
    "leiloeiro": "MULLER",
    "status": "ATIVO",
    "fonte_id": 1
}

print(dados)

resultado = supabase.table("imoveis").insert(dados).execute()

print("IMÓVEL COMPLETO INSERIDO COM SUCESSO")
