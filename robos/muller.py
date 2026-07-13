import re
from pathlib import Path

arquivo = Path("amostra_lote_7393.html")

conteudo = arquivo.read_text(encoding="utf-8")

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

print("TITULO:", titulo.group(1) if titulo else "")
print("CIDADE:", cidade.group(1) if cidade else "")
print("BAIRRO:", bairro.group(1) if bairro else "")
print("DATA 1:", data_1.group(1) if data_1 else "")
print("VALOR 1:", valor_1.group(1) if valor_1 else "")
print("DATA 2:", data_2.group(1) if data_2 else "")
print("VALOR 2:", valor_2.group(1) if valor_2 else "")
print("AVALIACAO:", avaliacao.group(1) if avaliacao else "")
