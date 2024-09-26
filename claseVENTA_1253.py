# Zona clase
class Venta1253:
    idVenta1253 = 0
    numCaja1253 = 0
    vendedor1253 = ""
    descuentoVenta1253 = 0.00
    totalVenta1253 = 0.00
    fechadeVenta1253 = ""
    reciboVenta1253 = ""
# Zona de funciones
    def mostrarDatos1253(self):
        print(f"Id: {vent1253.idVenta1253 }")
        print(f"Num.Caja: {vent1253.numCaja1253}")
        print(f"Vendedor: {vent1253.vendedor1253}")
        print(f"Total: {vent1253.totalVenta1253}")
        print(f"Fecha: {vent1253.fechadeVenta1253}")
        print(f"Recibo: {vent1253.reciboVenta1253}")
    def listaVenta1253(self):
        lisV1253 = ["Venta1: Peluche_Eiden", "Venta2: Peluche_Morvay", 
                    "Venta3: Peluche_Aster", "Venta4: Peluche_Yakumo", 
                    "Venta5: Peluche_Edmond","Venta6: Peluche_Olivine",
                    "Venta7: Peluche_Quincy"]
        print(lisV1253)
        for i in lisV1253:
            print("-", i)
    def tuplaVenta1253(self):
        tupV1253 = ("Venta8: Peluche_Kuya", "Venta9: Peluche_Garuu",
                    "Venta10: Peluche_Blade", "Venta11: Peluche_Karuu", 
                    "Venta12: Peluche_Dante","Venta13: Peluche_Jasson", 
                    "Venta13: Peluche_Guardia")
        print(tupV1253)
        for j in tupV1253:
            print("-", j)
    def diccionarioVenta1253(self):
        diccV1253 = {
            "id_Venta7:" : 50212,
            "Num.Caja:" : 5,
            "Vendedor_Venta7:" : "Alfonso Rojas",
            "Descuento $" : 12.5,
            "Total_Venta7:" : 50.80,
            "Fecha_Venta7:" : "19/07/2027", 
            "Recibo_Venta7" : "Pago: $100.00, Cambio: $38.73"
        }
        print(diccV1253)
        for maldonado , rodriguez in diccV1253.items():
            print("-", maldonado , rodriguez)
    def alta1253(self):
        print("Los datos se han completado...")
    def baja1253(self):
        print("Los datos se hab guardado con exito ☺")

# Creacion de objeto
vent1253 = Venta1253()

# Zona uso de objeto
vent1253.idVenta1253 = 1750
vent1253.numCaja1253 = 5
vent1253.vendedor1253 = "Valentina Maldonado"
vent1253.descuentoVenta1253 = 12.08
vent1253.totalVenta1253 = 89.78
vent1253.fechadeVenta1253 = "26/09/2024"
vent1253.reciboVenta1253 = "Pago: $70.00, Cambio: $1.83"
print("Datos")
vent1253.mostrarDatos1253()
print("Lista")
vent1253.listaVenta1253()
print("Tupla")
vent1253.tuplaVenta1253()
print("Diccionario")
vent1253.diccionarioVenta1253()
vent1253.alta1253()
vent1253.baja1253()







