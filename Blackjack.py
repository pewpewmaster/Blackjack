import random


# Create poker cards.
class Poke:

    # Poker cards have shapes and numbers.
    def __init__(self):
        self._cards = [[shape, number] for shape in "♠♥♦♣" for number in [1,2,3,4,5,6,7,8,9,10,'J','Q','K']]
        # shuffle the cards.
        random.shuffle(self._cards)


# Create a poker dealer.
class Dealer:

    def __init__(self):
        self.cards = Poke()._cards

    # Dealer gives a card.
    def give_one_card(self):
        return self.cards.pop()


# Create a player.
class Player:

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.points = 0
        self.cards_in_hand = []

    # Reset Cards and points.
    def init(self):
        self.cards_in_hand = []
        self.points = 0

    # Count points.
    def now_count(self):
        point = 0 
        for shape, number in self.cards_in_hand:
            if number in ['J', 'Q', 'K']:
                number = 10
            point += number
        # If player has "A" and the total points add 1 less than 21, then A = 11. 
        for card in self.cards_in_hand:
            if card[1] == 1 and point + 10 < 21:
                self.points = point + 10
            else:
                self.points = point

    # Compare points before exceeding 21 points. 
    def is_win(self, bot):
        s1 = self.points
        s2 = bot.points
        if s1 > s2:
            print(f"{self.name} has {s1} points. {bot.name} has {s2} points. {self.name} wins!")
            self.score += 1
        elif s1 == s2:
            print(f"{self.name} has {s1} points. {bot.name} has {s2} points. Draw!")
        else:
            print(f"{self.name} has {s1} points. {bot.name} has {s2} points. {bot.name} wins!")
            bot.score += 1            

    # Player gets cards from dealer.
    # "*" means multiple lists
    def get(self, *cards):
        for card in cards:
            self.cards_in_hand.append(card)
        # Count new points.
        self.now_count() 


computer = Player('Bot')
human = Player('Player')
dealer = Dealer()

# Main functions of the game
def game(dealer, computer, human):
    # Round number. 
    count = 0

    while True:
        count += 1
        print(f"Round {count}")
        flag = False
        # Initiate points and cards in new round. 
        human.init()
        computer.init()
        # Dealer gives two cards to both player and bot. 
        human.get(dealer.give_one_card(), dealer.give_one_card())
        computer.get(dealer.give_one_card(), dealer.give_one_card())
        print(f"{human.name} has cards: {human.cards_in_hand[-2]}, {human.cards_in_hand[-1]}")
        # Hide a card for bot.
        print(f"{computer.name} has cards: {computer.cards_in_hand[-2]}, ?")
        # See if the total points equal to 21. 
        if human.points == 21 == computer.points:
            print("Both {human.name} and {computer.name} have 21 points. Draw!")
        elif human.points == 21:
            print("{human.name} has 21 points. {human.name} wins!")
            human.score += 1
        else:
            # Player gets cards
            while True:
                if_next_card = input("Player gets another card?(Y/N) ")
                if if_next_card in ['N', 'n']:
                    break                   
                elif if_next_card in ['Y', 'y']:
                    human.get(dealer.give_one_card())
                    print(f"{human.name} gets a card {human.cards_in_hand[-1]}. {human.name} has cards: {human.cards_in_hand}")
                    # See if player's points exceed 21. 
                    if human.points > 21:
                        print(f"{human.name} has {human.points} points. {computer.name} wins!")
                        computer.score += 1
                        flag = True
                        break
            # Bot gets cards
            if not flag:
                # If bot has less points than player, then he gets a card.
                while computer.points < human.points:
                    computer.get(dealer.give_one_card())
                    print(f"{computer.name} gets {computer.cards_in_hand[-1]}. {computer.name} has cards: {computer.cards_in_hand}")
                # See if bot's points excceed 21.
                if computer.points > 21:
                    print(f"{computer.name} has points {computer.points}. {human.name} wins!")
                    human.score += 1
                else:
                    # If Both palyer and bot have points less than 21, then compare the points. 
                    human.is_win(computer)

        print("-" * 30)
        # Chooes if start a new games. 
        if_play_again = input("Play another game?(Y/N) ")
        if if_play_again in ['Y', 'y']:
            print(f"{human.name} score : {computer.name} score = {human.score}:{computer.score}")
        # Compare scores.
        elif if_play_again in ['N', 'n']:
            print(f"{human.name} socre : {computer.name} score = {human.score}:{computer.score}")
            if human.score > computer.score:
                print(f"{human.name} wins!")
            elif human.score < computer.score:
                print(f"{computer.name} wins!")
            else:
                print("Draw!")
            print("GG! Thanks for playing.")
            exit(0)
        else:
            print ("Don't gamble!")
            exit(0)


# Call function
game(dealer, computer, human)