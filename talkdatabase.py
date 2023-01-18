from talk.models import Message
from talk.models import Stress

talk_a_name = 'Aさん'
talk_b_name = 'Bさん'
talk_a_list = ['おはよう', 'こんにちは', 'こんばんは']
talk_b_list = ['おはよう1', 'こんにちは1', 'こんばんは1']
talk_list = []

for i in range(len(talk_a_list)):
    talk_list.append(talk_a_list[i])
    talk_list.append(talk_b_list[i])

i = 0    # talk用のカウンタ
for talk in talk_list:
    if i % 2 == 0:
        talk_database = Message(name = talk_a_name, content = talk)
    else:
        talk_database = Message(name = talk_b_name, content = talk)
    i = i + 1
    database.save()
    print(database.name)
    print(database.content)
         
#stress_value = '40%'    # TextFieldの場合
stress_value = 40.0      # FloatFieldの場合
stress_database = Stress(stress = stress_value)
stress_database.save()