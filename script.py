per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money=int(input("Введите сумму которую выпланируете положить под процент:"))

t=int((per_cent['ТКБ'])*(money/100))
s=int((per_cent['СКБ'])*(money/100))
v=int((per_cent['ВТБ'])*(money/100))
sb=int((per_cent['СБЕР'])*(money/100))


deposit=[t,s,v,sb]

print("Сумма по прошествии года в каждом из банков:",deposit)
print("Максимальная сумма, которую вы можете заработать",max(deposit))