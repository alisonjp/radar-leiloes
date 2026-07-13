from pathlib import Path

arquivo = Path("amostra_muller.html")

print("Robô Müller iniciado")

if arquivo.exists():
    print("Arquivo encontrado")
else:
    print("Arquivo não encontrado")
