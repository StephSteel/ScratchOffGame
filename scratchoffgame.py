import random

symbols = ['$', '%', '#', '*', '&']

card_levels = {
    'B': {'name': 'Basic', 'price': 5, 'max_win': 20},
    'I': {'name': 'Intermediate', 'price': 10, 'max_win': 50},
    'A': {'name': 'Advanced', 'price': 20, 'max_win': 100}
}


winning_symbols = {level: random.choice(symbols) for level in card_levels}


def create_scratch_card(level):
    card = []
    for _ in range(3):
        row = [random.choice(symbols) for _ in range(3)]
        card.append(row)
    return card

def display_purse(purse):
    print(f"Your current purse: ${purse}")
def display_card(card):
    for row in card:
        print(" ".join(row))

def check_win(card, winning_symbol, level):
    for row in card:
        if all(symbol == winning_symbol for symbol in row):
            return card_levels[level]['max_win']
    return 0

def main():
    print("Welcome to Scratch Off Game!")
    
    purse = 50 

    while True:
        print("\nAvailable Card Levels:")
        for level, info in card_levels.items():
            print(f"{level} - {info['name']} - Price: ${info['price']}  Max Win: ${info['max_win']}")
        
        selected_level = input("Choose a card level (B/I/A) or 'q' to quit: ").upper()
        
        if selected_level == 'Q':
            print("Thanks for playing!")
            break
        
        if selected_level not in card_levels:
            print("Invalid level. Please select a valid card level.")
            continue
        
        if purse < card_levels[selected_level]['price']:
            print("You don't have enough money to purchase this card level.")
            continue
        
        purse -= card_levels[selected_level]['price']
        
        card = create_scratch_card(selected_level)
        display_card(card)
        
        choice = input("Enter 's' to scratch the card or 'q' to quit: ").lower()
        
        if choice == 's':
            winnings = check_win(card, winning_symbols[selected_level], selected_level)
            if winnings > 0:
                print(f"Congratulations! You won ${winnings}!")
                purse += winnings
            else:
                print("Sorry, you didn't win this time. Try again!")
        
        display_purse(purse)

if __name__ == "__main__":
    main()
