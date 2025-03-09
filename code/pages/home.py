import streamlit as st
import pandas as pd


# Add custom CSS for the theme
def add_custom_css():
    st.markdown(
        """
        <style>
        body {
            background-color: black;
            color: white;
            font-family: 'Arial', sans-serif;
        }
        .stButton>button {
            background-color: #ffd700; /* Gold color for buttons */
            color: black;
            font-weight: bold;
            border-radius: 5px;
        }
        .stButton>button:hover {
            background-color: #ffcc00; /* Lighter gold on hover */
        }
        .stTitle {
            color: #ffd700; /* Gold color for titles */
        }
        .stTextInput>div>input {
            background-color: #333333;
            color: white;
            border: 1px solid #ffd700;
        }
        .stTextInput>div>input:focus {
            border: 2px solid #ffd700;
        }
        .stMarkdown {
            color: white;
        }
        .stTable {
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


# Function to display GDP data and visualizations
def home_page():
    if "logged_in" not in st.session_state or not st.session_state.logged_in:
        st.error("❌ You must log in to access this page.")
        st.experimental_set_query_params(page="main")  # Redirect back to login
        return

    # Title with emoji
    st.title("🇮🇳 Indian GDP Overview")

    # Definition of GDP
    st.markdown("### 📚 Definition of GDP")
    st.markdown(
        """
        GDP, or Gross Domestic Product, is the total monetary value of all goods and services
        produced within a country's borders in a specific time period. It is an essential indicator
        of a country's economic health and a tool for comparing the economic performance of
        different countries.
        """
    )

    st.markdown("### 🌍 India's GDP in Global Context")
    st.markdown(
        """
        India is one of the fastest-growing economies globally, with its GDP ranking among the
        top 5 in the world. This comparison highlights India's economic position relative to
        other major economies.
        """
    )

    # Data for visualizations (example data)
    data = {
        "City": ["Mumbai", "Delhi", "Bangalore", "Chennai", "Hyderabad"],
        "GDP (in billion USD)": [300, 250, 200, 150, 120],
    }
    df = pd.DataFrame(data)

    # Top cities GDP visualization
    st.markdown("### 🏙️ Top Cities by GDP (Last 5 Years)")
    st.table(df)

    st.markdown("### 📊 Highest State GDP ")
    state_gdp = {
        "State": ["Maharashtra", "Tamil Nadu", "Gujarat", "Uttar Pradesh", "Karnataka"],
        "GDP (in trillion INR)": [39, 24.8, 22.6, 21.6, 21],
    }
    state_df = pd.DataFrame(state_gdp)
    st.table(state_df)

    # Visualization example
    st.markdown("### 🗺️ Indian Map with GDP Highlights")
    st.image(
        "D:\GDP and Productivity of Indian Cities\pictures\India-GDP-Chart.jpg",
        caption="GENERAL REPORT",
        use_container_width=True,
    )

    # Add comparison table
    global_comparison = {
        "Country": ["USA", "China", "Japan", "Germany", "India"],
        "GDP (in trillion USD)": [23, 17, 5, 4.5, 3.5],
    }
    global_df = pd.DataFrame(global_comparison)
    st.markdown("### 🌎 India's GDP Compared to Other Countries")
    st.table(global_df)


# Add CSS and run the home page function
add_custom_css()

if __name__ == "__main__":
    home_page()
