#copying a list

my_foods = ['pizza', 'falafel', 'carrot cake']# source
friend_foods = my_foods[:] # start zero through the last  item
print("My food list")
print(my_foods)
print("friends's food list")
print(friend_foods)
my_foods[0]='cheese pizza'
print(my_foods)
print('friends food list',friend_foods)

my_foods.append('connoli')
friend_foods.append('ice cream')

print("after appending elemwnt into list")
