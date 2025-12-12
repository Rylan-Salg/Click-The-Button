# Click The Button

I made a simple little game where you gotta click a button 500 times

Sounds easy, and that's because it is easy, I mean i gotta present this in about 3 minutes of time so it's gotta be easy

There should be a video in the added files area of a small demonstration on how it works

# How The Game Works

It's pretty simple, you just click a button and threre is a 1% chance a boost will appear for a couple seconds which will give you about 150 clicks

# How the wiring works

There's only 9 wires, 1 button, and an LCD 16x2 screen display

4 of the wires are on the side of the lcd 16x2

2 of the wires are on the top of the lcd 16x2 in the power and ground spots

3 of the wires are connected to the button to make the button do button things

# How the code works

First I imported a bunch of libraries, set the button input to 27 (wherever the leftmost wire on the button is connected), set up the lcd 16x2, and finally set the clicks to 0 to start the game

Secondly I put a while true loop so then it won't end unless you complete a certain condition (in this case its getting the clicks to 500)

Then I made a boost randomizer so that it'll have a 1% chance to boost your progress

Fourthly I sensed that if the button is pressed it'll increase the clicks by 1 and I made sure to write it on the lcd 16x2 screen

Finally Once you win it'll give you text congratulating you for a few seconds before disappearing to cleanup the raspberry pi and the lcd 16x2 because if that doesn't happen it could potentially explode or shock you if your try to adjust the already running wires
