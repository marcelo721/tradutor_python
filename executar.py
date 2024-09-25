import os
import subprocess
import sys

from tradutor_swifit import traduzir_arquivo_swifit  # Importa a função do tradutor


def executar_codigo_python(arquivo_python):
    try:
        subprocess.run(["python", arquivo_python], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar {arquivo_python}: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Por favor, forneça o nome do arquivo .swifit para traduzir e executar.")
    else:
        arquivo_swifit = sys.argv[1]

        if not arquivo_swifit.endswith(".swifit"):
            print("O arquivo deve ter a extensão .swifit")
        else:
            arquivo_python = traduzir_arquivo_swifit(arquivo_swifit)
            if arquivo_python:
                executar_codigo_python(arquivo_python)
