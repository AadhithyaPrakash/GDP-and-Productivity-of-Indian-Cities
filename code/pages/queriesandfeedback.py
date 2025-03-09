import streamlit as st
from openai import OpenAI  # noqa: F401


# Function for the Queries and Feedback page
def queries_page():
    st.title("Queries and Feedback")

    # Feedback Form
    st.subheader("📬 Send us your Feedback")

    # HTML for embedding iframe with custom CSS styling
    st.markdown(
        """
        <style>
            /* Global background and text color */
            body {
                background-color: black;
                color: white;
                font-family: 'Arial', sans-serif;
            }

            /* Iframe styling */
            .iframe-container {
                width: 100%;
                height: 600px;
                border: none;
                border-radius: 15px;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3);
                background-color: black;
            }

            /* Form info text styling */
            .form-info {
                font-size: 14px;
                color: white;
                text-align: center;
                margin-top: 20px;
            }

            /* Icon styling */
            .icon {
                font-size: 28px;
                color: gold;
                text-align: center;
            }

            /* Chat container styling */
            .chat-container {
                background-color: black;
                color: white;
                border-radius: 10px;
                padding: 10px;
                margin-bottom: 10px;
                max-width: 90%;
                display: flex;
                flex-direction: column;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.5);
            }

            /* Chat bubbles */
            .chat-bubble {
                border-radius: 15px;
                padding: 10px;
                margin: 5px;
                max-width: 70%;
            }

            .chat-bubble-you {
                background-color: gold;
                color: black;
                align-self: flex-end;
            }

            .chat-bubble-chatbot {
                background-color: white;
                color: black;
                align-self: flex-start;
            }

            /* Chat icon */
            .chat-icon {
                font-size: 20px;
                color: gold;
                margin-right: 10px;
            }

            /* User input box */
            .input-box {
                border-radius: 15px;
                padding: 10px;
                background-color: #333;
                color: white;
                font-size: 16px;
                margin-top: 10px;
                width: 100%;
                border: 2px solid gold;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Set OpenAI API key from Streamlit secrets
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
    """
    # Set a default model
    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-3.5-turbo"

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("your query?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            stream = client.chat.completions.create(
                model=st.session_state["openai_model"],
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                stream=True,
            )

            # Iterate over the response stream and display each chunk
            response = ""
            for chunk in stream:
                response += chunk["choices"][0]["delta"].get("content", "")
                st.markdown(response)

        st.session_state.messages.append({"role": "assistant", "content": response})
        """
    # Embed Feedback Form with iframe
    st.markdown(
        """
        <div class="iframe-container">
            <iframe src="https://formsubmit.co/el/nohave" width="100%" height="100%"></iframe>
        </div>
        
        <p class="form-info">Your feedback will be sent to our email address upon submission. We appreciate your thoughts!</p>
        <p class="icon">📬</p>
        """,
        unsafe_allow_html=True,
    )

    # Keep the form and chat visible
    st.markdown("---")


# Example usage of the queries_page function
if __name__ == "__main__":
    queries_page()
