import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    emails = {}
    for (index,row) in person.iterrows():
        email = row["email"]
        if email not in emails:
            emails[email] = 1
        else:
            emails[email] += 1

    chosen = []
    for email in emails:
        if emails[email] > 1:
            chosen.append(email)
    return pd.DataFrame({"Email":chosen})