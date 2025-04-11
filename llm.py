import google.generativeai as genai

class CowRecommender:
    def __init__(self, api_key="AIzaSyBqZTixI9qEM0VkCRp3fWXm5EgZ87_ndp8"):  # Fix: init not init
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-2.0-flash-exp")

    def recommend(self, scraped_texts, cow_details):
        joined_text = "\n\n".join(scraped_texts)
        prompt = f"""
You are an expert in only cow  nutrition.

Based on the following data from online sources :
{joined_text} extract only the data of cows'nutrition

And the cow details:
- Age: {cow_details['age']} years
- Weight: {cow_details['weight']} kg
- Purpose: {cow_details['purpose']}

Please provide the best food combination recommendation for this cow from different resources and compare the similar price between each provider and give me the best one in araibc and make it more simple to a farmer.
"""
        response = self.model.generate_content(prompt)
        return response.text

