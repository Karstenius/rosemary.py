from kitchen import Rosemary
from kitchen.utensils import Plate, Bowl, BakingTray, Oven
from kitchen.ingredients import Butter, Egg, Salt, Flour, Sugar, BakingPowder, ChocolateChips

# First and foremost, we need to preheat the oven to 175 degrees celcius.
oven = Oven.use()
oven.preheat(degrees=175)

# Take a bowl for the batter.
bowl = Bowl.use(name='chocolate chip cookie batter')

# Add the butter to the bowl, and mix in the sugar, little bits at a time. 
bowl.add(Butter.take('one part'))
for i in range(10):
    bowl.add(Sugar.take('20 g'))
    bowl.mix()
# Add the egg, and mix it into the batter.
for egg in Egg.take(2):
    egg.crack()
    bowl.add(egg)
bowl.mix()
# Add a pinch of salt to the batter, and remember to mix it.
bowl.add(Salt.take('pinch'))
bowl.mix()
# Add the chocolate chips, the flour and some baking powder.
for i in range(6):
    bowl.add(Flour.take('50 g'))
    bowl.mix()
bowl.add(ChocolateChips.take('200 g'))
bowl.mix()
bowl.add(BakingPowder.take('some'))
bowl.mix()

# Get a plate out to put the cookies on.
plate = Plate.use(name='chocolate chip cookies')

# Place 16 scoops of the batter on the baking tray, and put the baking tray in the oven for 10 minutes.
bakingtray = BakingTray.use()
for i in range(16):
    bakingtray.add(bowl.take('1/16'))
oven.add(bakingtray)
oven.bake(minutes=10)

# Remove the cookies from the baking tray and place them on the plate
plate.add(bakingtray.take())

# Serve!
Rosemary.serve(plate)
