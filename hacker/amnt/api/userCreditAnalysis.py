import requests
from collections import defaultdict

# API Endpoint
API_URL = "https://api.example.com/users/credits"


def fetch_user_data(api_url):
    response = requests.get(api_url)
    response.raise_for_status()
    return response.json()


def analyze_credits(data):
    # Find user with highest credit
    highest_credit_user = max(data, key=lambda x: x["credit"])

    # Aggregate total debit by city
    debit_by_city = defaultdict(int)
    for user in data:
        debit_by_city[user["city"]] += user["debit"]

    return highest_credit_user, dict(debit_by_city)


def main():
    try:
        user_data = fetch_user_data(API_URL)

        highest_user, debit_per_city = analyze_credits(user_data)

        print(f"User with highest credit: {highest_user['username']} (${highest_user['credit']})")
        print("\nTotal debit per city:")
        for city, total_debit in debit_per_city.items():
            print(f"{city}: ${total_debit}")

    except requests.exceptions.RequestException as e:
        print("API request failed:", e)
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    main()
