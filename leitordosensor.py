from time import sleep
from usina import Usina
class leitor_sensor:
    def __init__ (self,usina):
        self.leitura=0
        self.usina=usina
    def armazena_dado(self):
        sleep(0.1)
        self.leitura=self.usina.get_sensor()
        return self.leitura
        


