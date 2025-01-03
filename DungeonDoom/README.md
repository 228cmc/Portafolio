# Dungeon of Doom

## Overview

"Dungeon of Doom" is a text-based Java game where you navigate a board to collect gold, avoid a bot that chases you, and escape through an exit. Players interact with the game by typing commands.

---

## How to Play

1. **Prepare a Board File**  
   Use the provided `exampleBoard.txt` or create your own file (e.g., `customBoard.txt`) with the following valid characters:
   - `P`: Player (your starting position)
   - `B`: Bot (the enemy)
   - `G`: Gold (collectible items)
   - `E`: Exit (goal to win)
   - `#`: Wall (blocks movement)
   - `.`: Empty space (movable tiles)  

   Place the `.txt` file at the same level as the Java files.

2. **Compile and Run the Game**  
   - Compile: `javac Main.java`
   - Run: `java Main <file_path>`  

3. **Game Commands**  
   - `LOOK`: View a 5x5 section of the board centered around your position.
   - `MOVE <direction>`: Move in one of four directions (`north`, `south`, `east`, `west`).
   - `PICKUP`: Collect gold if present at your current position.
   - `HELLO`: Display how much gold is needed to win.
   - `QUIT`: Exit the game.  

---

## Rules

1. Collect the required amount of gold to win (`2` by default).
2. Reach an exit tile after collecting enough gold.
3. Avoid the bot, which chases you across the board.
4. You cannot move through walls.

---

## Folder Structure

```
.
├── Main.java          # Entry point of the game
├── Board.java         # Manages the board and gameplay logic
├── BotPlayer.java     # Represents the bot enemy
├── HumanPlayer.java   # Represents the player character
├── Player.java        # Abstract base class for Human and Bot players
├── Wall.java          # Represents walls on the board
├── Gold.java          # Represents collectible gold
├── EmptyFloor.java    # Validates the board dimensions and layout
├── exampleBoard.txt   # Default board file for testing
```

---

## Object-Oriented Design

The game applies object-oriented programming principles by organizing functionality into classes based on the elements in the board: wall, gold, exit, player, bot, and empty space.  

1. **Encapsulation**  
   - The `Board` class encapsulates game logic, managing interactions between walls, gold, players, and exits.
   - The `Gold` class encapsulates the win condition using the static `requiredGold` method.

2. **Inheritance and Specialization**  
   - The `Player` class serves as an abstract base, defining shared attributes like position (`x`, `y`) and collected gold.  
   - Both `HumanPlayer` and `BotPlayer` inherit from `Player`, demonstrating inheritance.  
   - The `BotPlayer` class specializes behavior with its `chaseHuman` method, allowing the bot to track and move toward the human player.

3. **Polymorphism**  
   - Both `HumanPlayer` and `BotPlayer` follow the same interface defined in the `Player` class, enabling the board to interact with them seamlessly.

4. **Validation and Isolation**  
   - The `EmptyFloor` class validates board dimensions and layout, ensuring the game setup is consistent.

---

## Features to Improve

1. **Better File Path Handling**  
   Normalize file paths to support Windows (`\`) and Unix (`/`) systems for compatibility.
2. **More Gameplay Elements**  
   - Add traps or power-ups to enhance strategy.
   - Implement multiple bots for added difficulty.
   - Allow bots to collect gold.
3. **Graphical Version**  
   Replace the text-based interface with a graphical user interface (GUI).

---

## License

Created by **Carolina Masmela Correa**.  
Licensed under the MIT License.  





