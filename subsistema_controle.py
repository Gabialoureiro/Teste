import matplotlib
from time import sleep
from usina import Usina
from leitordosensor import leitor_sensor
from controlador import Controlador
usina1=Usina(249)
leitor_sensor1=leitor_sensor(usina1)
controlador1=Controlador(leitor_sensor1,usina1)
class subsistema:
     
    def __init__ (self, sensor, controlador,usina):
        usina=Usina()
        sensor=leitor_sensor(usina)
        controlador=Controlador(sensor,usina)
        self.usina=usina
        self.sensor=sensor
        self.controlador=controlador
        self.leituras=[]
    def passa_dados(self):
        leitura=self.sensor.armazena_dado()
        while leitura>191.25:
            leitura=self.sensor.armazena_dado()
            self.controlador.abrir_comportas
            self.leituras.append(leitura)
        fig . ax=plt.subplots()
        x=np.linspace(0,2000,20000)
        y=np.self.leituras

subsistema1=subsistema(leitor_sensor1,controlador1,usina1)
subsistema1.passa_dados()



    

        
    