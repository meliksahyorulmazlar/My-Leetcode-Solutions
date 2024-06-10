import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    x = players.shape
    return [x[0],x[1]]
