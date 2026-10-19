# temperature = 28

# if temperature > 25:
#     print("Сегодня жарко")

# print("Проверка завершена")

# if balance >= price:
#     balance -= price
#     print("Покупка оплачена")

# print("Текущий баланс:", balance)

order_total = 3200

if order_total >= 5000:
    delivery = 0
elif order_total >= 2000:
    delivery = 250
else:
    delivery = 500

final_total = order_total + delivery
print(f"Доставка: {delivery} руб.")
print(f"К оплате: {final_total} руб.")