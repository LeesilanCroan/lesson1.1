temp={
    'city': 'Москва',
    'temperature': 20
}
print(temp['city'])
temp['temperature'] = temp['temperature']-5
print(temp)
print(temp.get('country'))
print(temp.get('country', 'Россия'))
temp['date'] = '27.05.2019'
print(len(temp))