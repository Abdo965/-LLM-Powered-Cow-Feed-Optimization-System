import streamlit as st
from scraper import Scraper
from llm import CowRecommender

# Load API key from secrets or fallback
API_KEY = st.secrets["GEMINI_API_KEY"] if "GEMINI_API_KEY" in st.secrets else "AIzaSyBqZTixI9qEM0VkCRp3fWXm5EgZ87_ndp8"

# Initialize tools
scraper = Scraper()
recommender = CowRecommender()

st.set_page_config(page_title="Cow Food Recommendation", layout="wide")
st.title("Cow Food Recommendation System")

# ------------------ Step 1: URL Inputs ------------------
if "urls_fetched" not in st.session_state:
    st.header("Step 1: Enter URLs")

    num_urls = st.number_input("Number of URLs", min_value=1, max_value=10, value=1)
    url_inputs = []

    cols = st.columns(2)
    for i in range(num_urls):
        with cols[i % 2]:
            url = st.text_input(f"URL {i + 1}", key=f"url_{i}")
            url_inputs.append(url.strip())

    if st.button("Continue"):
        scraped_data = []
        for i, url in enumerate(url_inputs):
            if url:
                result = scraper.fetch(url)
                scraped_data.append(result)
            else:
                st.warning(f"URL {i + 1} is empty.")

        st.session_state['scraped_data'] = scraped_data
        st.session_state['urls_fetched'] = True
        st.rerun()

# ------------------ Step 2: Cow Details ------------------
if st.session_state.get("urls_fetched"):
    st.header("Step 2: Enter Cow Details")

    with st.form("cow_details_form"):
        age = st.number_input("Age of the Cow (in years)", min_value=0.0, step=0.1)
        weight = st.number_input("Weight of the Cow (in kg)", min_value=0.0, step=1.0)
        purpose = st.selectbox("Purpose of the Cow", ["Milk Production", "Meat", "Breeding", "Other"])
        submit = st.form_submit_button("Submit Cow Details")

    if submit:
        texts = [item['content'] for item in st.session_state['scraped_data'] if 'content' in item]
        cow_info = {
            'age': age,
            'weight': weight,
            'purpose': purpose
        }
        with st.spinner("Generating food recommendation..."):
            recommendation = recommender.recommend(texts, cow_info)
            st.subheader("Recommended Food Combination")
            st.write(recommendation)