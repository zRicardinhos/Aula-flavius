def main():
    distancia = float(input("Qual foi a distancia percorrida ? "))
    tempo_em_minutos = float(input("Digite o tempo em minutos "))
    tempo_em_horas = tempo_em_minutos / 60

    velocidade_media_km = distancia / tempo_em_horas
    velocidade_media_ms = velocidade_media_km * 0.278

    print(f"Velocidade media em KM/h : {velocidade_media_km:.2f}Km/h")

    print(f"Velocidade media em M/s : {velocidade_media_ms:.2f}M/s")


if __name__ == "__main__":
    main()
