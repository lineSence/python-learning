# Занятие 3, задача 4. Первая версия, как написал я. Нужно исправить (см. lessons/003-f-strings.md).
sum=float(input("Сумма=").replace(",", "."))
dis=float(input("Скидка=").replace(",", "."))
cost=float(sum/100*dis+sum)
print(f"Сумма={sum}руб.")
print(f"Скидка={dis}%")
print(f"К оплате={cost}руб.")
