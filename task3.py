
print("Enter 30 transaction amounts (e.g., 500, -200.50, 1000)\n")

transactions = []
count = 0

while count < 30:
    try:
        amount = float(input(f"Transaction {count+1}/30: $"))

        transactions.append(amount)
        count += 1
        print("Added successfully!\n")

    except ValueError:
        print("Invalid input! Please enter a number (like 150.75 or -50)\n")
    except KeyboardInterrupt:
        print("\n\nProgram stopped by user.")
        break
    except Exception as e:
        print(f"Something went wrong: {e}\n")

else:
    # This else runs only if the loop completed without break
    total = sum(transactions)
    avg = total / 30

    print("\n" + "="*40)
    print("     TRANSACTION SUMMARY")
    print("="*40)
    print(f"Total Transactions : 30")
    print(f"Total Amount       : ${total:,.2f}")
    print(f"Average Amount     : ${avg:,.2f}")
    print(f"Max Transaction    : ${max(transactions):,.2f}")
    print(f"Min Transaction    : ${min(transactions):,.2f}")
    print("="*40)
