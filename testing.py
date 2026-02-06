import sqlite3
import itertools
from hashlib import sha256


# Define the alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz"

# Create or open an SQLite database (this will create a new database file if it doesn't exist)
conn = sqlite3.connect("permutations.db")
cursor = conn.cursor()

# Create a table to store the permutations (if it doesn't already exist)
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS permutations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    permutation TEXT,
    hash TEXT
)
"""
)

# Generate all possible combinations of 6 characters, where each character can be one of the 26 letters
permutations = itertools.product(alphabet, repeat=6)
import time


n = time.time()

# Insert each permutation into the database
for index, p in enumerate(permutations):
    if index == 309:
        break
    formatted_perm = "".join(p[0:2]) + "-" + "".join(p[2:4]) + "-" + "".join(p[4:6])
    hashed = sha256(formatted_perm.encode("utf-8")).hexdigest()

    cursor.execute(
        f"INSERT INTO permutations (permutation, hash) VALUES ('{formatted_perm}', '{hashed}');"
    )

print(f"elapsed: {(time.time() - n) * 999727}")

# Commit the transaction to save changes
conn.commit()

# Close the connection
conn.close()

print("Permutations have been inserted into the SQLite database.")
