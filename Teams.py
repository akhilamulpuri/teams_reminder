import streamlit as st
import pandas as pd
import webbrowser
import time
import random

st.title("Teams Reminder Sender")

st.write("Upload an Excel file with columns: Name and Email")

uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx"])

default_message = "The Finance Team has created the Travel Expense Report for your company-paid travel under the title 'IN AP/SME'. Kindly submit the report by the End of the Day."

message = st.text_area("Enter Reminder Message", default_message)

if uploaded_file is not None:

    df = pd.read_excel(uploaded_file)
    df.columns = df.columns.str.strip()

    st.subheader("Preview of Data")
    st.dataframe(df)

    if st.button("Send Teams Messages"):

        for index, row in df.iterrows():

            name = str(row["Name"])
            email = str(row["Email"])

            final_message = f"Hi {name}, {message}"

            try:

                url = f"https://teams.microsoft.com/l/chat/0/0?users={email}"
                webbrowser.open(url)

                time.sleep(8)

                pyautogui.write(final_message, interval=0.02)
                pyautogui.press("enter")

                st.write(f"Message sent to {name}")

                time.sleep(random.uniform(5,7))

            except Exception as e:
                st.write(f"Error sending to {name}: {e}")

        st.success("Finished sending messages!")

