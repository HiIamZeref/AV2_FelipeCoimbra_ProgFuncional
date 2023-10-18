from pprint import pprint

database = [
    {"login": "admin", "senha": "admin"},
    {"login": "felipe", "senha": "123"},
    {"login": "pedro", "senha": "321"}
]

balance = {
    "admin": 1000,
    "felipe": 1000,
    "pedro": 1000
}


getLogin = lambda : (input("Digite o login: "), input("Digite a senha: "))
checkDatase = lambda data: True if {"login":data[0], "senha": data[1]} in database else False


flux = lambda result: chooseOperation(input("Digite a operação:  (deposit ou withdraw) ")) if result else print("Login Inválido.")
chooseOperation = lambda operation : deposit(LOGIN, int(input("Digite o valor a ser depositado: "))) if operation == "deposit" else withdraw( LOGIN, int(input("Digite o valor a ser retirado: ")))


deposit = lambda name, value: print(f"Novo saldo:  { {nome: saldo + value for nome, saldo in balance.items() if name == nome} }")
withdraw = lambda name, value: print(f"Novo saldo:  { {nome: saldo - value for nome, saldo in balance.items() if name == nome} }") if balance[name] - value >= 0 else "Saldo insuficiente."


LOGIN, SENHA = getLogin()
flux( checkDatase( (LOGIN, SENHA) ) )






