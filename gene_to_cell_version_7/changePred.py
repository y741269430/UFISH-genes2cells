import pandas as pd
import sys

if len(sys.argv) != 3:
    print("用法: python changePred.py 输入文件名 输出文件名")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

df = pd.read_csv(input_file)

df['gene'] = 'C' + df['axis-0'].astype(str)

df['axis-0'] = 1

df = df[['axis-0', 'axis-1', 'axis-2', 'gene']]

df.to_csv(output_file, index=False)

print(f"文件已保存到 {output_file}")