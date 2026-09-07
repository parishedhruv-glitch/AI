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
print("What is the temprature right now")
Temp = int(input())
if Temp > 30 :
    print(" It is a very hot day ")

elif Temp >= 20 :
    print(" It is a normal day")

else:
    print("it is a cold day")


print(f"it was nice chatting with you {name}. Goodbye!!!")
