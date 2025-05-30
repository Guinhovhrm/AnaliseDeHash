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
        
        user_verif = input(f"Digite o nome do usuário > ")
        encontrou = False

        for linha in conteudo:
            usuario = linha.split(",")
            nome_usuario = usuario[0]
            senha_usuario = usuario[1].replace("\n", "")
            
            if user_verif == nome_usuario:
                encontrou = True
                senha_verif = input(f"Digite a senha de verificação do usuário {user_verif} > ")
                hash_senha_verif = hashlib.md5(senha_verif.encode()).hexdigest()
                
                    
                if (hash_senha_verif == senha_usuario):
                    print("A senha do usuário está correta")
                else:
                    print("A senha do usuário está incorreta")
                    break
            
            else:
                print("")
                
                    
    elif n == 3:
        login = False
    