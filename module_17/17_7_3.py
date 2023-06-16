per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money = int(input("Введите сумму: "))

deposit = []
for key in per_cent:
    deposit.append(int(per_cent[key] * (money / 100)))

print(f"""{deposit}
Максимальная сумма, которую вы можете заработать — {max(deposit)}""")
