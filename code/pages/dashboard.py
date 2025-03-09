import streamlit as st
import streamlit.components.v1 as components


# Function to show the Dashboard page
def dashboard_page():
    st.title("📊 Dashboard Page")

    # Set the background color and styling for the page
    st.markdown(
        """
        <style>
        body {
            background-color: black;
            color: white;
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            overflow: hidden;
        }
        .container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            width: 100%;
        }
        .section-title {
            color: #ffd700;  /* Gold color for section titles */
            font-size: 24px;
            font-weight: bold;
        }
        .metrics-box, .insights-box {
            background-color: #2c3e50;
            color: white;
            padding: 15px;
            margin: 1px 0;
            border-radius: 1px;
        }
        .stButton>button {
            background-color: #ffd700;
            color: black;
            font-weight: bold;
            border-radius: 1px;
        }
        .stButton>button:hover {
            background-color: #ffcc00;  /* Lighter gold on hover */
        }
        iframe {
            border: none;
            border-radius: 1px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Container for the content
    st.markdown('<div class="container">', unsafe_allow_html=True)

    # Power BI embed URL
    iframe_code = """
    <iframe src="https://app.powerbi.com/reportEmbed?reportId=5efa531a-0c8e-4c7b-9b67-241445c121e8&autoAuth=true&ctid=defaac15-971a-4463-ac80-f44094ac5129"
            width="1000" height="600" allowFullScreen="true">
    </iframe>
    """

    # Embed the iframe using Streamlit's components
    components.html(iframe_code, height=600, width=1000)

    # Key Metrics Section
    st.markdown("<div class='section-title'>Key Metrics</div>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class="metrics-box">
            <b>Total GDP of India (2025):</b> $3.385 Trillion
        </div>
        <div class="metrics-box">
            <b>Top 3 Cities by GDP:</b> Mumbai, Delhi, Bangalore
        </div>
        <div class="metrics-box">
            <b>Highest State GDP:</b> Maharashtra
        </div>
        <div class="metrics-box">
            <b>Average City GDP Growth Rate (2025):</b> 6.4%
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Insights Section
    st.markdown("<div class='section-title'>Insights</div>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class="insights-box">
            1. Mumbai contributes the highest GDP, making it a key financial hub.
        </div>
        <div class="insights-box">
            2. GDP growth in southern cities like Bangalore and Chennai is outpacing the national average.
        </div>
        <div class="insights-box">
            3. Maharashtra remains the top-performing state in terms of GDP, owing to its large industrial base.
        </div>
        <div class="insights-box">
            4. There is a rising trend in the GDP of tier-2 cities, signaling emerging economic powerhouses.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # End the container div
    st.markdown("</div>", unsafe_allow_html=True)


# Running the dashboard page function
if __name__ == "__main__":
    dashboard_page()
