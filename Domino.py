import random

def BubbleSort(arr):
    n = len(arr)

    for i in range(n):
        for j in range (n - i - 1):
            if arr[j][1] > arr[j+1][1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def DominoDealer(num_players):
    domino_pieces = [
    (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6),
    (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6),
    (2, 2), (2, 3), (2, 4), (2, 5), (2, 6),
    (3, 3), (3, 4), (3, 5), (3, 6),
    (4, 4), (4, 5), (4, 6),
    (5, 5), (5, 6),
    (6, 6)
]
        # Shuffle the domino pieces
    random.shuffle(domino_pieces)

    # Number of players and pieces per player
    pieces_per_player = len(domino_pieces) // num_players

    # Distribute pieces to players
    players = []
    for i in range(num_players):
        player_pieces = domino_pieces[i * pieces_per_player: (i + 1) * pieces_per_player]
        players.append(player_pieces)
    
    return players

def PlayerOrder(players):

    player_order = []

    for player in players:
        points = 0
        for piece in player:
            if piece[0] == piece[1] and points < piece[0]:
                points = piece[0]
        player_order.append((players.index(player), points))
    
    BubbleSort(player_order)
    player_order.reverse()
    
    return player_order

def FirstPlay(Board, PlayerData, Order):

    current_player = PlayerData[Order[0][0]]
    points = 0
    for domino in current_player:
        if (domino[0] == domino[1]) and (points < domino[0]):
            points = domino[0]
            toPlay = (current_player.index(domino), (domino[0],domino[1]))
    Board.append(toPlay[1])
    current_player.pop(toPlay[0])

def BoardChecker(Board):
    n = len(Board) 
    return (Board[0][0], Board[0][1]) if n == 1 else (Board[0][0], Board[n - 1][1])

def CheckHand(PlayerData, Current, Possibilites):
    CanPlay = []
    for domino in PlayerData[Current]:
        if (domino[1] == Possibilites[0]) or (domino[1] == Possibilites[1]) or (domino[0] == Possibilites[0]) or (domino[0] == Possibilites[1]):
            CanPlay.append(domino)
    return CanPlay

def Turn(Board, PlayerData, Current, PossiblePlays):
    CurrentBoard = BoardChecker(Board)
    PlayerHand = PlayerData[Current]
    if len(PossiblePlays) == 1:
        TileToPlay = PossiblePlays[0]
    else:
        TileToPlay = random.choice(PossiblePlays)

    print(f"Player {Current + 1} will play the tile {TileToPlay}")

    if TileToPlay[1] == CurrentBoard[0]:
        Board.insert(0,TileToPlay)
        PlayerHand.remove(TileToPlay)
        print(Board)
        return Board
        
    elif TileToPlay[0] == CurrentBoard[1]:
        Board.append(TileToPlay)
        PlayerHand.remove(TileToPlay)
        print(Board)
        return Board
    
    elif TileToPlay[0] == CurrentBoard[0]:
        PlayerHand.remove(TileToPlay)
        TileToPlay = TileToPlay[::-1]
        Board.insert(0,TileToPlay)
        print(Board)
        return Board
    
    elif TileToPlay[1] == CurrentBoard[1]:
        PlayerHand.remove(TileToPlay)
        TileToPlay = TileToPlay[::-1]
        Board.append(TileToPlay)
        print(Board)
        return Board



Board = []
Places = []
totPlayer = 5
PlayerData = DominoDealer(totPlayer)
Order = PlayerOrder(PlayerData)
aux = True
aux2 = True
aux3 = False
while(True):

    CheckNoMorePlays = 0

    if aux2:
        FirstPlay(Board, PlayerData, Order)
        aux2 = False

    for player in Order:

        if len(Places) == totPlayer:
            print("No more possible plays")
            aux3 = True
            break

        if aux:
            aux = False
            continue
        Current = player[0]
        print("Checking player data")
        for i in PlayerData:
            print(i)
        print("End check")

        if len(PlayerData[Current]) == 0:
            Places.append(Current)
            PlayerData.pop(Current)
            continue

        PossiblePlays = CheckHand(PlayerData, Current, BoardChecker(Board))
        if len(PossiblePlays) == 0:
            print(f"Player {player[0] + 1} doesnt have a possible domino to play")
            CheckNoMorePlays += 1
            if CheckNoMorePlays == totPlayer:
                print("No more players hace possible plays")
                break
        else:
            Turn(Board, PlayerData, Current, PossiblePlays)
    
    if aux3 or CheckNoMorePlays == totPlayer:
        print(Board)
        print("Game endend")
        break
    



