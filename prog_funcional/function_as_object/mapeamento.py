import operator

alunos = [('Eduardo', 3), ('Aluno', 10), ('Professor', 7)]

#  Fazer o mapeamento dos nomes de alunos com nota > 5 (filtragem)

#  List Comprehension
print([ nome for nome, nota in alunos if nota > 5])


# Programação Funcional --> map()

def retorna_nomes(aluno):
	nome, _ = aluno
	return nome

def nota_maior_que_5(aluno):
	_, nota = aluno
	return nota > 5

print(list(map(retorna_nomes, filter(nota_maior_que_5, alunos))))

#  Utilizando módulo operator
print(list(map(operator.itemgetter(0), filter(nota_maior_que_5, alunos))))


