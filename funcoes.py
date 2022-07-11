def criar_backup(list_path):
    from datetime import datetime
    import tarfile, os, glob
    dir="/tmp/" # Onde o backup é salvo temporáriamente até que que seja enviado pra oci
    hash="d41d8cd98f00b204e9800998ecf8427e"  # Hash fixa inserida no dome de todos o backups

    data_hora = str(datetime.today())
    data_hora = data_hora.replace(":", "-")
    data_hora = data_hora.replace(" ", "-")
    #Apagando arquivo:
    excluir_file = glob.glob(f'{dir}/*{hash}*')
    for ex_file in excluir_file:
        os.remove(ex_file)

    #Gerando Novo Backup
    namefile = f"{dir}{data_hora}-hash{hash}.tar.gz"
    tar = tarfile.open(namefile, "w:gz")
    for name in list_path:
        print(namefile, name)
        tar.add(name)
    tar.close()
    return dir, namefile

def upload_to_bucket(path, name):
    import oci
    from oci.config import validate_config

    tenancyId = ""  # Your tenancies OCID.
    authUserId = ""  # The OCID of the user ID being used.
    OCI_KEY_PATH = ""  # Path of the key file.
    keyFingerprint = ""  # The fingerprint of the key file being used
    namespace = ""
    bucket_name = ""
    config = {
        "user": authUserId,
        "key_file": OCI_KEY_PATH,
        "fingerprint": keyFingerprint,
        "tenancy": tenancyId,
        "region": "sa-saopaulo-1"
    }
    # it validates the above fields for connection
    validate_config(config)
    filename=f"{name}"
    filename_buket= filename.replace(path, '')
    filename = filename.replace('//','/')
    with open(filename, "rb") as in_file:
        object_storage_client = oci.object_storage.ObjectStorageClient(config)
        object_storage_client.put_object(namespace, bucket_name,  f"backup-ubuntu/{filename_buket}", in_file)

def msg_telegram(mensagem):
    import telebot
    chave_api = ""
    bot = telebot.TeleBot(chave_api)
    bot.send_message("", mensagem)

def gerar_now():
    from datetime import datetime
    data_e_hora_atuais = datetime.now()
    data_e_hora = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
    return data_e_hora

def gerar_now_date():
    from datetime import datetime
    data_e_hora_atuais = datetime.now()
    data_e_hora = data_e_hora_atuais.strftime('%d-%m-%Y')
    return data_e_hora
