import streamlit as st


# Function to display the Conclusion page
def conclusion_page():
    st.title("🔍 Conclusion")

    # Add custom CSS for styling
    st.markdown(
        """
        <style>
        body {
            background-color: black;
            color: white;
            font-family: 'Arial', sans-serif;
        }
        .stMarkdown {
            color: white;
        }
        .highlight {
            color: #ffd700; /* Gold color for highlights */
            font-weight: bold;
        }
        .stButton>button {
            background-color: #ffd700;
            color: black;
            font-weight: bold;
            border-radius: 5px;
        }
        .stButton>button:hover {
            background-color: #ffcc00; /* Lighter gold on hover */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Display the conclusion content
    st.markdown("### 🌟 Key Insights")
    st.markdown(
        """
        - The data reveals that India's **GDP growth** is significantly influenced by urban development, 
          technological innovation, and industrial expansion.
        - Maharashtra, Tamil Nadu, and Karnataka emerge as top contributors to the national GDP.
        - India holds a strong global position, ranking among the top 5 economies, and continues to grow rapidly.
        """
    )

    st.markdown("### 📈 Future Prospects")
    st.markdown(
        """
        - With increased investment in infrastructure, education, and technology, India is poised for **long-term growth**.
        - Further analysis could incorporate **real-time data** for more accurate predictions and insights.
        - Government policies promoting entrepreneurship and innovation could further bolster GDP growth.
        """
    )

    st.markdown("### 🙏 Thank You!")
    st.markdown(
        """
        We hope this platform provided valuable insights into India's economic landscape.
        Please feel free to explore other pages or reach out via the Queries & Feedback page for any suggestions or questions.
        """
    )


# Running the conclusion page function
if __name__ == "__main__":
    conclusion_page()
