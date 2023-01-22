# Устройство состоит из трех деталей. 
# Для первой детали вероятность выйти из строя в первый месяц равна 0.1, 
# для второй - 0.2, для третьей - 0.25. Какова вероятность того, 
# что в первый месяц выйдут из строя:
#  а). все детали б). только две детали в). хотя бы одна деталь г). от одной до двух деталей?
p1 = 0.1  # Вероятность выйти из строя первой детали
q1 = 1 - 0.1 # Вереятность НЕ поломки первой детали
p2 = 0.2  # Вероятность выйти из строя второй детали
q2 = 1 - 0.2 # Вереятность НЕ поломки второй детали
p3 = 0.25 # Вероятность выйти из строя третьей детали
q3 = 1 - 0.25 # Вереятность НЕ поломки первой детали

print(f"a) Вероятность выхода из строя всех деталей {p1*p2*p3} или {p1*p2*p3*100:0.2f}%")
print(f"б) Вероятность выхода из строя двух деталей {p1*p2*q3+q1*p2*p3+p1*q2*p3} или {(p1*p2*q3+q1*p2*p3+p1*q2*p3)*100:0.2f}%")
print(f"в) Вероятность выхода из строя хотябы одной {p1*q2*q3+q1*p2*q3+q1*q2*p3+p1*p2*q3+q1*p2*p3+p1*q2*p3+p1*p2*p3} или {(p1*q2*q3+q1*p2*q3+q1*q2*p3+p1*p2*q3+q1*p2*p3+p1*q2*p3+p1*p2*p3)*100:0.2f}%")
print(f"г) Вероятность выхода из строя от 1 до 2 шт {p1*q2*q3+q1*p2*q3+q1*q2*p3+p1*p2*q3+q1*p2*p3+p1*q2*p3} или {(p1*q2*q3+q1*p2*q3+q1*q2*p3+p1*p2*q3+q1*p2*p3+p1*q2*p3)*100:0.2f}%")