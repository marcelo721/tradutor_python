# Experimental Virtual Interpreter for Lightweight Algorithmic Scripting and Integrated Operations (taylorSwift)



## Índice

- [Visão Geral](#visão-geral)
- [Instalação](#instalação)
- [Sintaxe](#sintaxe)
  - [Declarações de Variáveis](#1-declarações-de-variáveis)
  - [Instruções de Impressão](#2-instruções-de-impressão)
  - [Estruturas de Controle](#3-estruturas-de-controle)
    - [3.1 Instruções If](#31-instruções-if)
    - [3.2 Instruções Else](#32-instruções-else)
  - [Chaves](#4-chaves)
  - [Operadores](#5-operadores)
- [Exemplo de Programa](#exemplo-de-programa)
- [Conclusão](#conclusão)

## Visão Geral
Swifit é uma linguagem esotérica inspirada na discografia da cantora Taylor Swift. Com comandos baseados nos nomes de suas músicas, a linguagem foi criada para ser uma maneira lúdica e divertida de programar. Esta documentação detalha a sintaxe, comandos e estruturas da linguagem, além de fornecer exemplos práticos de uso

## Instalação

Para usar taylorSwifit, você precisa do Python instalado em seu computador. Clone este repositório e execute o arquivo `executar.py` para traduzir seus arquivos `.swifit` para python.

```bash
git clone https://github.com/seu-usuario/Evi-Lasio.git
cd "taylorSwifit"
python executar.py nome_so_arquivo.swifit
```

## Sintaxe

### 1. Declarações de Variáveis

Em Swifit, os tipos de variáveis são nomeados com base nos albuns da Taylor
Swift, Tipos de Variáveis:
• Fearless: Número inteiro (equivalente a int).
• Red: Número de ponto flutuante (equivalente a float).
• Evermore: String (equivalente a str).

**Sintaxe:**
```
tipo_variavel nome_variavel_valor record valor
```

**Exemplo:**
```
F e a r l e s s numero1 = 10
Red p r e co = 19.99
```

**Tradução para python:**
```python
numero1 = 10
p r eco = 19.99
nome = ” Taylor Swift ”;
```

### 2. Instruções de Impressão

em swifit, O comando Shake It Off imprime mensagens na tela.

**Sintaxe:**
```
Shake I t Off (” msg” )

```

**Exemplo:**
```
Shake I t Off (”olá mundo” )

```

**Tradução para python:**
print( ” Olá, mundo ! ” )
```

### 3. Estruturas de Controle

#### 3.1 Instruções If

Use a palavra-chave Love Story para criar uma instrução if. A condição usa o operador equalizer para verificações de igualdade.

**Sintaxe:**
```
Love Story ( a  e q u a l i z e r  b ) <
// comandos
>


```

**Exemplo:**
```
Love Story ( numero1 Kanye 10 ) <
Shake I t Off (”o numero é menor ou igual a 10 . ” )
>

```

**Tradução para python:**
```python
if numero1 <= 1 0:
    print ( ”O n m e r o menor ou i g u a l a 1 0. ” )
```

#### 3.2 Instruções Else

Use a palavra-chave Bad Blood para criar uma instrução else.

**Sintaxe:**
```
Love Story ( a   e q u a l i z e r   b ) <
// comandos
>
Bad Blood <
// comandos
>
```

**Exemplo:**
```
Love S to r y ( numero1 Kanye 10 ) <
Shake I t Off (”o número ´emenor ou igual a 10” )
>
Bad Blood <
Shake I t Off (” o numero é maior que 10 ” )
>
```

**Tradução para python:**
```python
if numero1 <= 1 0:
    print ( ”o número ´emenor ou igual a 10 ” )
else :
    print ( ”o numero é maior que 10 ” )
```


### 4. Chaves

Use os símbolos `>` e `<` para indicar o início e o fim de um bloco de código.

**Exemplo:**
```
>
    // código aqui
<
```

**Tradução para python:**
```python
// python usa identação para definir blocos de codigo 
```

### 5. Operadores

Taylor Swifit suporta os seguintes operadores:
• record: =
• equalizer: ==
• feat: +
• amplify: *
• mute: -
• harmonize: /
• Kanye: <=
• West: >=



## Exemplo de Programa

Aqui está um exemplo completo que demonstra vários recursos de taylor Swift:

```plaintext
taylorSwifit<
    Fearless i record 99
    All Too Well i in sing(99, 0, -1)<
        Shake It Off("Há " feat str(i) feat " garrafas de cerveja na parede, " feat str(i) feat " garrafas de cerveja.")
        Shake It Off("Pegar uma, passar para baixo, " feat str(i mute 1) feat " garrafas de cerveja na parede.")
    >

    Shake It Off("Nenhuma garrafa de cerveja na parede, nenhuma garrafa de cerveja.")
    Shake It Off("Vá ao bar e compre mais 99 garrafas de cerveja.")
>

```

**Tradução para python:**
```python
def main():
    i = 99
    for i in range(99, 0, -1):
        print("Há " + str(i) + " garrafas de cerveja na parede, " + str(i) + " garrafas de cerveja.")
        print("Pegar uma, passar para baixo, " + str(i - 1) + " garrafas de cerveja na parede.")
    
    print("Nenhuma garrafa de cerveja na parede, nenhuma garrafa de cerveja.")
    print("Vá ao bar e compre mais 99 garrafas de cerveja.")

if __name__ == '__main__':
    main()

```

## Conclusão

a linguagem foi criada para ser uma maneira lúdica e divertida de programar sem fins lucrativos(e também para não reprovar na disciplina).
