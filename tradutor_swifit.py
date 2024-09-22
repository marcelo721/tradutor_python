import os
import sys
import subprocess

def traduzir_linha_swifit(linha, nivel_indentacao, tipos_variaveis_swifit):
    comandos_swifit = {
        "Love Story": "if",
        "Bad Blood": "else",
        "You Belong With Me": "input",
        "Shake It Off": "print",
        "All Too Well": "for",
        "Folklore": "def",
        "sing": "range",
    }

    # Substitui comandos Swifit por Python
    for comando, traducao in comandos_swifit.items():
        linha = linha.replace(comando, traducao)

    # Ajusta para o comando All Too Well com range()
    if "All Too Well" in linha and "sing" in linha:
        partes = linha.split(" ")
        variavel = partes[2]  # Obtém a variável de iteração
        # Ajusta o restante da linha para o formato Python range(start, stop, step)
        resto_linha = " ".join(partes[3:]).replace("to", ",").replace(":", "")
        linha = f"for {variavel} in range({resto_linha}):"

    # Identifica o tipo da variável e ajusta o input
    for tipo_swifit, tipo_python in tipos_variaveis_swifit.items():
        if tipo_swifit in linha:
            linha = linha.replace(tipo_swifit, "")
            if "You Belong With Me" in linha:
                linha = linha.replace("You Belong With Me", f"{tipo_python}(input(")
                linha += "))"

    return linha

def verificar_tipo_variaveis(linhas, tipos_variaveis_swifit):
    tipos_definidos = set(tipos_variaveis_swifit.keys())
    # Verifica se há variáveis sem tipo definido
    for linha in linhas:
        for tipo in tipos_definidos:
            if tipo in linha:
                return True
    # Não há variáveis, então não há erro
    return False

def traduzir_arquivo_swifit(arquivo_entrada):
    tipos_variaveis_swifit = {
        "Fearless": "int",
        "Red": "float",
        "Evermore": "str",
    }

    arquivo_saida = os.path.splitext(arquivo_entrada)[0] + ".py"

    try:
        with open(arquivo_entrada, 'r') as entrada:
            linhas = entrada.readlines()
    except FileNotFoundError:
        print(f"Arquivo '{arquivo_entrada}' não encontrado.")
        return

    if verificar_tipo_variaveis(linhas, tipos_variaveis_swifit) and not any(tipo in linha for tipo in tipos_variaveis_swifit.keys() for linha in linhas):
        print("Erro: As variáveis não têm um tipo definido.")
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
                saida.write('    ' * nivel_indentacao + traduzir_linha_swifit(linha[:-1], nivel_indentacao, tipos_variaveis_swifit) + ':\n')
                nivel_indentacao += 1
                dentro_funcao = linha.startswith("def ")

            else:
                linha_traduzida = traduzir_linha_swifit(linha, nivel_indentacao, tipos_variaveis_swifit).lstrip()

                # Adiciona a indentação correta se necessário
                if nivel_indentacao > 0:
                    linha_traduzida = '    ' * nivel_indentacao + linha_traduzida
                
                saida.write(linha_traduzida + '\n')

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
