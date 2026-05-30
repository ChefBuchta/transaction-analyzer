import csv
import json
import random
from pathlib import Path
from datetime import datetime, timedelta
NUM_TRANSACTIONS = 1_000_000
NUM_ACCOUNTS = 50_000
ACCOUNT_LEN = 14
CONFIG_PATH = "config.json"
with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    config = json.load(f)
csv_path = Path(config["csv_path"])
json_path = Path(config["json_path"])

print(f"Generating {NUM_ACCOUNTS} unique accounts")

# generates unique transactions with zfill (padding with 0 untill desired len)
accounts = [f"CZ{str(i).zfill(ACCOUNT_LEN)}" for i in range(1, NUM_ACCOUNTS + 1)]

def generate_transaction(tx_id: int) -> dict:
    """Generates random transaction log."""
    source = random.choice(accounts)
    target = random.choice(accounts)
    
    while source == target:
        target = random.choice(accounts)
    
    # I don't care about if the person have enough money in this project, in production code there would have to be checks for that
    amount = round(random.uniform(100.0, 500000.0), 2)
    start_date = datetime(2026, 1, 1)
    random_days = random.randint(0, 364)
    random_seconds = random.randint(0, 86399)
    tx_date = start_date + timedelta(days=random_days, seconds=random_seconds)

    return {
        "tx_id": f"TXN-{str(tx_id).zfill(7)}",
        "source_account": source,
        "target_account": target,
        "amount": amount,
        "date": tx_date.strftime("%Y-%m-%dT%H:%M:%S")
    }

print(f"Generating {NUM_TRANSACTIONS} transactions into CSV and JSON")

with open(csv_path, 'w', encoding='utf-8') as csv_file, \
    open(json_path, 'w', encoding='utf-8') as json_file:
    fieldnames = ["tx_id", "source_account", "target_account", "amount", "date"]
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()
    
    json_file.write("{\n    \"transactions\": [\n")

    for i in range(1, NUM_TRANSACTIONS + 1):
        txn = generate_transaction(i)
        if i % 2: 
            csv_writer.writerow(txn)
        else:
            json_string = json.dumps(txn)
            if i < NUM_TRANSACTIONS:
                json_file.write(f"    {json_string},\n")
            else:
                json_file.write(f"    {json_string}\n")


    json_file.write("  ]\n}")

print(f"Done! Files")
