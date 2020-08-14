import pandas as pd
import numpy as np
import re
import time


def answer_five():
    cs = pd.read_csv("census.csv")
    # this is unnecessary u only need to set "STNAME" as index but whatever i worked around it
    cs.set_index(['STNAME', 'CTYNAME'], inplace=True)
    lenn = len(cs.index)
    # setting the values to 0 with the len being the number if states taken from SUMLEV == 40
    srr = pd.Series([0]*len(cs[cs["SUMLEV"] == 40])
                    # setting the index as the state name by masking and leaving only the States then resetting the
                    # index of this image of cs to get only STNAME
                    , index=cs[cs["SUMLEV"] == 40].reset_index()["STNAME"])
    """
    SUMLEV column is columns 0
    to look for a specific item PLEASE USE .loc or .iloc
    .iloc takes [index of raw, index of column]
    .loc takes [name of raw, name of column]
    NO NEED FOR NESTED FOR ur first for already go through all values 
    be smart and use the series but first set all of its values  to 0
    BTW this is not the best way but at least this is a more pandorable ((week 3 video 2))
    """
    for i in range(lenn):
        count = 0
        if cs.iloc[i, 0] == 50:
            count += 1
            # cs.index[i][0] returns the first index in the hierarchy system so Alabama only not (Alabama,some shitty state)
            srr[str(cs.index[i][0])] += 1
    return srr[srr == max(srr)].index[0]
print(answer_five())
