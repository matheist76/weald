# Weald
A weald is a woodland. It also rhymes wwith yield which means to give way to arguments, demands or pressure.
So this webapp is designed to help a GM of a Root RPG create characters. Layout their woodland. Etc. Look 
this isn't going to be pretty or very good. I don't do this stuff for a livings so yeah it's going to be 
absolute crap but if you want something better do it yourself don't bug me. Yeah this is going to be crap. Deal with it.
PS I'm also terrible at grammar and spelling. If this bothers you copy someone elses stuff you lazy git. 

Structure

Weald  - Main Program links to others
-> Players section: Used to allow players access to their character sheets. Create their own characters (given GM constraints) etc.
-> GM section: Used to build characters, setup character contraints for players to build characters, create vagabond types etc.

Todo

1st start creating the start page. Nothing fancy just a couple of links
So index.html
-> player.html
-> gm.html
-> settings.html
Please insert expletives here. Man it took longer than I admit to get that .... done. Yes I really am that dum. Okay
now onto working out basic stuff.

Vagabond = player. All players play as Vagabonds so while for other stuff, for example the board game, Vagabonds and 
players aren't equivalent they are here. At this point we learn that Magpie Games hates programmers. Or at least doesn't
think about them. I think if you can do this shit without bashing your brains out then you are far better than me.
So lets look at Details. This should be a non issue. Everyone just describe your character. Yeah na. We have suggestions
or at least that's what I think they are and each are different for each player type. So yeah this isn't going to be simple.


Vagabond Types: 

models
Drives
name = models.CharField(max_length=50, primary_key=True)
description = models.CharField(max_length=180)

DB Models

