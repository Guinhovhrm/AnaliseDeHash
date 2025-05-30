import hashlib
import itertools
import string
import time


caracteres = string.ascii_letters + string.digits + string.punctuation

def quebrar_md5(hash_alvo):
    inicio = time.time()
    
    for tentativa in itertools.product(caracteres, repeat=4):
        senha_tentativa = ''.join(tentativa)
        hash_tentativa = hashlib.md5(senha_tentativa.encode()).hexdigest()

        if hash_tentativa == hash_alvo:
            fim = time.time()
            tempo = fim - inicio
            return senha_tentativa, tempo

    return None, None

# Ler o arquivo de credenciais
try:
    with open("Credenciais.txt", "r") as arquivo:
        credenciais = [linha.strip().split(",") for linha in arquivo.readlines()]
except FileNotFoundError:
    print("Arquivo Credenciais.txt não encontrado.")
    exit()

# Armazenar resultados
resultados = []

print("Iniciando quebra de hashes...")

for usuario, hash_senha in credenciais:
    print(f"\nQuebrando senha para o usuário: {usuario} (hash: {hash_senha})")
    senha, tempo = quebrar_md5(hash_senha)
    
    if senha:
        print(f"Senha encontrada: {senha} | Tempo: {tempo:.2f} segundos")
    else:
        print("Falha ao encontrar a senha.")
    
    resultados.append((usuario, hash_senha, senha, tempo))

# Exibir tabela de resultados
print("\n--- Tabela de Resultados ---")
print(f"{'Usuário':<10} {'Hash':<34} {'Senha':<6} {'Tempo (s)':<10}")
print("-" * 65)

for usuario, hash_senha, senha, tempo in resultados:
    tempo_str = f"{tempo:.2f}" if tempo else "N/A"
    senha_str = senha if senha else "Não encontrada"
    print(f"{usuario:<10} {hash_senha:<34} {senha_str:<6} {tempo_str:<10}")

print("\nProcesso finalizado.")
