# TicTacToe Python

Welcome to the TicTacToe game made in Python Language, by Haris Noori.

TicTacToe is world's largest playing game, on paper and pens, boards, walls and floors, but here it is, the game is now available to play on online website. This is a two player game, so you must need an opponent, to play the game.

Link to the game: [PLAY](https://tictactoe-python-acf2f2ecbb0f.herokuapp.com/)

## Am I Responsive Screenshot
![Responsive Mockup](https://github.com/Haris-Noori/tictactoe-python/blob/main/assets/img/AmIResponsive.png)


## Features
- A user can be an player X or player O, so there are two players
- both players will get the chance to put their mark on the board one by one
- they can only do it once, can't change the position,
- a user can only input integer value from 0 to 8, no alpha, no alphanumeric or negative integers,
- All datatype checkes have been completed and tested

## Fixed & UnFixed Bugs
- There no Unfixed bugs, but there was a bug at the end of final review. So there are only 0 to 8 integers allowed but when I tried to put value 9 it showed that it is not acceptable but it still pass the turn to next player. So I figuered it out, the solution was to put a check at O'player, if value is nine then it should also let the user try again, not just skip the turn.

## Code Institute Python Linter Screenshot
![Python Linter](https://github.com/Haris-Noori/tictactoe-python/blob/main/assets/img/CI_python_linter.png)

## Deployment
- Login to Heroku account
- Click "New" in the Heroku dashboard and select ”Create new app”
- Write a name for the app and choose your region.
- then click ”Create App”
- In settings, two build pack scripts were added: Python and Nodejs (in that order)
- Connect your Heroku with your GitHub account and the repository you are working on
- Then at the bottom, you can do a manual deployment or set it to automatic deployment to deploy every time your repo is updated.
- In my case I chose manual deployment
![Heroku Deployment](https://github.com/Haris-Noori/tictactoe-python/blob/main/assets/img/deployment.png)

## Credits
- To [StackOverFlow](https://stackoverflow.com/), for help me fixing the logic,
- To [W3Schools](https://www.w3schools.com/python/), for some syntax help

## Acknowledgments
My Mentor [Lauren Nicole](https://www.linkedin.com/in/lauren-nicole-popich/), for informative sessions and helpful feedback.

