import hashlib

def merkle_tree(transactions):
    if len(transactions) == 0:
        return None
    elif len(transactions) == 1:
        return transactions[0]

    # Create a list to store intermediate hashes
    intermediate_hashes = []

    # Create the leaf nodes (hashes of individual transactions)
    for transaction in transactions:
        intermediate_hashes.append(hashlib.sha256(transaction.encode()).hexdigest())

    # Build the Merkle Tree by recursively hashing pairs of nodes
    while len(intermediate_hashes) > 1:
        new_level = []
        for i in range(0, len(intermediate_hashes), 2):
            if i + 1 < len(intermediate_hashes):
                combined_hash = intermediate_hashes[i] + intermediate_hashes[i + 1]
                new_hash = hashlib.sha256(combined_hash.encode()).hexdigest()
            else:
                new_hash = intermediate_hashes[i]
            new_level.append(new_hash)
        intermediate_hashes = new_level

    return intermediate_hashes[0]

# Example usage:
transactions = ["Tx1", "Tx2", "Tx3", "Tx4"]  # Replace with your transaction data
merkle_root = merkle_tree(transactions)
print("Merkle Root:", merkle_root)
