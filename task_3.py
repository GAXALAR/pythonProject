person = {}
data = input('Введите ваше: имя, фамилия, год рождения, город проживания, email, телефон: ')
data = data.split()
person['имя'] = data[0]
person['фамилия'] = data[1]
person['год рождения'] = data[2]
person['город проживания'] = data[3]
person['email'] = data[4]
person['телефон'] = data[5]

print(person)


