import time
import datetime
import pygame

def ativar_alarme(tempo_alarme):
    print (f"Alarme ativado para {tempo_alarme}")
    despertador = "Panoramic Arrival - Asher Fulero.mp3"
    ativado = True
    

    while ativado:
        agora = datetime.datetime.now()
        agora = agora.strftime("%H:%M:%S")
        print (agora)
        time.sleep(1)

        if agora == tempo_alarme:
            pygame.mixer.init()
            pygame.mixer.music.load(despertador)
            pygame.mixer.music.play()
            print("-" * 5 + "Hora de acordar" + "-" * 5)

            while pygame.mixer.music.get_busy():
                time.sleep(1)
        
            ativado = False

if __name__ == "__main__":
    tempo_alarme = input("Coloque o tempo que deseja para o seu alarme Hora:Minuto:Segundo ")
    ativar_alarme(tempo_alarme)