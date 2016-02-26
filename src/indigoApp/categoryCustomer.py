import random

categories = ['Appliance','Bath','Building Materials','Decor','Doors and Windows',
        'Electrical','Flooring','Heating and Cooling','Kitchen','Lighting and Fans','Lumber',
        'Home Maintenance', 'Outdoor','Plumbing', 'Seasonal','Storage']

noCategories = len(categories)
count = 1
print "Id,CustomerId,Category"
for i in range(1, 108):
    assignedCategories = random.randint(1,4)
    for j in range(0, assignedCategories):
        category = random.randint(0, noCategories-1)
        print count, ",", i, "," + categories[category].lower()
        count += 1


