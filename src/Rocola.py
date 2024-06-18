from diseñoObserver.Observer import Observer
from src.Potenciador import Potenciador

class Rocola(Observer):
    def __init__(self, musica1, musica2, musicapot):
        self.duracionMusica = 1800
        self.duracionActual = self.duracionMusica
        self.currentMusic = 1
        self.musica_fondo1 = musica1
        self.musica_fondo2 = musica2
        self.musica_potenciador = musicapot
        self.musica_fondo1.play(-1)

    # Va rotando la música de fondo
    def tiempoMusica(self):
        if not self.duracionActual:  # Si el tiempo esta en 0
            self.duracionActual = self.duracionMusica
            if self.currentMusic == 1:
                self.musica_fondo1.stop()
                self.musica_fondo2.play(-1)
                self.currentMusic = 2
            else:
                self.musica_fondo2.stop()
                self.musica_fondo1.play(-1)
                self.currentMusic = 1
        else:
            self.decTimeMusic()

    def decTimeMusic(self):
        self.duracionActual -=1

    def update(self, sujeto):
        # Chequeamos que el Sujeto sea un Potenciador, porque podemos estar observando otros Sujetos
        if isinstance(sujeto, Potenciador):
            if sujeto.isActive:
                if self.currentMusic == 1:
                    self.musica_fondo1.stop()
                    self.musica_potenciador.play(-1)
                else:
                    self.musica_fondo2.stop()
                    self.musica_potenciador.play(-1)
            else:
                if self.currentMusic == 1:
                    self.musica_potenciador.stop()
                    self.musica_fondo1.play(-1)
                else:
                    self.musica_potenciador.stop()
                    self.musica_fondo2.play(-1)