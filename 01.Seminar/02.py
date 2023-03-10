# Разработали спам-фильтр на основании часто встречающихся фраз. 70% всех писем –это 
# спам. В 10 % писем со спамом встречается фраза: «вся правда о» и в 0.5% она встречается 
# в хороших письмах. Какова вероятность, что пришедшее на почту письмо является спамом, 
# если в нем есть данная фраза?
# A - фраза
# B1 - спам
# B2 - не спам
# P(B1) - вероятность взять спам = 0,7
# P(B2) - вероятность взять неспам = 0,3
# P(A|B1) - вероятсновть фрызы в спаме = 0,1 
# P(A|B2) - вероятность фразы не в спаме = 0,005
# P(A) - полная вероятность события А = P(B1) * P(A|B1) + P(B2) * P(A|B2)
# P(B|A) - вероятность B (спама), при условии (если) событие А (фраза) произошло - 
# - формула Байеса = P(A|B) * P(B) / P(A)
PB = 0.7
PB1 = PB
PB2 = 0.3
PA_B = 0.1
PA_B1 = PA_B
PA_B2 = 0.005
PA = 0.7 * 0.1 + 0.3 * 0.005
print(f"Вероятность получить спам, если есть в нем фраза {PA_B * PB / PA * 100:1.2f}%")