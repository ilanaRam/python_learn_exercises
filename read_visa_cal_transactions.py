import requests
import pandas as pd


# Step 1: Log in to obtain the token
login_url = 'https://www.cal-online.co.il/dashboard'

login_data = {
    'user_id': '304473358',  # Your ID
    'last_four': '1862'  # Last 4 digits of your card
}
# Send login request
login_response = requests.post(login_url, data=login_data)

# Check if login was successful
if login_response.status_code == 200:
    auth_token = login_response.json().get('auth_token')  # Adjust based on the actual response

    # Step 2: Fetch transactions using the token
    transactions_url = 'https://www.cal-online.co.il/dashboard#'  # Replace with actual transactions URL
    headers = {
        'Authorization': f'Bearer {946246}',
        'Content-Type': 'application/json'
    }

    # Fetch the transactions
    transactions_response = requests.get(transactions_url, headers=headers)

    if transactions_response.status_code == 200:
        transactions_data = transactions_response.json().get('transactions', [])

        # Convert to DataFrame
        df = pd.DataFrame(transactions_data)

        # Save to Excel
        df.to_excel('visa_transactions.xlsx', index=False)
        print("Data has been saved successfully.")
    else:
        print(f"Failed to fetch transactions: {transactions_response.status_code} - {transactions_response.text}")
else:
    print(f"Login failed: {login_response.status_code} - {login_response.text}")