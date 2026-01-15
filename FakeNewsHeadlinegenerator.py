import random
subjects  = [
    "Shah Rukh Khan",
    "Virat Kohli",
    "Nirmala Sitharaman",
    "A mumbai cat"
    "A group of monkeys",
    "Prime Minister Modi",
    "Auto rickshaw driver from Delhi"
]

actions = [
    "launches",
    "cancles",
    "dances with",
    "eats",
    "declares war on",
    "orders",
    "celebrates"
]

places_or_things = [
    "at Red Fort",
    "in mumbai local Train",
    "a plate of samosa",
    "inside parliament",
    "at Ganga Ghat",
    "during IPL Match",
    "at India Gate"
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)
    
    headline = f"BREAKING NEWS: {subject} {action} {place_or_thing}"
    print("\n" + headline)
    
    user_input = input("\nDo you want to generate another headline? (yes/no): ").strip().lower()
    if user_input == 'no':
        break

print("\nThanks you for using the Fake News Headline Generator.Have a great day!")