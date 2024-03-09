import streamlit as st
from openai import OpenAI

st.title("Chat Assitant")

title = st.text_input('Favourite courses')
title = st.text_input('Do you like working independently or with company?')
title = st.text_input('long term career goals')
title = st.text_input('what inspires you')
title = st.text_input('skills and talents')
# Set OpenAI API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

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

# prompt_engineered_messages =  [
#         # Assume the assistant persona with background in career guidance
#                 {"role": "system", "content": "You are an AI knowledgeable in career advice for students and businesses."},
#                   *[{"role": m["role"], "content": m["content"]} 
#                 for m in st.session_state.messages]
#             ]

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    prompt_engineered_messages = [
        # Assume the assistant persona with background in career guidance
        {"role": "system", "content": "You are an AI knowledgeable in career advice for students and businesses. Don't give any infromation or response not within the framework of career advice for students and business"},
        *[
            {"role": m["role"], "content": m["content"]}
            for m in st.session_state.messages
        ],
        {"role": "user", "content": prompt}
    ]
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

 # Display assistant response in chat message container
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            # messages=[
            #     {"role": m["role"], "content": m["content"]}
            messages = prompt_engineered_messages,
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})
