opc=int(input("----MENU----\n1.-Mostrar tabla de traducciones.\n2.-Introducir palabra que desea traducir.\nIntroduzca su opcion: "))

traducciones =["Hello","Dog","Red","Green","Blue","Backpack","Table","Cat","Bird","Chicken","Fried","But","Car","Train","Motorcycle"]
traducciones2=["Hola","Perro","Rojo","Verde","Azul","Mochila","Mesa","Gato","Pajaro","Pollo","Frito","Pero","Coche","Tren","Motocicleta"]

if (opc==1):
        print("---TABLA DE TRADUCCIONES---")
        for palabra_s,palabra_e in zip(traducciones2, traducciones):
                print(palabra_s,"-",palabra_e)
elif(opc==2):
        palabra=input("Introduzca la palabra que desea traducir: ")
        i=0
        for palabra_s,palabra_e in zip(traducciones2,traducciones):
                if(palabra==palabra_s):
                        print("La traduccion de la palabra es: ",palabra_e)
                        i=1
                elif(palabra==palabra_e):
                        print("La traduccion de la palabra es: ",palabra_s)
                        i=1
        if(i!=1):
                print("La palabra introducida no es reconocida en el diccionario.")