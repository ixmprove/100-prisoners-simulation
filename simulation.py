from game import Game

import sys
import subprocess

# Import 'tqdm' if available, otherwise install it and then import it.
try:
    from tqdm import tqdm
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'tqdm'])
    from tqdm import tqdm
    


class Simulation:
    def __init__(self, amount_of_simulations=100, amount_of_players=100):
        self.amount_of_simulations = amount_of_simulations
        self.amount_of_players = amount_of_players
        self.simulations = []

        # Check if an argument is given, and if its format is correct
        if (len(sys.argv) > 1):
            try:
                self.amount_of_simulations = int(sys.argv[1])
            except ValueError:
                print("Amount of simulations must be an integer.")
                exit(1)

    def run(self):
        # Run the simulations
        for i in tqdm (range(self.amount_of_simulations), desc="Simulating...", ascii=False, ncols=75, leave=True):
            current_game = Game(self.amount_of_players).run()
            self.simulations.append(current_game)

        # Print the results
        games_won = self.simulations.count(True)
        amount_of_games = len(self.simulations)
        win_percentage = games_won / amount_of_games * 100

        print()
        print(f'Won {games_won} out of {amount_of_games} games.')
        print('Win percentage: {:.3f}%'.format(win_percentage))



Simulation().run()