def imprimir_pareja(nombres):
    for i in range(0,len(nombres)-1):
        for j in range(i+1,len(nombres)):
            pareja = (nombres[i],nombres[j])
            print(pareja) 



nombres = ["Ana","Pablo","Juan","Eliana"]
imprimir_pareja(nombres) 