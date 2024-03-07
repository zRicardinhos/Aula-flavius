import datetime


def main():
    data = datetime.date.today()

    year = data.year

    name = input("Informe seu nome : ")
    nasc = int(input("Informe seu ano de nascimento : "))

    idade = year - nasc

    print(f"{name} este ano vc completa {idade} anos")


if __name__ == "__main__":
    main()
    
