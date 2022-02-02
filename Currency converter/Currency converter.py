def argentine_peso(colombian_pesos):
    argentine_peso = 37.33
    argentine_peso = round(float(colombian_pesos / argentine_peso), 2)
    argentine_peso = "{:,}".format(argentine_peso).replace(".", "|").replace(",", ".").replace("|", ",")
    argentine_peso = str(argentine_peso)
    return argentine_peso


def australian_dollar(colombian_pesos):
    australian_dollar = 2798.27
    australian_dollar = round(float(colombian_pesos / australian_dollar), 2)
    australian_dollar = "{:,}".format(australian_dollar).replace(".", "|").replace(",", ".").replace("|", ",")
    australian_dollar = str(australian_dollar)
    return australian_dollar


def brazilian_real(colombian_pesos):
    brazilian_real = 745.13
    brazilian_real = round(float(colombian_pesos / brazilian_real), 2)
    brazilian_real = "{:,}".format(brazilian_real).replace(".", "|").replace(",", ".").replace("|", ",")
    brazilian_real = str(brazilian_real)
    return brazilian_real


def british_pound(colombian_pesos):
    british_pound = 5305.64
    british_pound = round(float(colombian_pesos / british_pound), 2)
    british_pound = "{:,}".format(british_pound).replace(".", "|").replace(",", ".").replace("|", ",")
    british_pound = str(british_pound)
    return british_pound


def canadian_dollar(colombian_pesos):
    canadian_dollar = 3091.79
    canadian_dollar = round(float(colombian_pesos / canadian_dollar), 2)
    canadian_dollar = "{:,}".format(canadian_dollar).replace(".", "|").replace(",", ".").replace("|", ",")
    canadian_dollar = str(canadian_dollar)
    return canadian_dollar


def chilean_peso(colombian_pesos):
    chilean_peso = 4.95
    chilean_peso = round(float(colombian_pesos / chilean_peso), 2)
    chilean_peso = "{:,}".format(chilean_peso).replace(".", "|").replace(",", ".").replace("|", ",")
    chilean_peso = str(chilean_peso)
    return chilean_peso


def chinese_yuan(colombian_pesos):
    chinese_yuan = 616.86
    chinese_yuan = round(float(colombian_pesos / chinese_yuan), 2)
    chinese_yuan = "{:,}".format(chinese_yuan).replace(".", "|").replace(",", ".").replace("|", ",")
    chinese_yuan = str(chinese_yuan)
    return chinese_yuan


def euros(colombian_pesos):
    euro = 4424.27
    euro = round(float(colombian_pesos / euro), 2)
    euro = "{:,}".format(euro).replace(".", "|").replace(",", ".").replace("|", ",")
    euro = str(euro)
    return euro


def japanese_yen(colombian_pesos):
    japanese_yen = 34.20
    japanese_yen = round(float(colombian_pesos / japanese_yen), 2)
    japanese_yen = "{:,}".format(japanese_yen).replace(".", "|").replace(",", ".").replace("|", ",")
    japanese_yen = str(japanese_yen)
    return japanese_yen


def mexican_peso(colombian_pesos):
    mexican_peso = 190.98
    mexican_peso = round(float(colombian_pesos / mexican_peso), 2)
    mexican_peso = "{:,}".format(mexican_peso).replace(".", "|").replace(",", ".").replace("|", ",")
    mexican_peso = str(mexican_peso)
    return mexican_peso


def peruvian_sol(colombian_pesos):
    peruvian_sol = 1025.57
    peruvian_sol = round(float(colombian_pesos / peruvian_sol), 2)
    peruvian_sol = "{:,}".format(peruvian_sol).replace(".", "|").replace(",", ".").replace("|", ",")
    peruvian_sol = str(peruvian_sol)
    return peruvian_sol


def uruguayan_peso(colombian_pesos):
    uruguayan_peso = 89.35
    uruguayan_peso = round(float(colombian_pesos / uruguayan_peso), 2)
    uruguayan_peso = "{:,}".format(uruguayan_peso).replace(".", "|").replace(",", ".").replace("|", ",")
    uruguayan_peso = str(uruguayan_peso)
    return uruguayan_peso


def us_dollar(colombian_pesos):
    us_dollar = 3923.84
    us_dollar = round(float(colombian_pesos / us_dollar), 2)
    us_dollar = "{:,}".format(us_dollar).replace(".", "|").replace(",", ".").replace("|", ",")
    us_dollar = str(us_dollar)
    return us_dollar


