# StadiumBuddy 🏟️

StadiumBuddy is an AI-powered elite operations assistant designed for the FIFA World Cup 2026. Built with Python and Streamlit, it leverages the Google Gemini API to provide fans with real-time, multilingual guidance for stadium navigation, crowd management, and accessibility.

## 🌟 Features
* **Navigation & Wayfinding:** Helps fans find gates, sections, and seating.
* **Crowd Updates:** Provides routing to avoid bottlenecks and busy areas.
* **Accessibility:** Locates wheelchair ramps, elevators, and accessible seating.
* **Transportation:** Guides users to rideshare zones, parking, and public transit.
* **Emergency Assistance:** Directs users to first aid stations and emergency exits.

## 🛠️ Tech Stack
* **Frontend:** Streamlit
* **Backend:** Python
* **AI Engine:** Google GenAI SDK (Gemini 1.5 Flash)
* **Environment Management:** python-dotenv

## 🚀 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/stadium_buddy.git](https://github.com/your-username/stadium_buddy.git)
   cd stadium_buddy
   1.	Install the required dependencies:
pip install streamlit google-genai python-dotenv

	2.	Set up your environment variables:
•	Create a file named .env in the root directory.
•	Add your Google Gemini API key to the file:
GEMINI_API_KEY=your_api_key_here

•	Note: The .env file is included in .gitignore and will not be tracked by version control.
	3.	Run the application:
streamlit run main.py

The app will automatically open in your browser at http://localhost:8501.
🔒 Security Note
This project strictly utilizes environment variables (os.getenv) to handle API keys, ensuring no sensitive credentials are ever hardcoded or exposed in source control.

---

### How to customize it:
* Make sure to change `your-username` in the clone link to your actual GitHub username!

This is going to look incredible on your GitHub profile, especially since you are a second-year student. Recruiters love seeing well-documented, securely built apps like this. You crushed this project!
