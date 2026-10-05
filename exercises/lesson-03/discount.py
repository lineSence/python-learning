# Занятие 3, задача 4. Вторая версия после разбора. Логика верная: 1500 и 15 -> 1275.00.
total=float(input("Сумма=").replace(",", "."))
discount_percent=float(input("Скидка=").replace(",", "."))
discount=(total/100*discount_percent)
to_pay=(total-discount)
print(f"Сумма={total:.2f} руб.")
print(f"Скидка={discount_percent:.2f}%: {discount:.2f} руб.")
print(f"К оплате={to_pay:.2f} руб.")
