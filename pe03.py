#Menu
print("Choose a program to run:")
print("1. People list")
print("2. Animal list ")
print("3. Duplicate list")
print("4. Food tuple")
print("5. ")

choice = int(input("Enter your choice (1-5): "))

if choice == 1:
    #---PEOPLE LIST---
#Make a list w/ 3 people and print it 
#replace a person that cant make it w/ another person ext. list[2] = 'Bob'
#.insert[0] add new guest to begining 
#.insert(middle, "bob") add to middle
# .append() add to end 
#Print new list 
# Use pop() to remove guests till only 2 remain

    people = ['bob', 'steve', 'troy'] #made a list of 3 people to invite to dinner 
    print("Original list: ", people) # Print that list 

    people[1] = 'sarah' #replace steve w/ sarah 
    print("Updated list:", people) #print updated list 

    people.insert(0, 'gabrielle') #Insert to begining of list 
    people.insert(len(people)//2, 'lebron') #Insert to the middle using len(people)//2 to find halfway point
    people.append('Tuan')#Insert to end of list
    print("New list:", people) #print new list 

    while len(people) > 2: #While the length of the list is greater than 2 
        removed = people.pop() #Removes last person from list till theres only 2 left
        print(f"Sorry {removed.title()} I can’t invite you to dinner.") # print one by one of people removed till 2 left

    print("Final list:", people) #print final list

elif choice == 2:
    #--- ANIMAL LIST--
    animals = ['lion', 'tiger', 'jaguar', 'cheetah', 'cougar', 'panther', 'leopard' ]#List of 7 animals (BIG CATS)

    print("The first three animals in the list are:", animals[:3]) #Print first 3 animals 

    middle_index = len(animals) // 2 #Finds the middle of the list
    print("Three animals from the middle of the list are:", animals[middle_index-1:middle_index+2]) #Slices 3 items centered in the middle

    print("The last three animals in the list are:", animals[-3:]) #Print last 3 animals

elif choice == 3:
    #---duplicate-list---
#Start with a list of numbers that have duplicates
#Make an empty list to hold numbers that appear more than once 
#Go thru each number in list one by one 
#For each number count how many times it apears in original list 
#If number appears more than once and not in duplicate list , add it 
#once its done print the duplicate list

    numbers = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]

    duplicates = [] #Empty list to store duplicates 

    for num in numbers: #Go through each number in list 
        if numbers.count(num) > 1 and num not in duplicates: #Check if it appears more than once and isn't added
            duplicates.append(num) #Add to duplicates

    print("Duplicate numbers:", duplicates)

elif choice == 4:

    foods = ("spring rolls", "chicken feet", "beef", "soup", "fried rice") #Foods in a tuple
    print("Menu:")  # print header once
    for food in foods: #For loop to print each food one by one 
        print(food)

    #foods[0] = "egg rolls" #trying to replace item but you cant replace in tuple
    #print(food) #there is an error in the terminal 

    foods = ("egg rolls", "chicken feet", "beef", "soup", "noodles") #new tuple w/ 2 different foods 
    print("\nRevised menu:")  # print header once again
    for food in foods: #For loop printing new foods one by one
        print(food)








    pass