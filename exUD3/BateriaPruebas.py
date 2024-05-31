import unittest
from jugador import Player, MIN_ENERGY, MAX_ENERGY, Game
class Test(unittest.TestCase):

    def test1(self):
        player = Player(1, "TestPlayer")
        self.assertEqual(player.get_energy(), 50)

    def test2(self):
        player = Player(2, "TestPlayer2")
        player.boost(-100)
        self.assertTrue(player.get_energy() == MIN_ENERGY)

    def test3(self):
        player = Player(3, "TestPlayer3")
        player.boost(200)
        self.assertTrue(player.get_energy() == MAX_ENERGY)

    def test4(self):
        player1 = Player(4, "TestPlayer4")
        player2 = Player(5, "TestPlayer5")
        game = Game(player1, player2, 1)  # Una sola ronda
        game.playRound()  # Modificar energías

        winner = game.winner()
        if player1.get_energy() > player2.get_energy():
            self.assertEqual(winner, player1)
        else:
            self.assertEqual(winner, player2)

if __name__ == '__main__':
    unittest.main()