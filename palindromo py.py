def es_palindronhmo(cadena):
    cadena = cadena.lower().replace(" ","")
    largo = len(cadena)//2
    for i in range(0, largo):
        if (cadena[i] != cadena[-i-1]):
            return False


    return True
        
    
   
palabra = input("ingrese una palabra palindromo:" )
print(es_palindronhmo(palabra))