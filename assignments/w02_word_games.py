verbs = []
adjectives = []
exclamations = []
animals = []
nouns = []
adverbs = []
article = "a"

print("Let's play MadLib! \n")

for each in range(1, 3):
    adjectives.append(input("Adjective? "))

animals.append(input("Animal? "))

for each in range(1, 4):
    verbs.append(input("Verb? "))
for each in range(1, 4):
    nouns.append(input("Noun? "))
for each in range(1, 3):
    adverbs.append(input("Adverb? "))
for each in range(1, 3):
    exclamations.append(input("Exclamation? "))

if animals[0][0] == 'a' or 'e' or 'i' or 'o' or 'u':
    preposition = 'an'


story = f"""
    The other day, I was really in trouble. It all started when I saw {article} {animals[0]} 
    {adverbs[0]} {verbs[0]} all the way down the hallway. "{exclamations[0].title()}!" I yelled. But all
    I could think to do was to {verbs[1]} over and over. Miraculously,
    that caused it to stop, but not before it tried to {verbs[2]}
    right in front of my {nouns[0]}. I was {adverbs[1]} panicked
    but there was nothing I could do. I grabbed my {adjectives[1]} {nouns[1]}, said 
    "{exclamations[1].title()}!" to my family, and high-tailed it out of the {nouns[2]}"""

print(story)
