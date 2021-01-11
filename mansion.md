# Mystery randomizer
## Objects
### Small objects
Good for discrete murder weapons and or tools. Things you might find in a drawer or other small cabinet
Roll D12
	1 candle stick
	2 white servants cloth or knitted cloth
	3 gold picture frame
	4 decorative plate
	5 small horse statue
	6 curtain closing rope
	7 fake fruit from fruit bowl
	8 urn
	9 heavy metal key
	10 tea saucer
	11 angel statue
	12 a dusty leathered bound book

### Large objects



## Incidents
If one were to simply sit in a room looking onto a hallway or another room. What might one see? Replace A and B for characters or servants.

Roll D20
	1 A runs down the hall shortly followed by B.
	2 A runs down the hall shortly followed by many people.
	3 A runs down the hall shortly followed by B running down the hall in the other direction.
	4 Many people run down the hall at once.
	5 A door slams.
	6 A window panel slams open and or closed with the wine
	7 secret door (flush the the wall) slides open
	8 a book falls off a shelf
	9 The doorbell chimes through the whole house
	10 A grandfather clock rings
	11 A bird crashes into the window
	12 A mouse gets out of one small whole, crosses the room, and enters another hole
	13 Floorboards creak
	14 A painting swings croakidly
	15 A swinging chair swings
	16 Sparks fly from the fire place
	17 




Say we were to write a murder mystery for nanogenmo
We need:
	C characters
	O objects
	R rooms
	I incidents
	A starting adverbs

Each sentence will be an action. They start with an adverb sometimes (suddenly, then, later, simulatenously....):
	10C chacracters do something by themselves (Suddenly, X hears/sees\ something. laughs, chuckles, giggles, screams, sings, dances, yawns)
	5CO characters interact with objects (grab, throw, place, move)
	10CC characters interact with each other (talk, fight, flirt, argue, negotiate)
	10CC actions for characters to do to another character (kill, glance at, yells at, walks towards, pushes, bullies, belittles)
	10CR characters can move from a room to another (if not locked, can add adjective gracefully, hurriedly...)
	10CR characters can lock or unlock a room (can add an adjective, silently, hurriedly,)
	IR An incident occurs in a room

7 different actions
10 chacracters
20 rooms
20 objects
20 incidents



# Code strucutre

1. Determine starting parameters
	Pick cast of 20 characters out of preset list
	Pick 20 rooms from preset list
2. repeatedly pick a sentence from a list of sentences like this
	ADVERB, CHARACTER VERB_TO CHARACTER_OTHER in ROOM.
3. pass sentence through functions that will replace each capitalized work appropriately
	ADVERB: Suddenly, Later, Then...
	CHARACTER: randomly pick from a preset list for that bike
	CHARACTER_OTHER: Pick from a list but don't match CHARACTER
	VERB_TO: slaps, whispers to, kills, etc...


	ROOM: pick a room, add some random number of qualifiers to it.





Rooms
	are connected to other rooms
	Maybe make a random network with high clustering coefficient, max degre of 4
	locking a room is boolean code on the node
	rooms have qualifications
		color
		size
		carpeted or not
		weather (drafty, cold, warm, damp)
		cleanliness (filled with cobwebs, dusty, spnaking clean)





