alunos = [('Eduardo', 3), ('Aluno', 10), ('Professor', 7)]

#  List Comprehension
print([(nome, nota) for nome, nota in alunos if nota > 5])

#  programação funcional --> filter()

def nota_maior_que_5(aluno):
	_, nota = aluno
	return nota > 5

print(list(filter(nota_maior_que_5, alunos)))