def calcular_media(notas):
    total_notas = sum(notas)
    return total_notas / len(notas)

def aluno_reprovado(media):
    return media < 6

def gerar_saida_aluno_reprovado(dados_alunos, matriculas_reprovadas):
    for matricula in matriculas_reprovadas:
        aluno = dados_alunos.get(matricula)
        if aluno:
            nome = aluno.get('nome')
            media_final = aluno.get('media_final')
            print(f"Aluno Reprovado: {nome} – Matrícula: {matricula} – Média Final: {media_final}")
