names = ["Alice", "Bob", "Charlie"]
salary = [5000, 6000, 7000]
bonus = ["10%", "5%", "15%"]



#print({name: (salary * float(bonus[:-1])/100) for name, salary, bonus in zip(names, salary, bonus)})

result = {names[i]: round(salary[i] * float(bonus[i].strip('%')) / 100, 2) for i in range(len(names))}
print(result)