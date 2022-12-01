# cse210-06

CSE-210 Final Project

Game Specification: https://byui-cse.github.io/cse210-course-competency/polymorphism/materials/cycle-specification.html

Group Members:
- Brock Ford
- Ashlee Butterfield
- Spencer Christensen
- Zachary Lindstrom
- Sayri Quinchiguango

Overview
Tetris is a game where the player tries to line up a row of blocks to make them disappear and earn points. The game ends when the block stack touches the top of the screen.

List of Classes
Casting
- Actor
- Cast
- Score
- Piece
- IBlock(Piece)
- JBlock(Piece)
- LBlock(Piece)
- OBlock(Piece)
- SBlock(Piece)
- TBlock(Piece)
- ZBlock(Piece)

Services
- keyboard_service
- video_service

Directing
- Director

Scripting
- Action
- control_actors_action
- draw_actors_action
- handle_collisions_action
- move_actors_action
- script

Other
__main__
constants

Next Steps
- Build the other six piece classes
- Establish movement
- Establish boundaries
- Build collision (stop the piece when it hits another piece)
    - Doesn't allow piece to go beyond boundary
- Build row deletion and point counter

Nice-to-haves
- Speed-up piece on down press
- Speed-up piece on higher points