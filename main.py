import streamlit as st
import pandas as pd
import matplotlib as plt
from pandasai import SmartDataframe
from pandasai.llm.openai import OpenAI
from pandasai import Agent

#ingest mock data to dataframe
# sdf1 = SmartDataframe('MOCK_APP_DATA.csv', config={"llm": llm})
# sdf2 = SmartDataframe('MOCK_RESOURCE_DATA.csv', config={"llm": llm})

# agent = Agent(
#     [sdf1, sdf2],
#     config={"llm": llm},
#     description=""
# )

# response = agent.chat("make graph to show the online status in each app_org")
# print(response)

# GUI
st.title("Talk to Enterprise Meta Data")
st.write("What's up!")
st.session_state.prompt_history = []

with st.form("Question"):
    question = st.text_input("Question", value="", type="default")
    submitted = st.form_submit_button("Submit")
    if submitted:
        with st.spinner():
            llm = OpenAI()

            sdf1 = SmartDataframe('MOCK_APP_DATA.csv', config={"llm": llm})
            sdf2 = SmartDataframe('MOCK_RESOURCE_DATA.csv', config={"llm": llm})

            agent = Agent(
                [sdf1, sdf2],
                config={"llm": llm},
                description=
                "You have two tables, the MOCK_APP_DATA has the basic descriptive information of all the applications, " +
                "and each application has an ID in the column id which is an unique identifier of each application. " + 
                "The MOCK_RESOURCE_DATA table indicated the resources each application use. Each application can have multiple resources, and each resource has an app_id indicated which application the resource(s) belongs to." +
                "Using the two tables, you can identify the descriptive information of each application, such as the owner of the application, the email address of the owner, " + 
                "the organization the app belongs to, and the resources being used by each app and the online status of the application. " +
                "Your job is to provide insights to the non-techincal users about the application information."
            )

            response = agent.chat(question)

            if response is not None:
                st.write(response)

            st.session_state.prompt_history.append(question)