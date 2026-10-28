import random

class BotPlayer:
    def __init__(self, name, profile):
        self.name = name
        self.profile = profile  # "Nit", "CallingStation", "Maniac"
        self.chips = 2000
        
    def make_decision(self, current_bet, pot_size):
        roll = random.randint(1, 100)
        
        if self.profile == "Nit":
            if current_bet > 0:
                if roll <= 85: return "Fold", 0
                elif roll <= 95: return "Call", current_bet
                else: return "Raise", current_divider = current_bet * 3
            else:
                return ("Check", 0) if roll <= 70 else ("Raise", 2.5)
                
        elif self.profile == "CallingStation":
            if current_bet > 0:
                if roll <= 10: return "Fold", 0
                elif roll <= 85: return "Call", current_bet
                else: return "Raise", current_bet * 2
            else:
                return ("Check", 0) if roll <= 80 else ("Raise", 2)
                
        elif self.profile == "Maniac":
            if current_bet > 0:
                if roll <= 20: return "Fold", 0
                elif roll <= 50: return "Call", current_bet
                else: return "Raise", current_bet * 3.5
            else:
                return ("Check", 0) if roll <= 30 else ("Raise", 3)
        return "Fold", 0
