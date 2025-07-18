import pandas as pd
import sys

if len(sys.argv) != 4:
    print("用法: python remove_gene.py 输入文件名 要删除的gene值 输出文件名")
    print("示例: python remove_gene.py temp.csv C4 all_gene_location.csv")
    sys.exit(1)

input_file = sys.argv[1]
gene_to_remove = sys.argv[2]
output_file = sys.argv[3]

df = pd.read_csv(input_file)

if 'gene' not in df.columns:
    print("错误: 输入文件中没有 'gene' 列，请确认文件结构。")
    sys.exit(1)

df_filtered = df[df['gene'] != gene_to_remove]

df_filtered.to_csv(output_file, index=False)

print(f"已从文件中删除所有 {gene_to_remove} 行，并保存为 {output_file}")