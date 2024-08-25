
# TASK 1
class ScoreEntry:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_score(score_entry):
        return score_entry.score


class Scoreboard:
    def __init__(self):
        self.scores = [] 

    def add_score(self, player_name, player_score):
        new_score_entry = ScoreEntry(player_name, player_score)
        self.scores.append(new_score_entry)
        
    def print_leaderboard(self):
        self.scores.sort(key=ScoreEntry.get_score, reverse=True)
        top_three_scores = self.scores[:3]

        for entry in top_three_scores:
            print(f"{entry.name}: {entry.score}")

scoreboard = Scoreboard()

scoreboard.add_score('Alice', 7821)
scoreboard.add_score('Bob', 12103)
scoreboard.add_score('Charlie', 8762)
scoreboard.add_score('Denise', 6573)

scoreboard.print_leaderboard()


# TASK 2
class ChoreTracker:
    def __init__(self):
        self.chores = {} # a dict

    # Write your add_hours and print_summary methods here
    def add_hours(self, chore_name, hours_spent):
        if chore_name in self.chores:
            current_chore_hours = self.chores[chore_name]
            self.chores[chore_name] = current_chore_hours + hours_spent
        else:
            self.chores[chore_name] = hours_spent

    def print_summary(self):
        total_hours = 0

        for chore_name, chore_hours in self.chores.items():
            total_hours += chore_hours
            print(f"{chore_name}: {chore_hours:.2f} hours")

        print(f"TOTAL: {total_hours:.2f} hours")

tracker = ChoreTracker()

tracker.add_hours('sweeping', 0.75)
tracker.add_hours('laundry', 0.5)
tracker.add_hours('working', 6)
tracker.add_hours('mopping', 0.5)
tracker.add_hours('laundry', 1)
tracker.add_hours('working', 5.5)

tracker.print_summary()



# TASK 3 A
class BankAccount:
    def __init__(self, name, initial_balance):
        self.name = name
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        # Part B: Raise an exception as appropriate
        self.balance = self.balance - amount

def print_balances(account_a, account_b):
    print('== Account balances ==')
    print(f'  {account_a.name}: ${account_a.balance:.2f}')
    print(f'  {account_b.name}: ${account_b.balance:.2f}')

# Part A. Write your transfer funds function here
def transfer_funds(transfer_amount, from_account, to_account):
    from_account.withdraw(transfer_amount)
    to_account.deposit(transfer_amount)

account_a = BankAccount('Alice', 100)
account_b = BankAccount('Bob', 100)
print_balances(account_a, account_b)

another_transfer = 'y'
while another_transfer == 'y':
    amount = float(input('Enter transfer amount ($): '))

    # Part C. Print an appropriate message if an exception is encountered
    transfer_funds(amount, account_a, account_b)

    print_balances(account_a, account_b)
    another_transfer = input('Perform another transfer? (y/n): ')



# TASK 3 B
class BankAccount:
    def __init__(self, name, initial_balance):
        self.name = name
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        # Part B: Raise an exception as appropriate
        if (self.balance - amount) < 0:
            raise ValueError("Balance would be negative after withdrawal")
        else:
            self.balance = self.balance - amount

def print_balances(account_a, account_b):
    print('== Account balances ==')
    print(f'  {account_a.name}: ${account_a.balance:.2f}')
    print(f'  {account_b.name}: ${account_b.balance:.2f}')

# Part A. Write your transfer funds function here
def transfer_funds(transfer_amount, from_account, to_account):
    from_account.withdraw(transfer_amount)
    to_account.deposit(transfer_amount)

account_a = BankAccount('Alice', 100)
account_b = BankAccount('Bob', 100)
print_balances(account_a, account_b)

another_transfer = 'y'
while another_transfer == 'y':
    amount = float(input('Enter transfer amount ($): '))

    # Part C. Print an appropriate message if an exception is encountered
    transfer_funds(amount, account_a, account_b)

    print_balances(account_a, account_b)
    another_transfer = input('Perform another transfer? (y/n): ')



# TASK 3 C
class BankAccount:
    def __init__(self, name, initial_balance):
        self.name = name
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        # Part B: Raise an exception as appropriate
        if (self.balance - amount) < 0:
            raise ValueError("Balance would be negative after withdrawal")
        else:
            self.balance = self.balance - amount

def print_balances(account_a, account_b):
    print('== Account balances ==')
    print(f'  {account_a.name}: ${account_a.balance:.2f}')
    print(f'  {account_b.name}: ${account_b.balance:.2f}')

# Part A. Write your transfer funds function here
def transfer_funds(transfer_amount, from_account, to_account):
    from_account.withdraw(transfer_amount)
    to_account.deposit(transfer_amount)

account_a = BankAccount('Alice', 100)
account_b = BankAccount('Bob', 100)
print_balances(account_a, account_b)

another_transfer = 'y'
while another_transfer == 'y':
    amount = float(input('Enter transfer amount ($): '))

    # Part C. Print an appropriate message if an exception is encountered
    try:
        transfer_funds(amount, account_a, account_b)
    except ValueError as error:
        print("<< Error transferring funds >>")

    print_balances(account_a, account_b)
    another_transfer = input('Perform another transfer? (y/n): ')



# TASK 4 A
