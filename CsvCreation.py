import pandas as pd
import requests

# Define the API endpoint
api_url = "https://jsonplaceholder.typicode.com/users"

# Send a GET request to the API
response = requests.get(api_url)

# Check if the request was successful
if response.status_code == 200:
    
    # Data Parsing
    data = response.json()

    # Create a DataFrame using Pandas
    df = pd.DataFrame(data)

    # Columns which I want in csv file
    columns_to_include = ["id", "name", "email", "phone", "website"]

    # Storing the data in new dataframe 
    x = df[columns_to_include]

    # Save the DataFrame to a CSV file
    x.to_csv("UserData.csv", index=False)

    print("CSV dataset created successfully.")
else:
    print("Failed to retrieve data from the API.")