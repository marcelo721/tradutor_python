def main():
    i = 99
    for i in range(99, 0, -1):
        print("Há " + str(i) + " garrafas de cerveja na parede, " + str(i) + " garrafas de cerveja.")
        print("Pegar uma, passar para baixo, " + str(i - 1) + " garrafas de cerveja na parede.")
    
    print("Nenhuma garrafa de cerveja na parede, nenhuma garrafa de cerveja.")
    print("Vá ao bar e compre mais 99 garrafas de cerveja.")

if __name__ == '__main__':
    main()
