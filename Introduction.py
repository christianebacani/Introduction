print("Hello I am Christiane Rhely Joselle A. Bacani")
input("Press enter if you want to know me more ^^ : ")

print("1.) My Strengths\n2.) My Weaknesses\n3.) My Pet Peeves\n4.) My Fears\n5.) My Passion\n6.) My Hobby\n7.) About me\n8.) Exit")
userChoice = int(input("Enter your choice here : "))

if userChoice == 1:
    print("STRENGTHS\n1.) Commited to work\n2.) Consistent\n3.) Calm under pressure\n4.) Optimistic")
elif userChoice == 2:
    print("WEAKNESSES\n1.) Needs a lot of attention\n2.) Overthinker\n3.) Doesn`t know how to set boundaries\n4.) Saying sorry all the time\n5.) Can`t express my problem\n6.) Observant\n7.) Loving too much without reserving any care to myself\n8.) Vulnerability")
elif userChoice == 3:
    print("PET PEEVES\n1.) Hot environment\n2.) Noisy surroundings\n3.) Smelly area\n4.) Slow Internet")
elif userChoice == 4:
    print("FEARS\n1.) Snakes\n2.) Ghost\n3.) Afraid that loved ones might leave me someday especially my girlfriend\n4.) Changes\n5.) Loneliness\n6.) Harsh Words")
elif userChoice == 5:
    print("PASSIONS\n1.) Coding\n2.) Gaming")
elif userChoice == 6:
    print("HOBBIES\n1.) Programming\n2.) Playing games\n3.) Watching series\n4.) Playing chess")
elif userChoice == 7:
    print("About me\n\nI am Christiane Rhely Joselle A. Bacani, 2nd year computer science student. Lives in Balanga City, Bataan\nA coding virtuoso with a passion on gaming. Has a lovely, sweet, caring, and gorgeous girlfriend and soon to be wife (Rica Mae G. Flores).\nDreams to become a Senior Data Analyst at Google. Loves to play games to forget about problems and anxiety and a happy-go-lucky person.\nSpecial thanks to my girlfriend (Rica Mae G. Flores) for supporting me, caring, reminding and be with me thru the good and bad times this project is for you ^^.")
elif userChoice == 8:
    print("Successfully Exited!")
else:
    print("Invalid Choice!")
