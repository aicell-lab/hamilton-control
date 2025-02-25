from pylabrobot.liquid_handling import LiquidHandler
from pylabrobot.liquid_handling.backends import Vantage
from pylabrobot.resources.hamilton import VantageDeck

backend = Vantage()
lh = LiquidHandler(backend=backend, deck=VantageDeck(size=1.3))

print(lh.deck)

from pylabrobot.resources import (
  TIP_CAR_480_A00,
  PLT_CAR_L5AC_A00,
  Cor_96_wellplate_360ul_Fb,
  HTF,
)
tip_car = TIP_CAR_480_A00(name="tip carrier")
tip_car[0] = HTF(name="tips_01")

lh.deck.assign_child_resource(tip_car, rails=3)
plt_car = PLT_CAR_L5AC_A00(name="plate carrier")
plt_car[0] = Cor_96_wellplate_360ul_Fb(name="plate_01")
lh.deck.assign_child_resource(plt_car, rails=15)

lh.summary()