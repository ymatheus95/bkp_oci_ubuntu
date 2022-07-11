from funcoes import *
#Diretórios e aquivos que devem ser backapiados:
diretorios_backups = ['/etc/','/home/matheus/Documents/']

#Cria os backups e retorna o nome do arquivo tar com todos os diretórios inclusos
diretorio, name = criar_backup(diretorios_backups)

diretorio_msg = ', '.join(diretorios_backups)  # Transforma a lista em texto para o envios das mensagens do telegram e a geração dos backups

# Diretórios onde os logs são salvos
path_log = "/var/log/backup_oci"

try:
    upload_to_bucket(diretorio, name)
    msg_telegram(f"{gerar_now()}\nBackup dos diretório {diretorio_msg}, realizados com sucesso.")
    with open(f"{path_log}/{gerar_now_date()}.txt", "a") as file_log:
        file_log.write(f"\n{gerar_now()} - "
                       f"Backup dos diretórios abaixo foram realizado com sucesso: "
                       f"{diretorio_msg}")

except Exception as erro:
    print(erro)
    msg_telegram(f"{gerar_now()} Falha ao realizar o backup dos diretório: \n{diretorio}"
                 f"{diretorio_msg}.\nDetalhe do erro: \n{erro}")
    with open(f"{path_log}/{gerar_now_date()}.txt", "a") as file_log:
        file_log.write(f"\n{gerar_now()} - "
                       f"Falha ao realizar o backup dos seguintes diretórios: "
                       f"{diretorio_msg}")
