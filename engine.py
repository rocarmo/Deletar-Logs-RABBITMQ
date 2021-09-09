import os
from dotenv import load_dotenv
from Logs.Logger import log
load_dotenv()


def delete_file():
    log.info("[!] - Iniciando limpeza de arquivo LOG RabbitMQ")

    try:
        target_file = os.getenv('target_file')[1:].strip('"')

        log.info("[+] - Caminho do arquivo para exclusão encontrado.")
        log.info("[!] - Excluindo arquivo...")

        os.remove(target_file)

        log.info("[+] - Arquivo excluido com sucesso!")
        log.info("---------------------------------------------------\n")

    except Exception as del_file_error:
        log.info('[X] - Erro ao tentar remover o arquivo ou o arquivo não foi encontrado.')
        log.info(del_file_error)
        log.info("---------------------------------------------------\n")


