#a parte que eu fiz:
#m = float(input('digite o valor em metros: '))
#print(f'{m} metros é ingual a \n{m*100 :.0f}cm\n{m*1000 :.0f}mm')

#não fiz essa parte:
medida = float(input('Uma distancia em metros: '))
mm = medida * 1000
cm = medida * 100
dm = medida * 10
dam = medida / 10
hm = medida / 100
km = medida / 1000
print('a media  de  {}m coresponde a \n{}km \n{}hm \n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(medida, km, hm, dam, dm, cm, mm))