from src.grafite import Grafite


class Lapiseira:

    def __init__(self, calibre:float):
        self.calibre = calibre
        self.folhasEscritas = 0
        self.grafiteDentro = []

    def inserir (self, grafite: Grafite):
        if self.calibre == grafite.getCalibre():
            if len(self.grafiteDentro) == 0:
                self.grafiteDentro.append(grafite)
                self.folhasEscritas = 0
                return True
            return False
        return False

    def remover(self):
        if self.grafiteDentro != []:
            self.grafiteDentro.pop()
            return False
        else:
            return True

    def escrever(self, folhas: int):
        return False

    def getGrafite(self):
        if len(self.grafiteDentro) > 0:
            return self.grafiteDentro
        else:
            return None

    def getCalibre(self):
        return self.calibre

    def getFolhasEscritas(self):
        return self.folhasEscritas