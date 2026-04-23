# Click The Button

A simple game about clicking a button. The objective of this game is to click the button 500 times.

# Installation

You will need the python file located at the top of the page along with 9 wires, and LCD 16x2 screen display, a singulr button, a raspberry pi, and a breadboard.

# How to wire the game

• 4 of the wires are on the side of the lcd 16x2

• 2 of the wires are on the top of the lcd 16x2 in the power and ground spots

• 3 of the wires are connected to the button to make the button do button things

• Make sure a raspberry pi is connected to your project indirectly thourgh the breadboard

# How the code works

First I imported a bunch of libraries, set the button input to wherever the leftmost wire on the button is connected, set up the lcd 16x2, and finally set the clicks to 0 to start the game.

Secondly I put a while true loop so then it won't end unless you complete a certain condition. (in this case its getting the clicks to 500)

Then I made a boost randomizer so that it'll have a 1% chance to boost your progress.

Fourthly I sensed that if the button is pressed it'll increase the clicks by 1 and I made sure to write it on the lcd 16x2 screen.

Finally Once you win it'll give you text congratulating you for a few seconds before disappearing to cleanup the raspberry pi and the lcd 16x2's data.
