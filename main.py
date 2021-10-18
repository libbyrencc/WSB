API_KEY = "PKNOUG6TB6QUGR3TMKV4"
SECRET_KEY = "674cgs9ZbPsAUKBQkHexppv8g5VTfoF3a3j22eLy"

import datetime
import time

import alpaca_trade_api as tradeapi
import numpy as np
import pandas as pd

#pd.options.display.max_rows = 999
#pd.set_option('display.max_columns', None)

#from datetime import datetime
from datetime import timedelta

from pytz import timezone

tz = timezone('EST')

api = tradeapi.REST(API_KEY,
                    SECRET_KEY,
                    'https://paper-api.alpaca.markets')