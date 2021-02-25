#objetivo é criar um programa que leia um número e mostre o seu dobro, tribro e sua raiz quadrada.
num=float(input('Digite um número inteiro: '))
dobro=num*2
triplo=num*3
raiz=num**(1/2)

print('O dobro desse número é {}, o seu triplo vale {} e a raiz quadrada é {:.2f}.'.format(dobro, triplo, raiz))
