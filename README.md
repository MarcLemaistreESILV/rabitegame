# rabitegame
top secret
Marc Lemaistre 22170166

****LICENSE****
no license, you can use it as you want I don't care

****GAME FUNCTOIONNING*****
THis projecte called rabbit game is about trying to make as many rabbit as possible
simply the payer has three actions: hide, love or alert he also can move
there is a map with features on it.
So there are three features:
-bush, where you can hide up to 3 rabbits
-wholes, inifit number of rabbit can hide
-rabbit
Rabbit can move, alert and hide. They cannot love however it is easy to add (the code is made for it)
Rabbit have a lot of parameters because the code tends to be more an evoluting AI than a game. 
So rabbit can repoduces giving speed, calling_eagle and for the futur color parameters (as a witness for the experience).
Rabbits can't see how many rabbits are in the bushes. So contrary to the payer, the aciton alerting ohter rabbits is very effective.
That was for the parameters now let's see how the code works,
the game is only about absolute postions. I tried displaying a gride meant to be moving on the futur to have an open map but it wasn't effiicient in small maps.
However it is still possible. That is the reason why bushes and wholes are generated automaticly, so the map can be open. It's also why in the first versions published on github
you see the name relative_x in the rabbit's parameters.
Finally I want to improve on the changing color. Indeed I didn't find the lirary I was looking for. So what I want to do is changing the color of the rabbits to make the color
also an evlotuive parameter.

