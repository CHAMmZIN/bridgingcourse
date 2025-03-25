"""  3-8. Seeing the World: Think of at least five places in the world you’d like  
to visit.
 • Store the locations in a list. Make sure the list is not in alphabetical order.
 • Print your list in its original order. Don’t worry about printing the list neatly; 
just print it as a raw Python list. """

loactions = ['Taungyi','Innlay','Seoul','Tokyo','Aukland']
print(loactions)

print(sorted(loactions))

print(f"original list \n {loactions}")

loactions.reverse()
print(f"reverse order of list {loactions}")

loactions.reverse()
print(f"second time reverse call and order of list {loactions}")

loactions.sort()
print(f"after sorting in alphabetical order {loactions}")

loactions.sort(reverse=True)
print(f"after sorting with decreasing order {loactions}")

print(f" number of place that I like to travel {len(loactions)}")

print(loactions[-6])