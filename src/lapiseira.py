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
        if self.grafiteDentro:
            self.grafiteDentro = []
            return True
        else:
            return False

    def escrever(self, folhas: int):
        if self.getGrafite() is not None:
            grafite = self.grafiteDentro[0]
            if grafite.tamanho > 0:
                folhaspossiveis = grafite.tamanho // grafite.desgastePorFolha()
                folhasescritas = min(folhas, folhaspossiveis)
                grafite.tamanho -= folhasescritas * grafite.desgastePorFolha()
                self.folhasEscritas += folhasescritas
                if grafite.tamanho == 0:
                    self.grafiteDentro.pop()
                if folhaspossiveis != folhas:
                    return False
                return True
        return False


    def getGrafite(self):
        if len(self.grafiteDentro) != 0:
            grafite = self.grafiteDentro[0].getCalibre()
            return grafite
        else:
            return None

    def getCalibre(self):
        return self.calibre

    def getFolhasEscritas(self):
        return self.folhasEscritas