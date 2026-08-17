import os
os.system("cls")

# Actividad: Sistema de reservas del Hotel Sol
# Debes crear un programa en Python que calcule el precio final de una reserva en un hotel.
# Enunciado
# El Hotel Sol tiene las siguientes tarifas:
# •	Habitación individual: $40.000 por noche.
# •	Habitación doble: $65.000 por noche.
# •	Habitación suite: $100.000 por noche.
# El cliente debe ingresar:
# 1.	Su nombre.
# 2.	El tipo de habitación (individual, doble o suite).
# 3.	La cantidad de noches.
# 4.	Su edad.
# 5.	Consultar si es miembro del hotel.
#DECLARO MIS CONSTANTES CON LOS VALORES DE LA TARIFA X HABITACION
INDIVIDUAL = 40000
DOBLE = 65000
SUITE = 100000
#SOLICITO TODOS LOS DATOS AL USUARIO
nombre = input("Ingrese su nombre\n")
tipo_habitacion = int(input("Ingrese tipo de habitacion.  1) individual  2) doble   3) suite\n"))
cantidad_noche = int(input("Ingrese cantidad de noches\n"))
edad = int(input("Ingrese su edad\n"))
es_miembro = input("Es miembro del hotel? si - no\n")
if tipo_habitacion == 1:
    habitacion = INDIVIDUAL
elif tipo_habitacion == 2:
    habitacion = DOBLE
elif tipo_habitacion == 3:
    habitacion = SUITE
else:
    habitacion = 0

valor_inicial = habitacion * cantidad_noche
if edad > 0 and edad < 18:
    descuento = 0.90
    porcentaje_edad = 10
elif edad >= 65:
    descuento = 0.85
    porcentaje_edad = 15
else:
    descuento = 1
    porcentaje_edad = 0
valor_provisorio = valor_inicial* descuento
# •	Si es miembro del hotel, recibe un 10% de descuento adicional.
if  es_miembro == "si":
    valor_precio_miembro = valor_provisorio * 0.90
else:
    valor_precio_miembro = valor_provisorio * 1
# •	Si la estadía es de 7 noches o más, recibe un 5% de descuento adicional.
if cantidad_noche >= 7:
    valor_precio_noche = valor_precio_miembro * 0.95
    porcentaje_miembro = 5 
else:
    valor_precio_noche = valor_precio_miembro * 1
    porcentaje_miembro = 0
print(f"precio inicial : ${valor_inicial}")
print(f"descuento edad: {porcentaje_edad}%")
print(f"precio: ${valor_provisorio}")
print(f"descuento del {porcentaje_miembro}%")
print(f"precio: $ {valor_precio_miembro}")
print(f"descuento por noche ")
print(f"precio: $ {valor_precio_noche}")









