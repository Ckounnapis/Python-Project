#charalampos kounnapis AM:5401

import random

ladders = {
    1: 38,
    4: 14,
    8: 30,
    21: 42,
    28: 76,
    50: 67,
    71: 92,
    80: 99
}

snakes = { 
    36: 6,
    32: 10,
    62: 18,
    48: 26,
    88: 24,
    95: 56,
    97: 78
}

def check_snakes_ladders(position, ladders, snakes, players_name):
    if position in ladders:
        new_pos = ladders[position]
        message = print(f"{players_name},you are lucky! You have reached square {position}, a base of a ladder," 
                    "which now takes you to square", new_pos)
        return new_pos, message
    
    if position in snakes:
        new_pos = snakes[position]
        message = print(f"{players_name},you are unlucky! You have reached square {position}, the head of a snake," 
                    "which now takes you to square", new_pos)
        return new_pos, message
        
    return position, None

def new_game():
    num_players = int(input("Please enter the number of players:"))
    players = []
    position = []
    
    for i in range(num_players):
        name = input(f"Player {i+1}, please enter your name: ")
        players.append(name)
        position.append(0)
    
    current_players = random.randint(0, num_players - 1)
    print(f"{players[current_players]},you are randomly selected to start" 
          " first")
    print("--------------------")
    
    play_game(players, position, current_players)

def save_game(players, position, next_player_index):
    with open("savedgame.txt", "w") as f:
        f.write(str(len(players)) + "\n")
        
        for i in range(len(players)):
            f.write(players[i] + " " + str(position[i]) + "\n")
            
        f.write(str(next_player_index) + "\n")
    print("game interrupted successfully. Status is saved in file 'savedgmae.txt'")

def load_game():
    with open("savedgame.txt", "r") as f:
        lines = f.readlines()
    
    num_players = int(lines[0].strip())
    
    players = []
    position = []
    
    for i in range(1, num_players + 1):
        name, pos = lines[i].split()
        players.append(name)
        position.append(int(pos))
        
    next_player_index = int(lines[num_players + 1].strip())

    return players, position, next_player_index
    

def play_game(players, position, current_players, loaded = False):
    num_players = len(players)
    
    
    while True:
        if not loaded:
            for i in range(num_players):
                print(f"{players[i]} at square {position[i])")
        else:
            for i in range(num_players):
                print(f"{players[i]} is at square {position[i]}")
       
            print(f"Next player is {players[next_player_index]}\n")
            
        answer = input(f"{players[current_players]},hit ENTER to roll the die," 
                        "or 'S' to save current game and exit:\n")
        if answer == "S" or answer == "s":
            next_player_index = current_players
            save_game(players, position, next_player_index)
            return
        
        die = random.randint(1, 6)
        print("The roll is: ", die)
        
        new_pos = position[current_players] + die
        
        if new_pos > 100:
            print(f"{players[current_players]} the die takes you outside the board,"
                  "so you will stay at your original square")
            new_pos = position[current_players]
        elif new_pos == 100:
            position[current_players] = new_pos
            print(f"{players[current_players]},congratulations! You are the first to" 
                  " land on square 100 and you win the game!")
            break
        else:
            players_name = players[current_players]
            new_pos, msg = check_snakes_ladders(new_pos, ladders, snakes,players_name )
            if msg:
                print(msg)
                
            position[current_players] = new_pos
            
        current_players = (current_players + 1) % num_players

  
def main():
    choice = input("Please enter 'L' or 'l' to continue last saved game," 
                    "or any other input to start a new game: ")
    if( choice == 'L' or choice == 'l'):
        try:
            players, position, next_player_index = load_game()
            play_game(players, position, next_player_index, loaded = False)
        except FileNotFound:
            print("No saved game found, Starting a new gmae \n")
            new_game()
    else:
        new_game()


if __name__ == "__main__":
    main()