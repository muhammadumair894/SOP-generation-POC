import streamlit as st

# Define the URL of the chatbot
chatbot_url ="https://chat.dante-ai.com/embed?kb_id=b1bee034-13ad-489c-98c1-973b67efba93&token=491d98c0-bca0-4d19-bcf9-557f2a35b1d4&modeltype=gpt-4&logo=dHJ1ZQ=="

# Define the height of the iframe
iframe_height = 500

# Define the Streamlit app
def app():
    # Set the app title
    st.set_page_config(page_title="Chatbot App", page_icon=":robot_face:")

    # Add a header
    st.header("Welcome to SOP Generation POC")

    # Define the iframe code as a string
    iframe_code = f'<iframe src="{chatbot_url}" width="125%" height="{iframe_height}" frameborder="0"></iframe>'

    # Add the iframe to the app using markdown
    st.markdown(iframe_code, unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    app()
