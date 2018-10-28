#!/usr/bin/env LC_ALL=en_US.UTF-8 /usr/local/bin/python3
import numpy as np
import pandas as pd
import matplotlib as ptl
import json

filename = "../data/ads/advertisers_you've_interacted_with.json"
with open(filename) as datafile:
    data = json.load(datafile)
history_df = pd.DataFrame(data["history"])
print(history_df.describe())
