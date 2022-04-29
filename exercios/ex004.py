#Faça um programa que leia algo pelo teclado e mostre na tela
# o seu tipo primitivo e todas as informações possíveis sobre ele.
a1=input ('escreva algo: ')
print('a somente letras? ',a1.isalpha())
print('a somente numeros',a1.isalnum())
print('a somente letras maiuculas',a1.isupper())
print('a somente letras minusculas',a1.islower())