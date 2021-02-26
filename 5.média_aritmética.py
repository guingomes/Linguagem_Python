#desenvolva um programa que leia duas notas de um aluno, calcule e mostre a sua média arredondada para uma casa decimal.
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = (n1+n2)/2

print('A média entre {} e {} é igual a {:.1f}'.format(n1, n2, m))
