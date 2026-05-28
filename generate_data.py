import csv
import json
import random
from datetime import datetime, timedelta

NUM_TRANSACTIONS = 1_000_000
NUM_ACCOUNTS = 50_000
ACCOUNT_LEN = 14
CSV_FILENAME = "transactions.csv"
JSON_FILENAME = "transactions.json"

print("Generating {NUM_ACCOUNTS} unique accounts")

# generates unique transactions with zfill (padding with 0 untill desired len)
accounts = [f"CZ{str(i).zfill(ACCOUNT_LEN)}" for i in range(1, NUM_ACCOUNTS + 1)]

def generate_transaction(trx_id):
    """Generates random transaction log."""

