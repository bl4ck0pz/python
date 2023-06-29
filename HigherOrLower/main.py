from game_data import data
from os import system
import art 

def pick_person(data):
    '''Randomly selects persons'''
    from random import randint
    return data[randint(0,49)]
    
def compare_celebs(person_A, person_B):
    '''
    Gives each celebrity an id &
    Returns the celebrity with the highest follwers 
    '''
    person_A["id"] = "a"
    person_B["id"] = "b"

    if int(person_A['follower_count']) > int(person_B['follower_count']):
        return person_A
    elif int(person_A['follower_count']) < int( person_B['follower_count']):
        return person_B

def game(person_A, person_B, score):
    if person_A['name'] == person_B['name']:
        person_B = pick_person
        
    system("cls")
    
    print(art.logo)
    print(f"You're right! Current score:  {score}." if score > 0 else "")
    print(f"Compare A: {person_A['name']}, a {person_A['description']}, from {person_A['country']}")
    print(art.vs)
    print(f"Against B: {person_B['name']}, a {person_B['description']}, from {person_B['country']}")
    
    choice = input("Who has more follwers? Type 'A' or 'B': ").lower()

    if choice != compare_celebs(person_A, person_B)['id']:
        print(f"Sorry, thats wrong. Final score: {score}")
        return
    else:
        score += 1
        print
        game(compare_celebs(person_A, person_B),pick_person(data), score)


person_A = pick_person(data)
person_B = pick_person(data)
game(person_A, person_B, score = 0)  
