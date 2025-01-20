import streamlit as st
import requests

# Prepare API key and API url
API_KEY = "UxVIn7D3jKqaWsiUqAAgxxxLBag606i9dbSjMcb9"
url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"

# Get the data
request = requests.get(url)
# Convert the data to dictionary
content = request.json()

# Get the url of the image
response = requests.get(content['url'])

# Download and save the image as 'image.jpg'
with open("image.jpg", "wb") as file:
    file.write(response.content)

# Set the title
st.title(content['title'])
# Set the image
st.image("image.jpg", caption=content['title'])
# Display the date of the content
st.write(f"Date: {content['date']}")
# Display the content
st.write(content['explanation'])