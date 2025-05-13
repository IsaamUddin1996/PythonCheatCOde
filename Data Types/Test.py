import requests

url = "https://www.artificial-intelligence.blog/"
response = requests.get(url)

# Print response headers to check content type
print("Content-Type:", response.headers.get("Content-Type"))

# Print the actual response text (for debugging)
print("Response Text:", response.text[:200])  # Print only first 200 characters
