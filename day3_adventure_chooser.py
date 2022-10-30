import time

adventurers_name = input('Enter the name of your andventurer: ')
wealth = 0

print('You have been wandering for hours in search of the Lost Treasure.\nAll so that you can get your little sister the cancer treatment she needs.')
time.sleep(2)
print(f'While you are close, there are many trials you will have to face, {adventurers_name}.')
time.sleep(2)

choice1 = input('Oh look! There is a boat. Will you take it or keep walking by foot? TAKE or NO: ')
time.sleep(2)
if choice1.lower() == 'no':
	print('You come across a pedestrian offering free horserides. She sees you and that you look tired, insisting you take one.')
	choice2 = input('You come to a crossroad and are unsure of which way to go. LEFT or RIGHT? ')
    
	if choice2.lower() == 'left':
		print('You are approaching the shore! You see a piece of inked paper tucked neatly inside a bottle. You grab it.')
		choice3 = input('It appears to be a map to a shipwreck! But there are two paths. Which one do you take? LEFT or RIGHT? ')

		if choice3.lower() == 'left':
			print('You followed the map to the shipwreck. You find a couple golden dubloons and take them for good measure.')
			wealth =+ 3
			choice4 = input('Do you want to continue scouring the boat or leave? CONTINUE or LEAVE: ')

			if choice4.lower() == 'continue':
				print('You continue scouring the boat wreck and find and see a chest.')
				choice5 = input('Do you search the chest or look elsewhere? CHEST or ELSEWHERE: ')

				if choice5.lower() == 'chest':
					print('You load your pocket and bag with all of the gold, jewelry, and souvenirs you can grab.')
					wealth += 500
					choice6 = input('You see a boat. Its just sitting there, free for anyone to take. Do you take it? YES or NO: ')
					if choice6.lower() == 'no':
						choice7 = input('You were rewarded for not stealing his boat. The man offers it to you in exchange for 50 coins. Accept offer YES or NO: ')
						if choice7.lower() == 'yes': 
							wealth -= 100
							print(f'You ride away with {wealth} coins for your family.')
						else:
							print(f"You leave and find a phone. You call the government to come pick you up. Since you are a tax paying citizen, it is free. You walk away with {wealth} coins for your sister's treatment.")
					else:
						print(f'The man killed you and took your {wealth} coins.')
				else:
					print(f'You accidentally drowned yourself trying to leave. You lost {wealth} coins.')
			else:
				print(f'You were killed leaving the area and lost your {wealth} coins.')
		else:
			print('The route lead you directly to the pirates new ship. The put a giant hole through your body.')
	else:
		print('You entered the pirates territory. They made it their mission to skin you alive.')
else:
	print('You were chased and hunted by a horde of pirates. Yeah. That was their boat.')



