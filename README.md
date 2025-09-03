Classic Pong Game with Python  pong

A complete implementation of the classic arcade game "Pong" built entirely with Python's built-in `turtle` module. This project features two-player gameplay, a live scoreboard, and progressively increasing difficulty.

<img width="797" height="620" alt="image" src="https://github.com/user-attachments/assets/73472786-f0a1-47da-aeb3-e27590d36a08" />


-----

## Features

  - **Two-Player Controls**: The left and right paddles are controlled independently.
  - **Live Scoreboard**: The score is updated in real-time at the top of the screen.
  - **Increasing Difficulty**: The ball's speed increases every time it's hit by a paddle, making for a more challenging game.
  - **Classic Visuals**: A clean, minimalist design reminiscent of the original arcade game.
  - **Modular Code**: The project is split into separate classes for the Ball, Paddle, and Scoreboard, making the code clean and easy to understand.

-----

## How to Play

The goal is to hit the ball with your paddle and score a point when your opponent misses.

  - **Left Paddle Controls**:
      - Press the **'w'** key to move up.
      - Press the **'s'** key to move down.
  - **Right Paddle Controls**:
      - Press the **'Up Arrow'** key to move up.
      - Press the **'Down Arrow'** key to move down.
  - **Exiting the Game**:
      - Press the **'f'** key to close the game at any time.

-----

## Getting Started

No special libraries are needed\! This project uses Python's standard `turtle` library, which comes with every Python installation.

### Prerequisites

  - Python 3.x

### Running the Game

1.  Clone this repository or download the files to your local machine.
2.  Open your terminal or command prompt and navigate to the project directory.
3.  Run the main game file using the following command:
    python main.py
4.  The game window will open, and you can start playing immediately.

-----

## Project Structure

The code is organized into four main files for better readability and management:

  - `main.py`: This is the entry point of the application. It initializes the screen, creates the game objects (paddles, ball, scoreboard), and contains the main game loop that controls the flow of the game.
  - `paddle.py`: Defines the `Paddle` class, which controls the appearance, position, and movement logic for both player paddles.
  - `ball.py`: Defines the `Ball` class. This file manages the ball's movement, its bouncing physics off the walls, and its collision detection with the paddles.
  - `scoreboard.py`: Defines the `Scoreboard` class, which is responsible for displaying the scores for both players and updating them whenever a point is scored.
