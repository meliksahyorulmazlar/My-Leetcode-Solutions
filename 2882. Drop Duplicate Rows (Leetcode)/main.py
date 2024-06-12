import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    ids = []
    names = []
    emails = []
    for (index,row) in customers.iterrows():
        email = row["email"]
        if email not in emails:
            ids.append(row["customer_id"])
            names.append(row["name"])
            emails.append(email)

    return pd.DataFrame({"customer_id":ids,"name":names,"email":emails})