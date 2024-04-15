import streamlit as st
import pandas as pd
import matplotlib as plt
import os
from pandasai import SmartDataframe
from pandasai.llm.openai import OpenAI
from pandasai import Agent

# GUI and chatbot connection
st.title("PIT BOT")
st.write("Hi, I am PIT Bot, I collected Enterprise meta data and I can understand human language and happy to provide you insights about the data!")
st.session_state.prompt_history = []

with st.form("Question"):
    question = st.text_input("Question", value="", type="default")
    submitted = st.form_submit_button("Submit")
    if submitted:
        with st.spinner():
            llm = OpenAI()
            sdf1 = SmartDataframe('mock_app_data.csv', config={"llm": llm})
            sdf2 = SmartDataframe('mock_resource_data.csv', config={"llm": llm})

            agent = Agent(
                [sdf1, sdf2],
                config={"llm": llm},
                description=
                "You have two tables, the mock_app_data has the basic descriptive information of all the applications, " +
                "and each application has an ID in the column id which is an unique identifier of each application. " + 
                "The mock_resource_data table indicated the resources each application use. Each application can have multiple resources, and each resource has an app_id indicated which application the resource(s) belongs to." +
                "Using the two tables, you can identify the descriptive information of each application, such as the owner of the application, the email address of the owner, " + 
                "the organization the app belongs to, and the resources being used by each app and the online status of the application. " +
                "Your job is to provide insights to the non-techincal users about the application information."
            )

            response = agent.chat(question)

            if response is not None:
                st.write(response)
            st.session_state.prompt_history.append(question)

if st.button("Clear the history"):
    st.session_state.prompt_history = []
