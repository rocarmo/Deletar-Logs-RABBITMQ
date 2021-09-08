import os
from dotenv import load_dotenv

load_dotenv()


def check_file():     # Função criada para verificar o arquivo ofensor
    target_file_raw = os.getenv('target_file')
    target_file = target_file_raw
    # target_file = "C:\Users\rocarmo\Documents\Win10_21H1_BrazilianPortuguese_x64.iso"

    print(os.path.getsize("r" + target_file))
    # print(os.path.getsize(target_file))

