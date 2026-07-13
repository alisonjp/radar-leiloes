from pathlib import Path

print("Robô Müller iniciado")

arquivo = Path("amostra_muller.html")

if not arquivo.exists():
    print("Arquivo não encontrado")
    exit()

conteudo = arquivo.read_text(encoding="utf-8")

total_links = conteudo.count("/item/")

print(f"Arquivo carregado")
print(f"Ocorrências de lotes encontradas: {total_links}")
