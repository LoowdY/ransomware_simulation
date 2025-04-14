import os
from cryptography.fernet import Fernet

# Carregar a chave previamente gerada
def carregar_chave():
    with open("chave.key", "rb") as chave_file:
        return chave_file.read()

# Descriptografar arquivos em uma pasta
def descriptografar_arquivos(pasta, fernet):
    for root, dirs, files in os.walk(pasta):
        for file in files:
            caminho = os.path.join(root, file)
            if file != "chave.key" and not file.endswith(".txt"):
                try:
                    with open(caminho, "rb") as enc_file:
                        dados = enc_file.read()
                    dados_descriptografados = fernet.decrypt(dados)
                    with open(caminho, "wb") as dec_file:
                        dec_file.write(dados_descriptografados)
                    print(f"Arquivo descriptografado: {caminho}")
                except Exception as e:
                    print(f"Erro ao descriptografar {caminho}: {e}")

# Execução
if __name__ == "__main__":
    pasta_alvo = "/home/teste/documents"
    chave = carregar_chave()
    fernet = Fernet(chave)

    descriptografar_arquivos(pasta_alvo, fernet)
