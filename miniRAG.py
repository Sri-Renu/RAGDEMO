import streamlit as st
from googleapiclient.discovery import build

API_KEY = os.getenv("GOOGLE_API_KEY")
CX = os.getenv("GOOGLE_CX")

def google_search(query,api_key,cse_id,num=3):
    """Run a GOOGLE CUSTOM SEARCH and return results. """
    service=build("customsearch","v1",developerKey=api_key)
    res = service.cse().list(q=query,cx=cse_id,num=num).execute()
    return res.get("items",[])

st.title("Mini RAG Demo with Google Search")

query=st.text_input("Enter your search query:")

if query:
    results=google_search(query,API_KEY,CX)

    if results:
        st.subheader("Search Results:")
        for item in results:
            st.write(f"-**{item['title']}**:{item['snippet']}")
            st.write(item['link'])

    else:
        st.write("No result found.")