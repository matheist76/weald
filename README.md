# Weald
A weald is a woodland. It also rhymes wwith yield which means to give way to arguments, demands or pressure.
So this webapp is designed to help a GM of a Root RPG create characters. Layout their woodland. Etc. Look 
this isn't going to be pretty or very good. I don't do this stuff for a livings so yeah it's going to be 
absolute crap but if you want something better do it yourself don't bug me. Deal with it. PS I'm also 
terrible at grammar and spelling. If this bothers you copy someone elses stuff you lazy git. 

Structure

Weald  - Main Program links to others
-> Players section: Used to allow players access to their character sheets. Create their own characters (given GM 
constraints) etc.
-> GM section: Used to build characters, setup character contraints for players to build characters, create vagabond 
types etc.

So this is going to be complicated. So rather than put this into a text file I've used a mind map online 
program. Here is the link. Hope this helps to understand the program. https://mm.tt/map/2331257264?t=HO5wlcReZp

I think the hardest problem to solve for this project will be the db. 


-- Playbook --
Okay so let's try and bring this all together.
These db models are what is used to define a particular playbook. Now of the worst of these project playbooks is the
"The Pirate" The breaks in normal rules in this monstrosity just ... so what is in a playbook? Take the background. We
use background questions and answers to create a background for the character so for the 3rd Question we have "What
happend to your captain?" then 5 choices. None of these match with any other vagabond playbook. So we need the playbook
to limit from the traits what the player can choose.
# TODO 1. Create Name & Description - strings
# TODO 2. Example outlines - player makes their own.
# TODO 3. Background - List of 5 Questions and the related answers. Note: Q4&5 change prestige so maybe need a way to signify this. 
# TODO I need a faction table then I need someway to link that with the question. mmmmmmm
#4. Drives - List of 4 choices where the user can select only 2
#5. Nature - List of 2 choices where the user picks just one.
#6. Connections - Name which can't be a primary key, description and user text.
#7. Stats - plus or minus for each stat
#8. Harm - don't touch I don't think.
#9. Roguish Feats - A direction with some feats that can be preselected.
#10. Weapon Skills - Like Roguish feats except that skills aren't preselected the available options are in bold.
#11. Moves - A direction with maybe some chosen. At this point to I find out different present selected but allow
#....for other options to be selected at a later point. You can gain other moves. See P175 of Core Book.
#12. Equipment - Each playbook has some starting equipment stuff but the only thing that changes is the Starting value.
#....However with a few move options you get stuff. Example Pirate you get a ship, Prince gets a heirloom weapon.



Todo
 * Create the basic db tables. The 1st and hardest one with be the traits db. Once that's done then it will 
the rest will just fall into place. The playbooks are simply pick and chose from the traits db.
 * Create Playbooks

1st start creating the start page. Nothing fancy just a couple of links
So index.html
-> player.html
-> gm.html
-> settings.html
Please insert expletives here. Man it took longer than I admit to get that .... done. Yes I really am that dum. Okay
now onto working out basic stuff.

22/6/2022
   ground/models/traits.py is used by playbook to fill out the character sheet. So only stuff that doesn't change goes 
   here. The only way to change data in traits will be through admin. Think of traits as ingredents which the method 
   playbook turns into a character sheet.

   ground/models/playbook.py the stuff here will be used by the playbook form to create the character sheet. So this is
   specific to a particula playbook.

   ground/models/character_sheets.py this db table will hold the character sheets for all of the players. So it will 
   contain the varible and the constants. 


traits.py 


playbook.py


character_sheets.py


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

