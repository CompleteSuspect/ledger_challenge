balances = {"Alice": 500,
            "Bob": 1000,
            "Craig": 750
            }

with open("transactions.txt", "r") as f:
    for line in f:
        line = line.strip()
        if not line or not line.startswith('#'):
            new_line = line.split('#', 1)[0].strip()
            try:
                name, amount_str = new_line.split(',', 1)
                name = name.strip().title()
                amount_int = int(amount_str.strip())
                print(f'Fetching from file: {name}, {amount_int}')

                if balances.get(name, 0) + amount_int >= 0:
                    balances[name] = balances.get(name, 0) + amount_int
                    print(f'Calculating new balance for {name}: £{balances[name]}\n')
                else:
                    print(f"{name}'s balance is too low(£{balances[name]}), transaction aborted!\n")

            except ValueError as e:
                print(f'Skipping line, {e}')

with open('updated_balances.txt', 'w') as f:
    for name, balance in balances.items():
        f.write(f'{name}: {balance}\n')
        print(f'{name}, has £{balance}.')