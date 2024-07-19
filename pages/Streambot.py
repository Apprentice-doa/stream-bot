import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Streambot", page_icon="🌍")

st.title("Streambot")

container = st.container()
with container:
    st.write("", style={"width": "100%", "text-align": "center"})
    st.markdown("<h6 style='text-align: center; color: white;'>Developed by Kelvin. </h6>", unsafe_allow_html=True)

#st.sidebar.header("Streambot")

# Set OpenAI API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Set a default model
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4o"

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
        # Assume the assistant persona with a background in career guidance
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


