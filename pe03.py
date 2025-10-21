#Menu
print("Choose a program to run:")
print("1. People list")
print("2. Animal list ")
print("3. ")
print("4. ")
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

    pass