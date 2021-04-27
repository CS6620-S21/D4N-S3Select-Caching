import sys
import pyarrow.parquet as pq
parquet_file = pq.ParquetFile(sys.argv[1])
print (parquet_file.metadata)
print (parquet_file.schema)
x = parquet_file.read()
print (x.column(0))
print (x.column(0)[122])