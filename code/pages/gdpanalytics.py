import streamlit as st
from dashboard import dashboard_page
import json
import os
import re
from home import home_page  # Import the home page function
from queriesandfeedback import queries_page  # Import queries and feedback page
from conclusion import conclusion_page

# File to store user data
USER_DATA_FILE = "user_data.json"

# Check if the user data file exists, if not create an empty one
if not os.path.exists(USER_DATA_FILE):
    with open(USER_DATA_FILE, "w") as f:
        json.dump({}, f)


# Function to load users from the JSON file
def load_users():
    with open(USER_DATA_FILE, "r") as f:
        return json.load(f)


# Function to save users to the JSON file
def save_users(users):
    with open(USER_DATA_FILE, "w") as f:
        json.dump(users, f)


# Function to handle login
def login_page():
    st.title("🔑 Login Page")

    # User input for login
    user_id = st.text_input("👤 Enter User ID", key="user_id_input_login")
    password = st.text_input(
        "🔒 Enter Password", type="password", key="password_input_login"
    )

    if st.button("🚪 Login"):
        users = load_users()
        if user_id in users and users[user_id]["password"] == password:
            st.session_state.logged_in = True  # Set session state to logged in
            st.session_state.user_id = user_id  # Store the user_id in session state
            st.success("✅ Login successful!")
            st.session_state.page = "home"  # Set default page to home
            st.rerun()  # Trigger a rerun to go to the home page
        else:
            st.error("❌ Invalid credentials.")


# Function to handle sign-up
def sign_up():
    st.title("📝 Sign Up Page")

    users = load_users()
    email = st.text_input(
        "📧 Enter Email", key="email_input_signup", placeholder="e.g., user@example.com"
    )
    user_id = st.text_input(
        "🆔 Enter User ID",
        key="user_id_input_signup",
        placeholder="Choose a unique username",
    )
    password = st.text_input(
        "🔑 Enter Password",
        type="password",
        key="password_input_signup",
        placeholder="Minimum 8 characters",
    )
    confirm_password = st.text_input(
        "🔄 Confirm Password",
        type="password",
        key="confirm_password_input_signup",
        placeholder="Re-enter your password",
    )
    pet_name = st.text_input(
        "🐶 What is your first pet's name?",
        key="pet_name_input_signup",
        placeholder="For security questions",
    )
    school_name = st.text_input(
        "🏫 What is the name of your school?",
        key="school_name_input_signup",
        placeholder="For security questions",
    )

    if st.button("✅ Sign Up"):
        # Email validation
        email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(email_regex, email):
            st.error("❌ Please enter a valid email address.")
            return

        # Password validation
        if len(password) < 8:
            st.error("❌ Password must be at least 8 characters long.")
            return
        if not re.search(r"[A-Z]", password) or not re.search(r"[a-z]", password):
            st.error("❌ Password must include both uppercase and lowercase letters.")
            return
        if not re.search(r"[0-9]", password):
            st.error("❌ Password must include at least one number.")
            return
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            st.error("❌ Password must include at least one special character.")
            return

        # Confirm password match
        if password != confirm_password:
            st.error("❌ Passwords do not match.")
            return

        # Check if user ID already exists
        if user_id in users:
            st.error("❌ User ID already exists.")
            return

        # Save new user
        users[user_id] = {
            "email": email,
            "password": password,
            "pet_name": pet_name,
            "school_name": school_name,
        }
        save_users(users)
        st.success("✅ Account created successfully!")

        # Redirect to login page
        st.session_state.page = "home"  # Set default page to home
        st.rerun()


def forgot_password():
    st.title("🔑 Forgot Password")

    users = load_users()
    user_id = st.text_input("👤 Enter Your User ID", key="user_id_input_forgot")

    if user_id not in users:
        if st.button("🔍 Verify User ID"):
            st.error("❌ User ID does not exist.")
        return

    st.success("✅ User ID verified.")

    pet_name = st.text_input(
        "🐶 What is your first pet's name?", key="pet_name_input_forgot"
    )
    school_name = st.text_input(
        "🏫 What is the name of your school?", key="school_name_input_forgot"
    )

    if st.button("✅ Verify Answers"):
        if pet_name == users[user_id].get("pet_name") and school_name == users[
            user_id
        ].get("school_name"):
            st.success("✅ Answers verified.")
            new_password = st.text_input(
                "🔑 Enter New Password", type="password", key="new_password_input"
            )
            confirm_new_password = st.text_input(
                "🔄 Confirm New Password",
                type="password",
                key="confirm_new_password_input",
            )

            if st.button("🔄 Reset Password"):
                if new_password != confirm_new_password:
                    st.error("❌ Passwords do not match.")
                elif len(new_password) < 8:
                    st.error("❌ Password must be at least 8 characters long.")
                else:
                    users[user_id]["password"] = new_password
                    save_users(users)
                    st.success("✅ Password reset successfully!")
                    st.session_state.page = "home"  # Set default page to home
                    st.rerun()  # Redirect back to the login page
        else:
            st.error("❌ Security answers are incorrect.")


# Add custom CSS for theme (Golden, White, Black)
def add_custom_css():
    st.markdown(
        """
        <style>
        body {
            background-color: black; /* Black background for the whole body */
            color: white; /* White text */
            font-family: 'Arial', sans-serif;
        }
        .stButton>button {
            background-color: #ffd700; /* Golden color for buttons */
            color: black;
            border: none;
            border-radius: 5px;
            padding: 1px 0px;
            font-weight: bold;
        }
        .stButton>button:hover {
            background-color: #ffcc00; /* Lighter golden when hovered */
        }
        .stTextInput>div>input {
            background-color: #333333; /* Dark background for text inputs */
            color: white;
            border: 1px solid #ffd700; /* Golden border */
        }
        .stTextInput>div>input:focus {
            border: 2px solid #ffd700; /* Golden border on focus */
        }
        .stRadio>div>label {
            color: white; /* White color for radio labels */
        }
        .stTitle {
            color: #ffd700; /* Golden color for titles */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def main_page():
    # Initialize session state for page navigation
    if "page" not in st.session_state:
        st.session_state.page = "home"  # Default to home page

    # Check if the user is logged in
    if "logged_in" in st.session_state and st.session_state.logged_in:
        # Sidebar navigation with icons
        page = st.sidebar.radio(
            "🔽 Navigate",
            ["🏠 Home", "📊 Dashboard", "💬 Queries & Feedback", "📜 Conclusion"],
        )

        if page == "🏠 Home":
            st.session_state.page = "home"
            home_page()  # Home page
        elif page == "📊 Dashboard":
            st.session_state.page = "dashboard"
            dashboard_page()  # Dashboard page
        elif page == "💬 Queries & Feedback":
            # Redirect to the Queries and Feedback page
            st.session_state.page = "queries"
            queries_page()  # Queries and feedback page
        elif page == "📜 Conclusion":
            st.session_state.page = "conclusion"
            conclusion_page()  # Conclusion page
    else:
        choice = st.sidebar.radio(
            "🔑 Select action", ["🔐 Login", "📝 Sign Up", "❓ Forgot Password"]
        )

        if choice == "🔐 Login":
            login_page()  # Show login page
        elif choice == "📝 Sign Up":
            sign_up()  # Show sign-up page
        elif choice == "❓ Forgot Password":
            forgot_password()  # Show forgot password page


add_custom_css()

# Running the main page function
if __name__ == "__main__":
    main_page()
