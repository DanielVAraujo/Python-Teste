print ("Digite sua nota do 1º Bimestre")
nota1 = input()
nota1_real= float (nota1)
print ("Digite sua nota do 2º Bimestre")
nota2 = input()
nota2_real= float (nota2)
print ("Digite sua nota do 3º Bimestre")
nota3 = input()
nota3_real= float (nota3)
print ("Digite sua nota do 4º Bimestre")
nota4 = input()
nota4_real= float (nota4)
media = (nota1_real+nota2_real+nota3_real+nota4_real)/4

print (f"Resultado da Média: {media}")

if media>=6:
    print("Parabéns, Você Foi Aprovado!")
else:
    print("Sinto Muito, Você Está Reprovado!")
