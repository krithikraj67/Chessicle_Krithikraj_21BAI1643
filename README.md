# Chessicle Game Rules and Setup Instructions

## Setup Instructions

1. **Install Required Dependencies:**
   - Use the following command to install the required Python libraries:
     ```bash
     pip install -r requirements.txt
     ```

2. **Run the Server:**
   - Start the server by running the `server.py` script:
     ```bash
     python server.py
     ```

3. **Run the Game:**
   - Once the server is running, start the game by executing the `game.py` script:
     ```bash
     python game.py
     ```

## Game Rules

### Game Setup
- **Players:** 2 Players
- **Grid:** 5x5 grid
- **Teams:** Each player controls a team of 5 characters, consisting of 3 Pawns, 1 Hero1, and 1 Hero2.
- **Initial Setup:** 
  - Players arrange their characters on their respective starting rows at the beginning of the game.
  - Character positions are input as a list of character names, placed from left to right.

### Characters and Movement

#### 1. Pawn
- **Movement:** Moves one block in any direction (Left, Right, Forward, or Backward).
- **Move Commands:** 
  - `L` (Left)
  - `R` (Right)
  - `F` (Forward)
  - `B` (Backward)

#### 2. Hero1
- **Movement:** Moves two blocks straight in any direction.
- **Attack:** Kills any opponent's character in its path.
- **Move Commands:** 
  - `L` (Left)
  - `R` (Right)
  - `F` (Forward)
  - `B` (Backward)

#### 3. Hero2
- **Movement:** Moves two blocks diagonally in any direction.
- **Attack:** Kills any opponent's character in its path.
- **Move Commands:** 
  - `FL` (Forward-Left)
  - `FR` (Forward-Right)
  - `BL` (Backward-Left)
  - `BR` (Backward-Right)

#### Move Command Format:
- **For Pawn and Hero1:** `<character_name>:<move>`  
  Example: `P1:L`, `H1:F`
- **For Hero2:** `<character_name>:<move>`  
  Example: `H2:FL`, `H2:BR`

#### Notes:
- All moves are relative to the player's perspective.

### Game Flow

#### Initial Setup
- **Character Deployment:** Players deploy all 5 characters on their starting row in any order.
- **Character Arrangement:** Players choose any arrangement of 3 Pawns, 1 Hero1, and 1 Hero2 for their team.

#### Turns
- Players alternate turns, making one move per turn.

#### Combat
- **Character Removal:** 
  - If a character moves to a space occupied by an opponent's character, the opponent's character is removed from the game.
  - **Hero1 and Hero2:** Remove any opponent's character in their path, not just the one at the final destination.

#### Invalid Moves
Moves are considered invalid if:
- The specified character doesn't exist.
- The move would take the character out of bounds.
- The move is not valid for the given character type.
- The move targets a friendly character.

**Resolution:** Players must retry their turn if they input an invalid move.

#### Game State Display
- **Grid:** After each turn, the 5x5 grid is displayed with all character positions.
- **Naming Convention:** Character names are prefixed with the player's identifier and character type (e.g., `A-P1`, `B-H1`, `A-H2`).

### Winning the Game
- **Victory Condition:** The game ends when one player eliminates all of their opponent's characters.
- **Winner Announcement:** The winning player is announced.
- **New Game:** Players can choose to start a new game.
