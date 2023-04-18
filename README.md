----------------------------------------------------------------------------



 #########    #######     #########   ########    ########    #########   ##
#########    #########   #########   ##########  ##########  #########   ###
###          ###   ####     ###      ####  ####  ####  ####     ###      ###
####         ###    ###     ###      ###    ###  ###    ###     ###      ###
##########   ###   ####     ###      ###         ###    ###     ###      ###
 ##########  #########      ###      ###  #####  ###    ###     ###      ###
        ###  ########       ###      ###  #####  ###    ###     ###      ##
       ####  ###            ###      ####   ###  ####  ####     ###         
 #########   ###          #########  ##########  ##########     ###       ##
#########    ###         #########    ########    ########      ###      ###



----------------------------------------------------------------------------
                                BLESSING!
                        
                        A boredom-driven project
                      by Andrea Bellanca AkA Spigot
----------------------------------------------------------------------------

Welcome to Blessing, a random prompt generator meant to be used in riced shells.
Blessing has been made while ignoring my history class cause who cares about 
Italy teaming up with the USA and Nazi Germany at the same time??

Blessing is heavily inspired by Fortune, though it DOES NOT INTEND to replace or
rival it (let's face it, this is just a boredom project made by a script kiddo,
Fortune is on a whole 'nother level!). All it does is show one of how many
prompts one wants to add to blessing.txt on your terminal/shell. I've designed
it with FISH in mind as it's the shell I go to on my machines, but i guess it
would work on any shell that support greetings/startup prompts

----------------------------------------------------------------------------
                                   Q&A
----------------------------------------------------------------------------

Q] Why?
A] Boredom, brotha!

Q] Why adding a run.sh that just redirects to Blessing?
A] Good question. It's mainly cause on fish writing functions and aliases is
   basically just creating a script using built-in fish commands ([for example](https://imgur.com/a/ehmlCJY))
   so, instead of having to cd to the file and python3 the script i just chose
   to package everything in one folder and point the function to the run.sh
   script

Q] What does Blessing do?
A] Blessing is basically a low effort, boredom-driven Fortune lookalike. It
   takes its prompts from the blessing_prompts.txt and chooses to display one of
   them. It is randomized, so you shouldn't be seeing the same prompt over and
   over again. Theoretically it should be allowed to add as many prompts as you
   wish, there's only one way to find out! ;)

----------------------------------------------------------------------------
                             HOW TO USE BLESSING
----------------------------------------------------------------------------

Supposing you've already cloned the repo and have Python 3.10 or higher
installed, simply run the run.sh file or blessing.py. In order to edit, add or
remove prompts, simply edit the blessing_prompts.txt. To uninstall Blessing,
simply remove the spigot_blessing folder. Simple :)

I have little to no understanding on how to rice shells, I'm not sure how to do
stuff like [this](https://imgur.com/a/5R1EyY9) on BASH or ZSH, so I will only
provide steps to set up blessing on FISH's startup:

STEP 1] Open your terminal emulator
STEP 2] Run the following command:
      $ function fish_greeting
         ./path/to/spigot_blessing/run.sh
         end
STEP 3] Apply the changes you made to fish_greeting:
      $ funcsave fish_greeting
STEP 4] Enjoy your custom greeting messages, cause we're DONE!!! :D

Really, it's THAT easy!
















Need any help? Wanna say something to me? Then hmu on my socials! :D

 REDDIT = InTenebrisDomini (https://www.reddit.com/user/InTenebrisDomini)
 TWITTER = @spigotemcee (https://www.twitter.com/spigotemcee)
 EMAIL = andreabellanca@garibaldiliceo.net