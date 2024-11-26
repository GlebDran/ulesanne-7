arvud = []
for i in range(5):
    arv = int(input(f"Sisesta {i+1}. täisarv: "))
    arvud.append(arv)

aritmeetiline_keskmine = sum(arvud) / len(arvud)
print(f"Aritmeetiline keskmine on {aritmeetiline_keskmine:.2f}")

