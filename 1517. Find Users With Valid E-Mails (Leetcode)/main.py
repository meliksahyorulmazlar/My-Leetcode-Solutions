import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    ids = []
    names = []
    emails = []
    allowed = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',"_",".","-",'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',"0","1","2","3",'4',"5","6","7","8","9"]


    for (index,row) in users.iterrows():
        email = row["mail"]
        if email[0].isalpha():
            if "@" in email:
                parts = email.split("@")
                if parts[1] == "leetcode.com":
                    length = len(parts[0])
                    count = 0
                    for item in parts[0]:
                        if item in allowed:
                            count += 1
                    if count == length:
                        ids.append(row["user_id"])
                        names.append(row["name"])
                        emails.append(row["mail"])
    return pd.DataFrame({"user_id":ids,"name":names,"mail":emails})