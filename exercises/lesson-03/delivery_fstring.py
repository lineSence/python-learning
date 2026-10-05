# Занятие 3, задача 3 (по заготовке). Работает.
weight = float(input("Вес, кг: ").replace(",", "."))
price_per_kg = float(input("Цена за кг: ").replace(",", "."))
cost = weight * price_per_kg
print(f"Вес {weight} кг × {price_per_kg:.2f} руб. = {cost:.2f} руб.")
