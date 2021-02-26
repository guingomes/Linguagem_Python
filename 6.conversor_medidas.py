#criar um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

m = float(input('Digite um valor em metros: '))
km = m/1000
hm = m/100
dam= m/10

dm = m*10
cm = m*100
mm = m*1000

print("A medida de {} metros corresponde a {:.0f} dm, {:.0f} cm e {:.0f} mm".format(m, dm, cm, mm))

print("A medida de {} metros corresponde a {} km, {} hm e {} dam".format(m, km, hm, dam))