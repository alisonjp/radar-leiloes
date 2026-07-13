from pathlib import Path
import re

print("Robô Müller iniciado")

arquivo = Path("amostra_muller.html")

conteudo = arquivo.read_text(encoding="utf-8")

titulos = re.findall(
    r"<h5>(.*?)</h5>",
    conteudo,
    re.DOTALL
)

titulos_filtrados = []

for titulo in titulos:
    titulo = titulo.strip()

    if titulo == "Lance Inicial":
        continue

    titulos_filtrados.append(titulo)

print(f"Títulos válidos: {len(titulos_filtrados)}")

for titulo in titulos_filtrados[:20]:
    print(titulo)
