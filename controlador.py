from time import sleep
from usina import Usina
from leitordosensor import leitor_sensor
class Controlador:
    def __init__ (self,sensor,usina):
        self.sensor=sensor
        self.usina=usina
    def abrir_comportas (self):
        if self.sensor.armazena_dado(usina)>191.25:
            usina.set_actuator(True)
        else:
            usina.set_actuator(False)
