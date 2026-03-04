import re
import json
<<<<<<< HEAD
# Читаем чек из raw.txt
with open("raw.txt", encoding="utf-8") as f:
   receipt = f.read()
# Цены
prices = re.findall(r"\n(\d[\d\s]*,\d{2})\nСтоимость", receipt)
prices_clean = [float(p.replace(" ", "").replace(",", ".")) for p in prices]
# Продукты
products = re.findall(r"\d+\.\n(.+?)\n\d", receipt, re.DOTALL)
# Итог
total_match = re.search(r"ИТОГО:\n([\d\s]+,\d{2})", receipt)
total = float(total_match.group(1).replace(" ", "").replace(",", ".")) if total_match else None
# Дата и время
datetime_match = re.search(r"Время:\s([\d\.]+\s[\d:]+)", receipt)
=======
# Вставляешь текст чека сюда, вместо ...
receipt = """
сюда вставляешь весь текст чека
"""
# Извлекаем все цены
prices = re.findall(r"\n(\d[\d\s]*,\d{2})\nСтоимость", receipt)
clean_prices = [float(p.replace(" ", "").replace(",", ".")) for p in prices]
# Извлекаем названия продуктов
products = re.findall(r"\d+\.\n(.+?)\n\d", receipt, re.DOTALL)
# Общая сумма
total_match = re.search(r"ИТОГО:\n([\d\s]+,\d{2})", receipt)
total = total_match.group(1).replace(" ", "").replace(",", ".") if total_match else None
# Дата и время
datetime_match = re.search(r"Время:\s(\d{2}\.\d{2}\.\d{4}\s\d{2}:\d{2}:\d{2})", receipt)
>>>>>>> 08d0d7740bb364bf41b2a6243992fa9f764cab8c
datetime_value = datetime_match.group(1) if datetime_match else None
# Метод оплаты
payment_match = re.search(r"(Банковская карта|Наличные)", receipt)
payment_method = payment_match.group(1) if payment_match else None
<<<<<<< HEAD
# Формируем JSON
data = {
   "products": products,
   "prices": prices_clean,
=======
# Собираем данные
data = {
   "products": products,
   "prices": clean_prices,
>>>>>>> 08d0d7740bb364bf41b2a6243992fa9f764cab8c
   "total": total,
   "datetime": datetime_value,
   "payment_method": payment_method
}
<<<<<<< HEAD
# Выводим JSON
print(json.dumps(data, ensure_ascii=False, indent=4))
=======
print(json.dumps(data, indent=4, ensure_ascii=False))
>>>>>>> 08d0d7740bb364bf41b2a6243992fa9f764cab8c
