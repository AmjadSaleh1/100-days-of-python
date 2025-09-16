from Data import data
from art import logo
from art import vs
import random

score = 0
end_game = False
print(logo)


def pick_and_check(rand1, rand2, choose):
    if choose == 'a' and rand1 > rand2:
        return 1
    elif choose == 'a' and rand2 > rand1 or choose == 'b' and rand1 > rand2:
        return 0
    elif choose == 'b' and rand2 > rand1:
        return 1


random1 = random.choice(data)
random2 = random.choice(data)

if random1 == random2:
    random2 = random.choice(data)

while not end_game:
    print(f"Compare A:{random1['name']} a {random1['description']} , from {random1['country']}")
    print(vs)
    print(f"Against B:{random2['name']} a {random2['description']} , from {random2['country']}")
    choose = input("who has more followers ? type 'A' or 'B'").lower()
    if not pick_and_check(random1['follower_count'], random2['follower_count'], choose):
        end_game = True
        print(f"sorry,thats wrong , final score {score}")
    else:
        score += 1
        random1 = random2
        random2 = random.choice(data)
        while random2 == random1:
            random2 = random.choice(data)
        second_choice = random2['follower_count']
