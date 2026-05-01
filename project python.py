# Fraud Detection System

# Sample transaction data (amounts)
transactions = [100, 250, 300, 5000, 150, 20000, 350, 400]

# Threshold amount (anything above this is suspicious)
THRESHOLD = 10000

def detect_fraud(transactions):
    suspicious = []
    
    for i, amount in enumerate(transactions):
        if amount > THRESHOLD:
            suspicious.append((i, amount))
    
    return suspicious

# Run detection
fraud_transactions = detect_fraud(transactions)

# Display results
if len(fraud_transactions) == 0:
    print("No suspicious transactions detected.")
else:
    print("Suspicious Transactions Found:")
    for index, amount in fraud_transactions:
        print(f"Transaction {index + 1}: Amount = {amount}")
