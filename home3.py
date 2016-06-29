'''
Купи слона.
Компьютер предлагает купить слона пока пользователь не введет слово "хорошо" иначе пишет "Все говорят" + слова пользователя + ", а ты купи слона!"

Модификация.
Константой задается список продуктов. Компьютер должен "продать" все продукты, так как продавал слона.
'''

product = ['Elefant', 'Umbrella', 'Shoe']

def agressive(prod2sell, user_input):
    return input('Все говорят: \"' + user_input + '\", а ты купи ' + prod2sell + ' ')

for prod2sell in product:
    print('Attention! ' + prod2sell + ' is for SALE!')
    user_input = input('Купи ' + prod2sell + ' ')
    while user_input != 'хорошо':
        user_input = agressive(prod2sell, user_input)
    print(prod2sell + ' is sold!\n')

input('\nStock is empty. Press Enter to finish')
