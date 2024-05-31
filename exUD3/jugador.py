import random
MAX_ENERGY = 100
MIN_ENERGY = 0

class Player:
    def __init__(self, id_player, nickname):
        self.__idPlayer = id_player
        self.__nickName = nickname
        self.__energy = (MAX_ENERGY + MIN_ENERGY) // 2

    def get_idPlayer(self):
        return self.__idPlayer

    def get_nickName(self):
        return self.__nickName

    def get_energy(self):
        return self.__energy

    def set_idPlayer(self, new_id):
        self.__idPlayer = new_id

    def set_nickName(self, new_nickname):
        self.__nickName = new_nickname

    def __set_energy(self, new_energy):
        self.__energy = max(MIN_ENERGY, min(MAX_ENERGY, new_energy))

    def __str__(self):
        return f"[{self.__idPlayer}, {self.__nickName}, {self.__energy}]"

    def boost(self, charge):
        if not isinstance(charge, int):
            charge = 0

        new_energy = self.__energy + charge
        self.__set_energy(new_energy)
        return charge, self.__energy

class Game:
    def __init__(self, player1, player2, rounds):
        self.__player1 = player1
        self.__player2 = player2
        self.__rounds = rounds

    def playRound(self):
        charge1 = random.randint(-25, 25)
        charge2 = random.randint(-25, 25)
        boost1 = self.__player1.boost(charge1)
        boost2 = self.__player2.boost(charge2)
        return [boost1, boost2]

    def winner(self):
        if self.__player1.get_energy() > self.__player2.get_energy():
            return self.__player1
        elif self.__player2.get_energy() > self.__player1.get_energy():
            return self.__player2
        else:
            return None  # Empate

    def play(self):
        for i in range(self.__rounds):
            result = self.playRound()
            print(f"Round {i+1}: {result}")

class main:
    p1 = Player(1, "a")
    p2 = Player(2, "b")

    g1 = Game(p1, p2, 3)

    print("p1:", p1)
    print("p2:", p2)

    g1.play()

    ganador = g1.winner()
    if ganador:
        print("El ganador del combate es:", ganador)
    else:
        print("Empate")
