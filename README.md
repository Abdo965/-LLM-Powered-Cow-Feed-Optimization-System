# LLM-Powered Livestock Health Monitoring System  

## Overview  
An AI-driven livestock health monitoring system utilizing **Large Language Models (LLMs)** and deep learning to detect diseases in cows, specifically **Lumpy Skin Disease** and **Mastitis Disease**. Farmers can upload images, receive automated diagnoses, and generate detailed veterinary reports using **Streamlit**.  

## Features  
- 🧠 **AI-Based Disease Detection**: Uses trained models to classify cow health conditions.  
- 📜 **LLM-Powered Report Generation**: Automatically creates professional veterinary health reports.  
- 🖥️ **User-Friendly Interface**: Streamlit simplifies interactions for farmers.  
- ⏳ **Real-Time Monitoring & Alerts**: Provides early warning for potential infections.  

---
## Set Up Environment Variables
  - **Create a .env file in the project directory and add your API keys and configurations:
  - **GOOGLE_API_KEY=your-api-key-here

## 🚀 Installation Guide  

### 📥 1. Clone the Repository  
Run the following command in your terminal:  
```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
# Create and activate virtual environment
python -m venv venv  
source venv/bin/activate  # Use venv\Scripts\activate for Windows

# Install dependencies
pip install -r requirements.txt  

# Run the application
streamlit run app.py  
