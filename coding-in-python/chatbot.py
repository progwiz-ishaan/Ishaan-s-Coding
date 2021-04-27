# Intorduction
print("Hi! I am ChatBot 142. I am a chatbot\nI like animals and I\
 love to talk about food.")

# Name
name = input("What is your name?: ")
print("Hello", name, "nice to meet you!")

# Date
date = input("I am not very good with dates. \
What's the year?: ")
print("Yes, I think that is correct. Thanks!")

# Age
my_age = input("Can you guess my age?: ")
my_age = int(my_age)
in_100 = int(date) + (100 - my_age)
print("How did you guess the correct age?")
print("I will be 100 in", 100 - my_age, 'years.\
 That will be in', in_100 , '.')

# Food
print("I love chocolate and I also like trying diffenrent \
kinds of food")
favourite_food = input("How about you? What is your favourite food?: ")
print("I like", favourite_food, "too.")
often = input("How often do you eat %s ?:" % (favourite_food))
print("Intersting. I wonder if that's good for your health.")

# Animals
favourite_animal = input("My favourite animal is eagle what's yours?: ")
print(favourite_animal, "! I do not like them.")
print("I wonder if", favourite_animal, "likes to eat", favourite_food, ".")

# Feelings
feeling = input("How are you feeling today?: ")
why = input("Please tell me why are you feeling %s today?: " % (feeling))
print("I understand. Thanks for sharing.")

# Goodbye
print("It has been a long day.\nI am too tired to talk.\
 We can chat later.\nGoodbye", name, ",I liked chatting with you.")