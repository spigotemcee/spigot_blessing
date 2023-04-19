#############################################################################
################### LITERALLY JUST IMPORTING RANDOM SHIT ####################
#############################################################################

import os
import random
import distro
import json

#############################################################################
################ IT'S SO SMALL!!! (that's what she said...) #################
#############################################################################

bdata = os.path.expanduser('~/spigot_blessing/data/BLESSINGS.JSON')
   # Turn bdata into an absolute path
blist = ["var1", "var2", "var3", "var4", "var5", "var6", "var7", "var8", "var9", "var10", "varOS"]
   # Used to choose between entires, edit for how many entries you have in BLESSINGS.JSON
brandom = random.choice(blist)
   # Literally just a randomizer

with open(bdata, "r") as bread:
   if brandom == "varOS":
      print("↑ Nice to see a " + distro.name() + " user ;) ↑")
   else:
      bdict = json.load(bread)
      print(bdict[brandom])
