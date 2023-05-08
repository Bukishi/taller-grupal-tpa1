class Medida:
    def __init__(self, nombre_medida, valor_medida, valor_equivalente):
        self.nombre_medida = nombre_medida
        self.valor_medida = valor_medida
        self.valor_equivalente = valor_equivalente

    def valor_Equivalente(valor_medida, valor_equivalente):
        return valor_medida/valor_equivalente
    
    def comparacion(barril, onza):
        litro_a_onza = 33.81
        litro_a_barril = 0.01
    
        if litro_a_barril*barril > litro_a_onza*onza:
            return "Hay mas barriles que onzas"
        
        elif litro_a_barril*barril < litro_a_onza*onza:
            return "Hay mas onzas que barriles"
        
        elif litro_a_barril*barril == litro_a_onza*onza:
            return "Hay la misma cantidad de barriles y onzas"
    
print(Medida.comparacion(100,20))