def run():
    user = input("Hi, What is your name? ").capitalize()
    menu = int(input(f"""{user}, I am your converter of Colombian pesos to different currencies of the world.
                     
                     What currency would you like to convert your Colombian pesos to?
                     
                     1 Argentine pesos.
                     
                     2 Australian dollar.
                     
                     3 Brazilian real.
                     
                     4 British pound. 
                     
                     5 Canadian dollar.
                     
                     6 Chilean peso.
                     
                     7 Chinese yuan.
                     
                     8 Euro.
                     
                     9 Japanese yen.
                     
                     10 Mexican pesos.
                     
                     11 Peruvian sol.
                     
                     12 Uruguayan peso.
                     
                     13 US dollar.
                     
                     Write the number of the selection you chose: """))
    
    if menu == 1:
        colombian_pesos = float(input(f"{user}, how many Colombian pesos you want to convert? "))
        arg_pesos = argentine_peso(colombian_pesos)
        arg_pesos = print(f"{user}, you have {arg_pesos} argentine pesos.")
    
    elif menu == 2:
        colombian_pesos = float(input(f"{user}, how many Colombian pesos you want to convert? "))
        aus_dollar = australian_dollar(colombian_pesos)
        aus_dollar = print(f"{user}, you have {aus_dollar} australian dollars.")
        
    elif menu == 3:
        colombian_pesos = float(input(f"{user}, how many Colombian pesos you want to convert? "))
        bra_real = brazilian_real(colombian_pesos)
        bra_real = print(f"{user}, you have {bra_real} brazilian reals.")
        
    elif menu == 4:
        colombian_pesos = float(input(f"{user}, how many Colombian pesos you want to convert? "))
        pound = british_pound(colombian_pesos)
        pound = print(f"{user}, you have {pound} british pounds.")
        
    elif menu == 5:
        colombian_pesos = float(input(f"{user}, how many Colombian pesos you want to convert? "))
        cad_dollar = canadian_dollar(colombian_pesos)
        cad_dollar = print(f"{user}, you have {cad_dollar} canadian dollars.")
        
    elif menu == 6:
        colombian_pesos = float(input(f"{user}, how many Colombian pesos you want to convert? "))
        chl_peso = chilean_peso(colombian_pesos)
        chl_peso = print(f"{user}, you have {chl_peso} chilean pesos.")
        
    elif menu == 7:
        colombian_pesos = float(input(f"{user}, how many Colombian pesos you want to convert? "))
        ch_yuan = chinese_yuan(colombian_pesos)
        ch_yuan = print(f"{user}, you have {ch_yuan} chinese yuannes.")
        
    elif menu == 8:
        colombian_pesos = float(input(f"{user}, how many Colombian pesos you want to convert? "))
        euro = euros(colombian_pesos)
        euro = print(f"{user}, you have {euro} euros.")
        
    elif menu == 9:
        colombian_pesos = float(input(f"{user}, how many Colombian pesos you want to convert? "))
        jp_yen = japanese_yen(colombian_pesos)
        jp_yen = print(f"{user}, you have {jp_yen} japanese yen.")
    
    elif menu == 10:
        colombian_pesos = float(input(f"{user}, how many Colombian pesos you want to convert? "))
        mex_peso = mexican_peso(colombian_pesos)
        mex_peso = print(f"{user}, you have {mex_peso} mexican pesos.")
        
    elif menu == 11:
        colombian_pesos = float(input(f"{user}, how many Colombian pesos you want to convert? "))
        per_sol = peruvian_sol(colombian_pesos)
        per_sol = print(f"{user}, you have {per_sol} peruvian sol.")
        
    elif menu == 12:
        colombian_pesos = float(input(f"{user}, how many Colombian pesos you want to convert? "))
        uru_peso = uruguayan_peso(colombian_pesos)
        uru_peso = print(f"{user}, you have {uru_peso} uruguayan peso.")
    
    elif menu == 13:
        colombian_pesos = float(input(f"{user}, how many Colombian pesos you want to convert? "))
        dollar = us_dollar(colombian_pesos)
        dollar = print(f"{user}, you have {dollar} dollars.")
        
    else:
        print("This option is not available, please try again.")
        run()
        
    
if __name__ == "__main__":
    run()