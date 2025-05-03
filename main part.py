alfavit_EN = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

offset = int(input('Шаг Шифрования:'))
language = input("Язык (RU/ENG):").strip().upper()

if language == "ENG":
  alfavit = alfavit_EN
elif language == "RU":
  alfavit = alfavit_RU
else:
  print("Выбран неверный язык")
  exit()

message = input('Сщщбщение для шифровки:').upper()
itog = ''

for i in message:
  mesto = alfavit.find(i)
  if mesto + offset > len(alfavit):
    new_mesto = mesto+offset - len(alfavit)
  else:
    new_mesto = mesto + offset
  itog += alfavit[new_mesto]
  alfavit[new_mesto]
  print('Зашифрованное сообщение:', itog)
