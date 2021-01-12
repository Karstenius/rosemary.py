from kitchen.ingredients.Ingredient import LemonJuice, LemonZest
from kitchen import Rosemary
from kitchen.utensils import Plate, Bowl, PieDish, Oven, Fridge
from kitchen.ingredients import Butter, Egg, Salt, Flour, Sugar, Apple, Lemon, Cinnamon, Cornstarch, Water

# Put some water into the fridge
fridge = Fridge.use()
bowl_water = Bowl.use(name = 'water')
bowl_water.add(Water.take('500 ml'))
fridge.add(bowl_water)

# Now we need to preheat the oven to 180 degrees celcius.
oven = Oven.use()
oven.preheat(degrees=175)

# Start of the dough, by adding flour and salt, and mixing it quickly.  
bowl_dough = Bowl.use(name = 'pie dough')
bowl_dough.add(Flour.take('300 g'))
bowl_dough.add(Salt.take('teaspoon'))
bowl_dough.mix()
# Gradually add butter into the bowl, and knead the dough.
for i in range(10):
    bowl_dough.add(Butter.take('25 g'))
    bowl_dough.mix()
# Take the water out of the fridge, and gradually add it to the bowl, and knead it further.
fridge.take()
for i in range(5):
    bowl_dough.add(Water.take('1/5'))
# Put the bowl with dough into the fridge to chill.
fridge.add(bowl_dough)

# Get a bowl for the filling.
bowl_filling = Bowl.use(name = 'apple filling')
# Peel and slice the apples.
for apple in Apple.take(6):
    apple.peel()
    apple.slice()
    bowl_filling.add(apple)
# Zest and juice half of the lemon, the part that goes into the filling.
for lemon in Lemon.take(1):
    lemon.zest()
    lemon.squeeze()
    bowl_filling.add(LemonJuice.take('1'))
    bowl_filling.add(LemonZest.take('1/2'))
# Add the sugar, cornstarch, salt and cinnamon to the filling.
bowl_filling.add(Sugar.take('150 g'))
bowl_filling.add(Cornstarch.take('spoonful'))
bowl_filling.add(Salt.take('pinch'))
bowl_filling.add(Cinnamon.take('teaspoon'))

# Prepare the apple pie itself. 
pie_dish = PieDish.use(name = 'apple pie')
fridge.take()
pie_dish.add(bowl_dough.take('3/4'))
pie_dish.add(bowl_filling.take())
pie_dish.add(bowl_dough.take('1/4'))
# Finish of the apple pie with an egg, some sugar and the lemon juice and zest.
bowl_egg = Bowl.use(name = 'egg')
for egg in Egg.take(1):
    egg.crack()
    bowl_egg.add(egg)
pie_dish.add(bowl_egg.take())
pie_dish.add(Sugar.take('spoonful'))
pie_dish.add(LemonZest.take('1/2'))

# Put the apple pie into the oven for 60 minutes, and take it out after.
oven.add(pie_dish)
oven.bake(minutes=60)
oven.take()

# Take a plate, and put the apple pie on the plate
plate = Plate.use(name = 'grand apple pie')
plate.add(pie_dish.take())

# Serve!
Rosemary.serve(plate)


