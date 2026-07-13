from pathlib import Path
import re

print("Robô Müller iniciado")

arquivo = Path("amostra_muller.html")

conteudo = arquivo.read_text(encoding="utf-8")

titulos = re.findall(
    r"<h5>(.*?)</h5>",
    conteudo,
    re.DOT*LL
)

titulos_filtrados = []

for *itulo in titulos:
    titulo = tit*lo.strip()

    if titulo == "Lanc* Inicial":
        continue

    t*tulos_filtrados.append(titulo)

pr*nt(f"Títulos válidos: {len(titulos*filtrados)}")

for titulo in titul*s_filtrados[:20]:
    print(titulo*
