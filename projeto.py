import time, os , webbrowser
from tabulate import tabulate
dados=[]

while True:
    print("1-Calcular o Imc\n2-Consultar historico\n3-Sair") 
    opçoes= input("escolha aqui as opçoes: ") 
        
    match opçoes:
        case "1": 
            os.system(' cls ') 
            print("estamos te redirecionando a tabela") 
            time.sleep(2)
            break

        case  "2":
            os.system('cls')   
            dados=[]
            with open("dados_usuario.txt", "r") as arquivo:
                for linha in arquivo:
                    dados.append(linha.strip().split(","))
                print(tabulate(dados, headers=["Nome", "Altura", "Peso"], tablefmt="plain"))
                comando2= input("digite (sim/nao) para apagar os dados: ")
                if comando2.lower() == "sim":
                    with open("dados_usuario.txt", "w"):
                        pass

                comando = input("escreva (voltar) para ir ao menu: ") 
                if comando.lower() == "voltar":

                    break
                os.system('cls')

        case "3": 
            os.system( 'cls' ) 
            print("Voce Saiu") 
            exit()

        case _: 
            print("isso nao e permitido")
            time.sleep(2)
            os.system('cls')

os.system('cls')
tabela_imc=[
    ["peso normal", "18.4 a 24.9"],
    ["acima do peso", "25.0 a 29.9"], 
    ["obesidade grau I", "30.0 a 34.9"],
    ["obesidade grau II", "35.0 a 39.9"],
    ["obesidade grau III", "40.0 ou mais"],
]
print(tabulate(tabela_imc, headers=("classificaçao", "imc"), tablefmt="fancy_grid"))

while True:
    def Calcular_IMC(peso, altura, Nome):
        imc = peso / (altura ** 2)
        print(f"Seu IMC é: {imc:.2f}")


        match imc:
            case _ if imc < 18.5:
                print("Você está abaixo do peso.")

            case _ if 18.5 <= imc <= 24.9:
                print("Você está no peso normal.")

            case _ if 25.0 <= imc <= 29.9:
                print("Você está acima do peso.")

            case _ if 30.0 <= imc <=34.9:
                print("Você tem Obesidade Grau I ")

            case _ if 35.0 <= imc <= 39.9:
                tabela_imc=[
                    ["Obesidade Grau II", "35.0 a 39.9"]
                ]
                print(tabulate(tabela_imc, headers=("classificaçao", "imc"),tablefmt="fancy_grid"))
                
                time.sleep(5)
                os.system( 'cls' )

                tabela=[
                    ["---AGUARDE---CARREGANDO AS DICAS---"]
                ]
                print(tabulate(tabela, headers=("aguarde"), tablefmt= "simple"))

                time.sleep(2)
                print(f"Ola {Nome}!!!")
                time.sleep(3)

                comando = input("escreva dicas para ver soluçoes: ")
                if comando.lower() == "dicas":
                    chrome = webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s ")
                    chrome.open_new_tab("https://www.tuasaude.com/obesidade-grau-2/")
                   

            case _ if imc >= 40.0 :
                tabela_imc=[
                    ["Obesidade Grau III", "40.0+"]
                ]
                print(tabulate(tabela_imc, headers=("classificaçao", "imc"),tablefmt="fancy_grid"))

                time.sleep(5)
                os.system( 'cls' )
                print("---AGUARDE---CARREGANDO AS DICAS---")
                time.sleep(2)
                print(f"Ola {Nome}")
                time.sleep(3)


                comando = input("escreva dicas para ser direcionado ao site: ")
                if comando.lower() == "dicas":
                    chrome = webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s ")
                    chrome.open_new_tab("https://www.tuasaude.com/obesidade-morbida/")
    try:
        Nome = str(input("informe aqui seu nome: "))
        peso = float(input("informe aqui o seu peso: "))
        altura = float(input("infome aqui a sua altura: "))

        with open("dados_usuario.txt", "a") as arquivo:
            arquivo.write(f"{Nome}, {altura:.2f}m, {peso:.2f}kg\n")
            

        Calcular_IMC(peso, altura, Nome)
    except ValueError:
        print("isso nao e compativel")
    
    time.sleep(5)
    os.system('cls')
    comand = input("Deseja fazer outro calculo (sim/nao)\n")
    os.system('cls')
    if comand == "nao":
        print("Voce Saiu")
        exit()
