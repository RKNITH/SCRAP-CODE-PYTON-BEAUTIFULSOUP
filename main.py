import requests

# Function to get website source code
def get_website_source(url):
    try:
        # Send a request to the website
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Return the source code of the website
            return response.text
        else:
            return f"Failed to retrieve content. Status code: {response.status_code}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Example usage
url = 'www.abc.com'  # Replace with the URL of the website you want to scrape
website_code = get_website_source(url)
print(website_code)
