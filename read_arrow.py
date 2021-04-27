import sys
import pandas
import pyarrow.feather as feather
feather_file = sys.argv[1]
read_df = feather.read_feather(feather_file)