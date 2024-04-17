def main():
    print(""""

 __ __  ____   ____    ____      ___ ___   ____  ______    ___  ____   ____   ____      _____   ____  __ __   ___   ____   ____  ______   ____ 
|  |  ||    \ |    \  /    |    |   |   | /    ||      |  /  _]|    \ |    | /    |    |     | /    ||  |  | /   \ |    \ |    ||      | /    |
|  |  ||  D  )|  _  ||  o  |    | _   _ ||  o  ||      | /  [_ |  D  ) |  | |  o  |    |   __||  o  ||  |  ||     ||  D  ) |  | |      ||  o  |
|  |  ||    / |  |  ||     |    |  \_/  ||     ||_|  |_||    _]|    /  |  | |     |    |  |_  |     ||  |  ||  O  ||    /  |  | |_|  |_||     |
|  :  ||    \ |  |  ||  _  |    |   |   ||  _  |  |  |  |   [_ |    \  |  | |  _  |    |   _] |  _  ||  :  ||     ||    \  |  |   |  |  |  _  |
|     ||  .  \|  |  ||  |  |    |   |   ||  |  |  |  |  |     ||  .  \ |  | |  |  |    |  |   |  |  | \   / |     ||  .  \ |  |   |  |  |  |  |
 \__,_||__|\_||__|__||__|__|    |___|___||__|__|  |__|  |_____||__|\_||____||__|__|    |__|   |__|__|  \_/   \___/ |__|\_||____|  |__|  |__|__|
                                                                                                                                               

""")

    materias = {
        "1" : "ALGORITMOS E LÓGICA DE PROGRAMAÇÃO",
        "2" : "FUNDAMENTOS DE MATEMÁTICA",
        "3" : "INTRODUÇÃO À INFORMÁTICA",
        "4" : "LÓGICA",
        "5" : "TEORIA GERAL DA ADMINISTRAÇÃO",
        "6" : "NENHUM",
        "0" : "SAIR/TERMINAR VOTACAO"
    }
    print("Opcoes disponiveis: \n")
    for materia in materias:
        print(materia, materias[materia])
    print()
    cand_1 = 0
    cand_2 = 0
    cand_3 = 0
    cand_4 = 0
    cand_5 = 0
    cand_6 = 0
    while True:
        voto = input("ESCOLHA UMA OPCAO VALIDA\n")
        while voto not in materias:
            print("OPCAO INVALIDA, VEJA AS OPCOES DISPONIVEIS\n")
            for materia in materias:
                print(materia, materias[materia])
            voto = input("ESCOLHA UMA OPCAO VALIDA\n")
        match voto:
            case "1":
                cand_1 += 1
            case "2":
                cand_2 += 1
            case "3":
                cand_3 += 1
            case "4":
                cand_4 += 1
            case "5":
                cand_5 += 1
            case "6":
                cand_6 += 1
            case "0":
                break 
    lista = [cand_1,cand_2,cand_3,cand_4,cand_5,cand_6]
    total = cand_1 + cand_2 + cand_3 + cand_4 + cand_5 + cand_6
    lista.sort(reverse=True)
    print(lista)

if __name__ == "__main__":
    main()
        
