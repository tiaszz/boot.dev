CARAVAN
Siege weapons (battering rams, catapults, etc) are special units in Age of Dragons. Let's write the logic for how they move around the map.

CHALLENGE
Complete the Siege, BatteringRam, and Catapult classes.

SIEGE CLASS
CONSTRUCTOR
Accepts two parameters (in order) and sets them as instance variables:

max_speed
efficiency
GET_TRIP_COST()
Calculates the cost of a trip:

(distance / efficiency) * food_price

It costs food to move siege weapons, those things are heavy!

GET_CARGO_VOLUME()
This method should be left empty. Use the pass keyword. Child classes will override this method.

BATTERINGRAM CLASS
CONSTRUCTOR
Calls the parent constructor, then sets the extra battering-ram-only instance variables as member variables.

GET_TRIP_COST()
Uses the parent method to calculate the cost of food for a trip, plus the extra cost of carrying a load.

The formula for calculating the cost:

base_cost + (load_weight * 0.01)

GET_CARGO_VOLUME()
Returns the cargo capacity in meters cubed. Get the volume of the battering-ram's "bed" (cargo area) by multiplying its area and depth. Every bed is 2 meters deep.

CATAPULT CLASS
CONSTRUCTOR
Calls the parent constructor, then sets the extra catapult-only instance variable as a member variable.

GET_TRIP_COST()
Do not override this method.

GET_CARGO_VOLUME()
Just returns the cargo capacity of the catapult. This is already set by the constructor.




