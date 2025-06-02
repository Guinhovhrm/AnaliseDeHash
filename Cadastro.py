#Victor Hugo Rodrigues Macharete
#Caio Letty de Carvalho

import hashlib

login = True

while login == True:
    n = int(input("O que você deseja fazer?\n1 - Cadastrar \n2 - Autenticar \n3 - Sair\n> "))

    if n == 1:
        print("cadastro")
        usuario = input("Digite o nome do usuário (com 4 letras)> ")
        if len(usuario) != 4:
            print("Quantidade de letras incorretas, até no máximo 4")
            break

        senha = input("Digite a senha do usuário > ")
        if len(senha) != 4:
            print("Quantidade de caracteres incoretas, até no máximo 4")
            break
        
        senha_md5 = hashlib.md5(senha.encode())
        senha_md5 = senha_md5.hexdigest()
        with open("Credenciais.txt", "a") as arquivo:
            arquivo.write(f"{usuario},{senha_md5}\n")
        
    elif n == 2:
        print("autenticar")
        with open("Credenciais.txt", "r") as arquivo:
            conteudo = arquivo.readlines()
        
        user_verif = input(f"Digite o nome do usuário > ").strip()
        encontrou = False

        for linha in conteudo:
            usuario = linha.strip().split(",")
            nome_usuario = usuario[0].strip()
            senha_usuario = usuario[1].strip()
            
            if user_verif == nome_usuario:
                tentativas = 0
                encontrou = True
                while tentativas < 3:
                    senha_verif = input(f"Digite a senha de verificação do usuário {user_verif} > ")
                    hash_senha_verif = hashlib.md5(senha_verif.encode()).hexdigest()
                        
                    if (hash_senha_verif == senha_usuario):
                        print("A senha do usuário está correta")
                        break
                    else:
                        tentativas += 1
                        print(f"A senha do usuário está incorreta. Tentativas restantes: {3 - tentativas}")
                        
                        if tentativas == 3:
                            print("números de tentativas excedido.")
                            login = False
    elif n == 3:
        login = False
    