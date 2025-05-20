import hashlib

login = True

while login == True:
    n = int(input("O que você deseja fazer?\n1 - Cadastrar \n2 - Autenticar \n3 - Sair\n> "))

    if n == 1:
        print("cadastro")
        usuario = input("Digite o nome do usuário")
        senha = input("Digite a senha do usuário")
        senha_md5 = hashlib.md5(senha.encode())
        senha_md5 = senha_md5.hexdigest()
        with open("Credenciais.txt", "w") as arquivo:
            arquivo.write(f"{usuario},{senha_md5}\n")
        
    elif n == 2:
        print("autenticar")
        with open("Credenciais.txt", "r") as arquivo:
            conteudo = arquivo.readlines()

        for linha in conteudo:
            usuario = linha.split(",")
            nome_usuario = usuario[0]
            senha_usuario = usuario[1].replace("\n", "")
            print(nome_usuario)
            print(senha_usuario)

    elif n == 3:
        login = False


print("Você saiu")