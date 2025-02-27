import pandas as pd


def process_text(user_content: pd.DataFrame) -> pd.DataFrame:
    original = []
    converted = []
    ids = []
    for index, row in user_content.iterrows():
        ids.append(row['content_id'])
        new = row['content_text']
        original.append(new)
        new = " ".join([n.title() for n in new.split(" ")])
        converted.append(new)

    return pd.DataFrame({'content_id': ids, "original_text": original, 'converted_text': converted})
