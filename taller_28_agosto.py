 #-----------------------------------EJERCICIO NUMERO 1--------------------------------------------------
""" numero = [1,2,3,4,8,5,9,10] 
#recorrer y mostrar la lista

for num in numero:
    print(f"numero:{num}")

#Ordenarla y mostrarla
numero.sort()
for num in numero:
    print(f"numero:{num}") 

 #longitud de la lista
print("El número de elementos de la lista es", len(numero)) 

 #buscar un elemento por teclado
num =int(input("ingrese numero a buscar"))
if num in numero: 
    print(f"El número {num} existe en la lista")
else:
    print(f"no se encuentra el numero{num}")  """



 #--------------------EJERCICIO NUMERO 2, AÑDIR VALORES MIENTRAS SU LONGITUD SEA MNOR A 120--------------------------

""" valores=[]

while len(valores) <= 120 :
    valor=int(input("Ingrese un numero:"))
    valores.append(valor)

#imprimimos la lista    
print(f"la lista ingresada es: {valores}")  """

 #-------------------------EJERCICIO NUMERO 3, COMPROBAR SI LA VARIABLE ESTA VACIA-------------------------------

""" prueba=input("ingrese algo o solo de enter")
if len(prueba)==0:
    prueba=input("la variable no tiene datos, ingrese datos a la variable en minuscula")
    final = prueba.upper()
    print(final)
else:
    print("la variable tiene datos")  """


#---------------------------------------------EJERCICIO NUMERO 4-----------------------------------------------------
""" variada = [[2,4],"algo",True,2]



def tipo_dato(x, y, z, o):
    for num in variada:
        if type(num)==list:
            print(f"la variable: {num} es de tipo de dato: {type(num)}")
        elif type(num)==str:
            print(f"la variable: {num} es de tipo de dato: {type(num)}")
        elif type(num)==int:
            print(f"la variable: {num} es de tipo de dato: {type(num)}")
        elif type(num)==int:

            print(f"la variable: {num} es de tipo de dato: {type(num)}")
        elif type(num)==bool:
            
            print(f"la variable: {num} es de tipo de dato: {type(num)}")
        
print(tipo_dato([2,4],"string",2,True))
 """


 #------------------------------------------EJERCICIO 5-----------------------------------------------------------

""" peliculas = [
    {
        "categoria": "ACCION",
        "juegos":["GTA","COD","PUGB"]
    }, 
    {
        "categoria": "AVENTURA",
        "juegos":["ASSINS","CRASH","Prince of persia"]
    },
    {
        "categoria": "DEPORTES",
        "juegos":["FIFA 21",
        "PRO 21","MOTO GP 21"]
    }

]






for contacto in peliculas:
    print(f"CATEGORIA: {contacto['categoria']}")
    print(f"{contacto['juegos']}")  """


#---------------------------------------EJERCICIO 6--------------------------------------------------
""" contactos = [
    {
        'nombre':'antonio',
        'cedula':106180,
        'carrera':'fisica'
    },
    {
        'nombre':'santiago',
        'cedula':54852,
        'carrera':'sistemas'
    },
    {
        'nombre':'raul',
        'cedula':55325,
        'carrera':'electronica'
    }
]

opcion=int(input("ingrese una opcion pa editar: 1.nombre 2.cedula 3.carrera"))

    

def modificarNombre(nom, nuevo):

    for contacto in contactos:

        if contacto == nom:

            contacto[contacto] = nuevo """