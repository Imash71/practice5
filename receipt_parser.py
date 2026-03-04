import re
import json
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
datetime_value = datetime_match.group(1) if datetime_match else None
# Метод оплаты
payment_match = re.search(r"(Банковская карта|Наличные)", receipt)
payment_method = payment_match.group(1) if payment_match else None
# Формируем JSON
data = {
   "products": products,
   "prices": prices_clean,
   "total": total,
   "datetime": datetime_value,
   "payment_method": payment_method
}
# Выводим JSON
print(json.dumps(data, ensure_ascii=False, indent=4))