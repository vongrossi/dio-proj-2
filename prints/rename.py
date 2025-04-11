import os
import re

# Diretório onde estão as imagens
diretorio = "./"

# Regex para capturar nomes do tipo "image (N)"
padrao = re.compile(r"image \((\d+)\)")

# Loop para percorrer todos os arquivos no diretório
for nome_arquivo in os.listdir(diretorio):
    match = padrao.match(nome_arquivo)
    if match:
        numero = match.group(1)  # Captura apenas o número dentro dos parênteses
        novo_nome = f"image_{numero}{os.path.splitext(nome_arquivo)[1]}"  # Mantém a extensão original
        os.rename(os.path.join(diretorio, nome_arquivo), os.path.join(diretorio, novo_nome))

print("Renomeação concluída!")

