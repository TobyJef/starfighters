* Welcome to Starfighters

Starfighters is a single player, turn based strategy game set in the depths of space. Take command as Admiral, your mission is to hunt down and destroy the opposing enemy fleet before the enemy can locate and destroy your own Starfighters.

The enemy Admiral has hidden their fleet within this star systems nebula cloud, and their precise location cannot be detected. but your scanners however can detect and return instances of any shots fired that have hit or missed their target.

Over the two game boards, use the tactical grids to record your shots on the enemy fleet, and the enemies attempt at your own Starfighters. All it takes is one direct hit to destroy a Starship, so speed an accuracy is of the most importance.

Best of luck Admiral.


** How to Play

- A brief History 

Starships is a single player game based on the classic pen and paper game of Battleships. In the original Battleships game the player is given two 10x10 grids. The first grid is used for the placement of the players five Battleships of varying sizes, and to mark the opponents shots against the player's ships. The second grid is used to mark down the players shot against the enemy ships and to record the outcome of a players turn. Turns for both the player and their opponent will result in a shot either hitting or missing a ship or resulting in a Battleship being sunk. The size of the ship determines the required amount of hits before a Battleship is sunk.

The classes of naval ships used in the original game were:

- Carrier (5 grid spaces)
- Battleship (4 grid spaces)
- Cruiser (3 grid spaces)
- Submarine (3 grid spaces)
- Destroyer (2 grid spaces)

Due to different publications found of the game Battleships found around the word, ship names, ship and grid sizes can vary.

