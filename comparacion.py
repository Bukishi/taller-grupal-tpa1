class Medida:
    def init(self, nombre_medida, valor_medida, valor_equivalente):
        self.nombre_medida = nombre_medida
        self.valor_medida = valor_medida
        self.valor_equivalente = valor_equivalente

    def calcular_valor_equivalente(self):
        return self.valor_medida / self.valor_equivalente

    def convertir_a_barriles(litros):
        return litros / 100

    def comparar(self, otra_medida):
        if self.valor_medida > otra_medida.valor_medida:
            return 'mayor'
        elif self.valor_medida < otra_medida.valor_medida:
            return 'menor'
        else:
            return 'igual'
medida1 = Medida('Longitud', 10, 1) 
medida2 = Medida()
resultado = medida1.comparar(medida2)

print(resultado)