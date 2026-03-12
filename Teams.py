import pandas as pd
import webbrowser
import pyautogui
import time
import random

EXCEL_FILE = r"C:\Users\Akhila.Mulpuri\OneDrive - GEP\Documents\invoices.xlsx"

df = pd.read_excel(EXCEL_FILE)
df.columns = df.columns.str.strip()

for index, row in df.iterrows():

    name = str(row["Name"])
    email = str(row["Email"])

    message = f"Hi {name},The Finance Team has created the Travel Expense Report for your company-paid travel under the title 'IN AP/SME'.Kindly submit the report by the End of the Day."

    try:

        # Open chat directly
        url = f"https://teams.microsoft.com/l/chat/0/0?users={email}"
        webbrowser.open(url)

        # Wait for Teams to open chat
        time.sleep(8)

        # Type message
        pyautogui.write(message, interval=0.02)
        pyautogui.press("enter")

        print(f"Message sent to {name}")

        time.sleep(random.uniform(5,7))

    except Exception as e:
        print(f"Error sending to {name}: {e}")

print("Finished sending messages")
