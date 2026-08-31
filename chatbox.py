print("hello i am AI bot. What's your name? :")

name = input()

print(f"Nice to meet you,{name}!")

print("how are you feeling today? (good/bad)")

mood = input().lower()

if mood == "good" :
    print(" I'm glad to hear that")

elif mood == "bad" :
    print(" I'm  sorry to hear that. Hope things get better soon")

else:
    print("i see. Sometimes it's hard to put feelings inot words")

print(f"it was nice chatting with you {name}. Goodbye!!!")
