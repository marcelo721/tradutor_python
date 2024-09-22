import os
import sys
import subprocess

def traduzir_linha_swifit(linha, nivel_indentacao):
    comandos_swifit = {
        "Love Story": "if",
        "Bad Blood": "else",
        "You Belong With Me": "input",
        "Shake It Off": "print",
        "All Too Well": "for",  
        "Folklore": "def",      
    }

    tipos_variaveis_swifit = {
        "Fearless": "",  # int
        "Red": "",       # float
        "Evermore": "",  # string
    }

    for comando, traducao in comandos_swifit.items():
        linha = linha.replace(comando, traducao)

    for tipo_swifit in tipos_variaveis_swifit:
        if tipo_swifit in linha:
            linha = linha.replace(tipo_swifit, "")

    return linha

def traduzir_arquivo_swifit(arquivo_entrada):
    # Obter o nome do arquivo de saída, apenas trocando a extensão para .py
    arquivo_saida = os.path.splitext(arquivo_entrada)[0] + ".py"

    try:
        with open(arquivo_entrada, 'r') as entrada:
            linhas = entrada.readlines()
    except FileNotFoundError:
        print(f"Arquivo '{arquivo_entrada}' não encontrado.")
        return

    with open(arquivo_saida, 'w') as saida:
        nivel_indentacao = 0
        dentro_taylor_swifit = False
        dentro_funcao = False

        for linha in linhas:
            linha = linha.strip()

            if linha.startswith("taylorSwifit{"):
                saida.write("def main():\n")
                nivel_indentacao += 1
                dentro_taylor_swifit = True
                dentro_funcao = False

            elif linha == "}":
                nivel_indentacao -= 1
                if dentro_funcao:
                    dentro_funcao = False
                elif dentro_taylor_swifit:
                    dentro_taylor_swifit = False

            elif linha.endswith("{"):
                saida.write('    ' * nivel_indentacao + traduzir_linha_swifit(linha[:-1], nivel_indentacao) + ':\n')
                nivel_indentacao += 1
                dentro_funcao = linha.startswith("def ")

            else:
                linha_traduzida = traduzir_linha_swifit(linha, nivel_indentacao).lstrip()
                saida.write('    ' * nivel_indentacao + linha_traduzida + '\n')

        saida.write("\nif __name__ == '__main__':\n")
        saida.write('    main()\n')

    print(f"Tradução concluída. Arquivo salvo como {arquivo_saida}")
    return arquivo_saida

def executar_codigo_python(arquivo_python):
    try:
        subprocess.run(["python", arquivo_python], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar {arquivo_python}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Por favor, forneça o nome do arquivo .swifit para traduzir.")
    else:
        arquivo_swifit = sys.argv[1]

        if not arquivo_swifit.endswith(".swifit"):
            print("O arquivo deve ter a extensão .swifit")
        else:
            arquivo_python = traduzir_arquivo_swifit(arquivo_swifit)
            if arquivo_python:
                executar_codigo_python(arquivo_python)
