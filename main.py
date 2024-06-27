from operacoes import calcular_media, aluno_reprovado, gerar_saida_aluno_reprovado

dados_alunos={
    '26': {'nome':'Maria', 'notas':[8, 7, 5, 9] },
    '101': {'nome': 'Ana', 'notas':[9, 9, 8, 9]},
    '13': {'nome': 'João', 'notas':[6, 5, 5, 5]},
    '37': {'nome': 'Ágatha', 'notas':[8, 6, 7.5, 9]},
    '72': {'nome': 'Joaquim', 'notas':[6, 5.5, 5, 7]},
    '5': {'nome': 'Félix', 'notas':[10, 8, 8, 8]},
    
}

for matricula, aluno in dados_alunos.items():
    media = calcular_media(aluno['notas'])
    aluno['media'] = media

for matricula, aluno in dados_alunos.items():
    if aluno_reprovado(aluno['media']):
        print(f"{aluno['nome']} está reprovado.")


matriculas_reprovadas = [matricula for matricula, aluno in dados_alunos.items() if aluno_reprovado(aluno['media'])]

gerar_saida_aluno_reprovado(dados_alunos, matriculas_reprovadas)