traducciones =["Hello","Dog","Red","Green","Blue","Backpack","Table","Cat","Bird","Chicken","Fried","But","Car","Train","Motorcycle"]
traducciones2=["Hola","Perro","Rojo","Verde","Azul","Mochila","Mesa","Gato","Pajaro","Pollo","Frito","Pero","Coche","Tren","Motocicleta"]

def funcion():
        opc=int(input("----MENU----\n1.-Mostrar tabla de traducciones.\n2.-Introducir palabra que desea traducir.\nIntroduzca su opcion: "))
        if (opc==2):
                palabra=input("Introduzca la palabra que desea traducir: ")
                i=0
                for palabra_s,palabra_e in zip(traducciones2,traducciones):
                        if(palabra==palabra_s):
                                print("La traduccion de la palabra es: ",palabra_e)
                                i=1
                                opc=0
                        elif(palabra==palabra_e):
                                print("La traduccion de la palabra es: ",palabra_s)
                                i=1
                                opc=0
                if(i!=1):
                        print("La palabra introducida no es reconocida en el diccionario.")
                        add=input("¿Desea agregarla al diccionario?[S/N]: ")
                        if(add=="S" or add=="s"):
                                type=input("¿Su palabra esta en Ingles o Espanol?: ")
                                if(type=="Espanol" or type=="espanol"):
                                        traducciones2.append(palabra)
                                        trad=input("Introduzca su traduccion: ")
                                        traducciones.append(trad)
                                        print("---Agregado con exito.---")
                                        print("---TABLA DE TRADUCCIONES ACTUALIZADA---")
                                        for palabra_s,palabra_e in zip(traducciones2, traducciones):
                                                print(palabra_s,"-",palabra_e)
                                                opc=0
                                if(type=="Ingles" or type=="ingles"):
                                        traducciones.append(palabra)
                                        trad=input("Introduzca su traduccion: ")
                                        traducciones2.append(trad)
                                        print("---Agregado con exito.---")
                                        print("---TABLA DE TRADUCCIONES ACTUALIZADA---")
                                        for palabra_s,palabra_e in zip(traducciones2, traducciones):
                                                print(palabra_s,"-",palabra_e)
                                                opc=0
                        else:
                                init=1
        elif(opc==1):
                print("---TABLA DE TRADUCCIONES---")
                for palabra_s,palabra_e in zip(traducciones2, traducciones):
                        print(palabra_s,"-",palabra_e)
                opc=0

init=int(input("---BIENVENIDO---\n1.-Iniciar programa.\n2.-Salir\nEliga su opcion: "))
while init==1:
        funcion()
        init=int(input("1.-Iniciar nuevamente el programa.\n2.-Salir\nEliga su opcion: "))