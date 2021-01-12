from kitchen import Rosemary
from kitchen.utensils import Pan, Plate, Bowl
from kitchen.ingredients import Butter, Egg, Salt, Flour, Milk

# Pancakes for multiples of 8 
pancakes = 5

# Take a bowl for the batter
bowl = Bowl.use(name='pancake batter')

# Add all the eggs to the empty bowl and mix
for egg in Egg.take():
    egg.crack()
    bowl.add(egg)

# Whisk the eggs until frothy 
bowl.mix()

# Add a dash of salt and mix in the flour per 50g to the batter
bowl.add(Salt.take('dash'))
for i in range(5 * pancakes):
    bowl.add(Flour.take('50 g'))
    bowl.mix()

# Add in the milk, by halves
for i in range(2 * pancakes):
    bowl.add(Milk.take('250 ml'))
    # Mix the batter thoroughly before adding the second half of milk, and then mix thoroughly when all the ingredients are in.
    bowl.mix() 

# Take a plate
plate = Plate.use(name = 'pancakes')

# Get the pan ready, and make eight pancakes
for i in range(8 * pancakes):
    # Make a single pancake
    pan = Pan.use(name='pancake')
    pan.add(Butter.take('small slice'))
    pan.add(bowl.take('1/' + str(8 * pancakes)))
    # Cook the pancakes for 30 seconds, and flip after. Do this 4 times to cook both sides 60 seconds and golden brown.
    for i in range(4):
        pan.cook(minutes=0.5)
        pan.flip()
    plate.add(pan.take())

# Serve!
Rosemary.serve(plate) 