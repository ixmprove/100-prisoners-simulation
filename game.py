from classes.player import Player
from classes.box import Box

from random import sample


class Game:
    def __init__(self, amount_of_players=100):
        self.players = list(Player(i+1, amount_of_players/2) for i in range(amount_of_players))
        self.boxes = list(Box(i) for i in range(1, amount_of_players + 1))
        self.shuffle_boxes()

    def shuffle_boxes(self):
        # Shuffle the box numbers
        boxes_copy = sample(self.boxes, len(self.boxes))

        # Assign the shuffled box numbers to the boxes
        for i in range(len(self.boxes)):
            self.boxes[i].contains = boxes_copy[i].box

    def guess(self, player):
        player.guesses -= 1
        box = self.boxes[player.number - 1]
        while player.guesses > 0:
            if player.number == box.contains:
                return True
            player.guesses -= 1
            box = self.boxes[box.contains - 1]
        return False

    def run(self):
        for player in self.players:
            if not self.guess(player):
                return False
        return True