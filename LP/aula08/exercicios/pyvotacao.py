import csv


# Lista para armazenar os votos
votos = []

# Lê os dados do arquivo CSV
with open('aula08/exercicios/dados_elecao.csv', 'r') as dados:
    leitor = csv.reader(dados)
    next(leitor)  # Pula o cabeçalho
    for linha in leitor:
        candidato = linha[2].strip()  # Coluna do candidato
        votos.append(candidato)

# Obtém os candidatos únicos
candidatos = set(votos)

# Conta os votos para cada candidato
cand_voto = {candidato: votos.count(candidato) for candidato in candidatos}

# Ordena o dicionário por quantidade de votos (decrescente)
cand_voto = sorted(cand_voto.items(), key=lambda x: x[1], reverse=True)

# Cria o arquivo de resultados
with open('aula08/exercicios/resultado.csv', 'w', newline='') as result:
    escritor = csv.writer(result)
    escritor.writerow(['Resultados eleitorais'])
    escritor.writerow(['-' * 25])
    escritor.writerow([f'Total de votos: {len(votos)}'])
    escritor.writerow(['-' * 25])
    for cand in cand_voto:
        porcentagem = (cand[1] * 100) / len(votos)
        escritor.writerow([f'{cand[0]}: {porcentagem:.1f}% ({cand[1]})'])
    escritor.writerow(['-' * 25])
    escritor.writerow([f'Vencedor: {cand_voto[0][0]}'])
    escritor.writerow(['-' * 25])
