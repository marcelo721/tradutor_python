def menu():
    print("Bem vindo a Swifit Calculator <3")
    print("1 - Fibonacci")
    print("2 - Fatorial")
    opc = int(input("Escolha a operação: "))
    n = int(input("Digite um número: "))
    
    if(opc == 1):
        print(fibonacci(n))
    elif(opc == 2):
        print(fatorial(n))
    else:
        print("Opção Inválida!!!")

def fibonacci( n):
    if(n == 0) :
        return 0
    if(n <= 2) :
        return 1
    else :
        return fibonacci(n - 1) + fibonacci(n - 2)

def fatorial( n):
    if(n <= 1) :
        return 1
    else :
        return n * fatorial(n - 1)

def main():
    menu()

if __name__ == '__main__':
    main()
