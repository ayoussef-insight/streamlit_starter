import streamlit as st
import requests

st.title('Search the web')

def search_bing(query, api_key):
    # Set up Bing Search API endpoint and headers
    search_url = "https://api.bing.microsoft.com/v7.0/search"
    headers = {"Ocp-Apim-Subscription-Key": api_key}
    params = {"q": query, "textDecorations": True, "textFormat": "HTML"}

    # Send request to Bing API
    response = requests.get(search_url, headers=headers, params=params)
    
    # If request is successful, return the JSON response
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error fetching data from Bing: {response.status_code}")
        return None


# Input field for user to enter search keyword
search_query = st.text_input("Enter search keywords", "")

# Button to trigger the search
if st.button("Search"):
    # Check if user has entered a keyword
    if search_query:
        # Perform the search using the Bing Search API
        api_key = "d4d1d36b1ac4426f8ab781fd59ce5fff"  # Replace with your actual API key
        results = search_bing(search_query, api_key)
        
        # If results were found, display them
        if results:
            st.subheader("Search Results:")
            for result in results['webPages']['value']:
                st.markdown(f"**[{result['name']}]({result['url']})**")
                st.markdown(result['snippet'], unsafe_allow_html=True)
                st.markdown("---")
    else:
        st.warning("Please enter a keyword to search.")



