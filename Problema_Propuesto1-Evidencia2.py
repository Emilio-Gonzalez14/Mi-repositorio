class Joven:

 def inicializar (self,nombre,edad):
    self.nombre=nombre
    self.edad=edad

 def imprimir(self):
   print("Nombre",self.nombre)
   print("Edad",self.edad)

 def mayor_edad(self):
   if self.edad>=18:
     print("Es mayor de edad")
   else:
     print("No es mayor de edad")

#Bloque principal
joven1=Joven()
joven1.inicializar("Emilio",18)
joven1.imprimir()
joven1.mayor_edad()


    