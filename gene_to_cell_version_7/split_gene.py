import pandas as pd
import sys
import os

if len(sys.argv) != 3:
    print("用法: python split_gene.py 输入文件名 输出目录")
    sys.exit(1)

input_file = sys.argv[1]
output_dir = sys.argv[2]

df = pd.read_csv(input_file)

if 'gene' not in df.columns:
    print("错误: 输入文件中没有 'gene' 列，请确认文件结构。")
    sys.exit(1)

os.makedirs(output_dir, exist_ok=True)

for gene_value, group in df.groupby('gene'):
    output_filename = os.path.join(output_dir, f"{gene_value}.csv")
    group.to_csv(output_filename, index=False)
    print(f"已保存 {gene_value} 到 {output_filename}")

print(f"所有文件已保存到目录: {output_dir}")