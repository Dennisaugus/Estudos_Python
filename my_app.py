def aluno(nome, email, *args):
    return sum(args)

print(aluno('Dennis', 'dennisasg@outlook.com', 23.4))
print(aluno('Maria','mariaasg@outlook.com'))
print(aluno('Jose','joseasg@outlook.com',2 ,3 ,5 ,6)) 