- More information on the game Battleships can be found at [link to wikipedia.com](https://en.wikipedia.org/wiki/Battleship_game)

In my version Starfighters, the classic Naval game has been given a sci-fi twist, with a brief backstory and mission briefing to transport the player and game into the cosmos. 

A 5x5 grid size is being used for the players and the opponents ship placements. With the same basic rules of the game apply, find and destroy the entire enemy fleet, before they to destroy yours. Both sets of Starfighters are placed on the grids at random. 

** Features

- Game Design

The classic grid design from the game Battleships was used. This allows for precise placement of Player and Computer Starfighters, and Player shot placement.

A 5x5 grid size allows for a decent sized game board to accomodate single grid space sized Starfighters.
It would be my intention in a future update to add a 10x10 grid. As discussed further in the Future Improvement section.  

- Flow Diagram showing the intended flow of how the game would run from Start, to Finish.

![Flow diagram Beginning](documentation/flow-diagram-start.webp)
![Flow diagram Middle](documentation/flow-diagram-middle.webp)
![Flow diagram End](documentation/flow-diagram-end.webp)

- Future Improvements:

The ability for the player to choose between the game's set standard 5x5 or larger grid sizes, such as 6x6, 8x8 and 10x10.

The ability for the player to set their own starfighter positions on their tactical grid.

Larger Starfighters of taking up bigger grid spaces, and requiring more hits to be added, with an additional option of allowing the player choice of which Starfighters to be used in their game. 

Max amount of the larger Starfighters would only be available to the player when playing on the 10x10 grid.

Difficulty option for the player to set the number of enemy ships to allow for increased or decreased game difficulty.

The use of an outside library such as colorama to introduce some colour and futher design into the game.

Introduce a replay game function to allow the player to reset the game, and play a new game of Starfighters.

** Technologies Used

Starfighters was written using the Python programming language.

** Testing

- Bugs

Solved Bugs

Issue found when trying to deploy my app on Heroku. I needed to reach out to Tutor Support for advice, the bug could have be an issue from using the pip3freeze command while composing my app on codeanywhere. Sean from Tutor Support, suggested to remove the installed packages and to re try deployment with a new set of packages. Once replacing what was suggested as the issue and attempted re-ployment on Heroku, the apps deployment was finally complete. Further information on this bug can be found in the credit section at the end of the ReadME.

![heroku error](documentation/heroku-error.webp)

The image of the below bug found during testing, would occur when testing the Hit, Miss, Destroyed markers against the board whilst in early development. Once the final shot on a ship was completed resulting in the ship being destroyed. All remaining empty spaces would change to the Destroyed marker.

The issue found due to a mispelling and once corrected, the code would run as designed. The Destroyed element was eventually removed in this current iteration of Starfighters, due to design choice of the game overall. Preferring to use a smaller grid board and smaller sized ships, for game optimization when being played. It would be my intention in a future update to bring back the destroyed marker into the game.

![Ship destroyed bug](documentation/ship-destroyed-bug.webp)

An example of a planned larger sized starfighter's random placement by the program, being placed over two grid rows resulting in a split Starfighter.

![Split Starfighter bug](documentation/split-ship.webp)

An example of a planned larger sized starfighter's random placement by the program, being placed outside of the confines of the planned grid size.

![Out of Bounds Starship](documentation/out-of-bounds.webp)

The above examples of the larger sized Starfighters was eventually dropped in the current version of this game. But with a future plan to reintroduce them.

- Remaining Bugs

A remaining bug found within the game at the moment has come about by myself attempting to structure the code layout for easier reading. However in doing this it has resulted in the base game being able to run. Due to time, I was unable to perform a full de-bug and re-write of the code.

Validation

- PEP8
![PEP8 Validation](documentation/linter-pass.webp)

- Deployement

- Deployment to Heroku

Ensure all relevant packages for project are installed, and make any final commits and push the update through to Github.

Create or Sign in to your Heroku account.

Click on the Create App option and give your App a name for your deployment, then selcet your region from the provided drop down box. As App names need to be unique, there maybe a possibility that your preferred name may already be taken. If that is the case, take a moment to think of a new name.

Whilst on the main project page, there are a extra steps to take on the Heroku platform before we can deploy our app. Which can be done by going to the settings tab. 

Underneath App Information, you will find Config Vars.

Click on the reveal Config Vars button, within the KEY box, add PORT and then add 8000 to the VALUE box. Then click add.
This is done to due to a warning found on the Deploying our Project Part 2, video page. As it was found by not adding this there was a possibility that the deployment may fail.

![ Add the config-vars image](documentation/config-vars.webp)

Afterwards we need to turn our attention to installing some buildpacks we need to run our app outside of the requirements.txt file. First we want to install the python buildpack, followed by the node.js buildpack, then click the add buildpack button.

![Add the buildpacks image](documentation/buildpacks.webp)

Once the buildpacks have been added, scroll back to the top of the page and head over to the deployment page, by clicking on the Deploy tab.

Within the Deployment Method, we will select Github as our deployment method by clicking on the Github option, then click the Connect to Github button below. This will connect to our Github repository and allow us to proceed to the next step.

Below we will find the App connected to GitHub section. Enter the name of the project repository in the search bar and click the search button. Once the project's repository is found, we can then click the connect button to link our Heroku app with the code found in the Github project repository.

Afterwards proceed to scroll down the page and choose if would prefer Automatic or Manual Deployment. We select automatic so that any further Git commit and push's on the project can be automatically deployed.

Finally below at the end of the page we have reached the Manual Deploy section where we click on the Deploy Branch button so that we can initiate our apps deployment.


- Forking and Cloning

How to Fork the repository:

Log into Github.

Go to the repository for this project, (https://github.com/TobyJef/starfighers)

Click the Fork button found on the right of the page underneath the upper navigation bar.

- How to Clone the repository:

Log into GitHub.

Go to the repository for this project, (https://github.com/TobyJef/starfighters)

Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.

Open a terminal in your code editor type 'git clone' into the terminal and then paste the link you copied from the Github repository. Press enter to change the current working directory to the location you want to use for the cloned directory. 


- Credits

- Sean from Tutor Support.

 I reached out to Tutor Support after I attempted to deploy this project on Heroku.
Whilst following through the Deploying our Project, Part 1 video from the Love Sandwiches Walkthrough project,
upon my first attempt at deployment, the deployment failed due to the below error:

ERROR: Could not find a version that satisfies the requirement python-apt==2.4.0+ubuntu1 (from versions: 0.0.0, 0.7.8)
ERROR: No matching distribution found for python-apt==2.4.0+ubuntu1
! Push rejected, failed to compile Python app.
! Push failed.

Before finishing work on my project for the night I sent an out of hours message off to Tutor Support to ask for some assistance,
as after searching resources such as Stack Overflow and the code institute community channels within Slack. I was yet to find a solution that fixed the issue, although other students appeared to have the same problem.

When I resumed work on this project the following morining I had a reply from Sean, who suggested that after looking at the Starships repository, Sean believed that the issue was possibly caused from using the pip3 freeze > requirements.txt whilst constructing my project on Code Anywhere and that by using the pip3 freeze > requirements.txt had installed unnecessary packages into the program, which has caused the error. Sean suggested that a possible fix would be to, replace the packages with those found currently in the requirements.txt file and to try redeployment again.

After following Seans instructions and attempting redeployment on Heroku, the deployment was successful.

![pip3freeze](documentation/pip3freeze.webp)
![heroku error](documentation/heroku-error.webp)
![heroku fix](documentation/heroku-fix.webp)
