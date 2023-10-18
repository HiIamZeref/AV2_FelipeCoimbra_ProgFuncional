from pprint import pprint
getData = lambda : (input("Digite seu login de cadastro: "), input("Digite sua senha de cadastro: "))
saveData = lambda file, login, senha: file.write(f"{login},{senha}\n")

# CADASTRANDO DADOS
LOGIN, SENHA = getData()

fileSave = open("database.txt", "a")

saveData(fileSave, LOGIN, SENHA)
fileSave.close()


# REALIZANDO LOGIN
fileRead = open("database.txt", "r")

generateData = [{"login": line.split(",")[0], "senha": line.split(",")[1]} for line in fileRead]

pprint(generateData)

validateLogin = lambda data: print("SUCESSO") if {"login": input("Insira seu login: "), "senha": input("Insira sua senha: ") + "\n"} in data else print("FRACASSO")

validateLogin(generateData)

fileRead.close()





