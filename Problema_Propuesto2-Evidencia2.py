class Triangulo:
    def inicializar(self):
        self.lado1 = int(input("Ingrese primer lado: "))
        self.lado2 = int(input("Ingrese segundo lado: "))
        self.lado3 = int(input("Ingrese tercer lado: "))

    def imprimir(self):
        print("Lado1:", self.lado1)
        print("Lado2:", self.lado2)
        print("Lado3:", self.lado3)

    def lado_mayor(self):
        print("Lado mayor:")
        if self.lado1 > self.lado2 and self.lado1 > self.lado3:
            print(self.lado1)
        else:
            if self.lado2 > self.lado3:
                print(self.lado2)
            else:
                print(self.lado3)

    def es_equilatero(self):
        if self.lado1 == self.lado2 and self.lado1 == self.lado3:
            print("El triángulo es equilátero")
        else:
            print("El triángulo no es equilátero")


# bloque principal
triangulo1 = Triangulo()
triangulo1.inicializar()
triangulo1.imprimir()
triangulo1.lado_mayor()
triangulo1.es_equilatero()
