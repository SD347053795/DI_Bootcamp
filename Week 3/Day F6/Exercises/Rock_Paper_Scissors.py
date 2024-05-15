from game import Game
def get_user_menu_choice():
    print("Menu:")
    print("1. Play a new game")
    print("2. Show scores")
    print("3. Quit")
    choice = input("Enter your choice: ")
    return choice
def print_results(results):
    print("Game Results:")
    for key, value in results.items():
        print(f"{key.capitalize()}: {value}")
    print("Thank you for playing!")
def main():
    results = {'win': 0, 'loss': 0, 'draw': 0}
    while True:
        choice = get_user_menu_choice()
        if choice == '1':
            game = Game()
            result = game.play()
            results[result] += 1
        elif choice == '2':
            print_results(results)
        elif choice == '3':
            print_results(results)
            break
        else:
            print("Invalid choice. Please choose again.")
main()