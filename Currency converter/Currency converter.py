def dolar_americano(pesos_colombianos):
    dolar_americano = 3939
    dolar_americano = round(float(pesos_colombianos / dolar_americano), 2)
    dolar_americano = "{:,}".format(dolar_americano)
    dolar_americano = str(dolar_americano)
    return dolar_americano


def run():
    user = input("Hi, What is your name? ").capitalize()
    menu = int(input(f"""{user}, soy tu conversor de pesos colombianos a diferentes monedas del mundo. 
                     
                     A que moneda quisieras convertir tus pesos colombianos?
                     
                     1 Dolar americano. 
                     
                     2 Dolar canadiense. 
                     
                     3 Peso mexicano. 
                     
                     4 Sol peruano.
                     
                     5 Peso chileno.
                     
                     6 Peso uruguayo.
                     
                     7 Peso argentino. 
                     
                     8 Real brasileño.
                     
                     9 Peso argentino. 
                     
                     10 Euro.
                     
                     11 Libra esterlina. 
                     
                     12 Dolar australiano. 
                     
                     13 Yen japones.
                     
                     14 Yuan chino.
                     
                     Escribe el numero de la selección que escogiste: """))
    
    
    if menu == 1:
        pesos_colombianos = float(input(f"{user}, cuantos pesos colombianos deseas convertir? "))
        dolar = dolar_americano(pesos_colombianos)
        dolar = print(f"{user} tienes {dolar} dolares.")
        
    
if __name__ == "__main__":
    run()