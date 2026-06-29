from pathlib import Path
import pandas as pd
import numpy as np

# 原始 ChatGPT 大文件路径
INPUT_FILE = Path("data_backup/chatgpt_reviews.csv")

# 抽样后输出路径
OUTPUT_FILE = Path("data/chatgpt_reviews_sample_50000.csv")

# 抽样数量
SAMPLE_SIZE = 50000

# 每次读取多少行，服务器内存足够的话可以调大
CHUNK_SIZE = 100000

# 随机种子，保证每次抽样结果可复现
RANDOM_SEED = 42


def count_rows(csv_path: Path) -> int:
    """分块统计 CSV 总行数，不一次性读入内存。"""
    total = 0
    print("开始统计原始数据行数...")

    for i, chunk in enumerate(
        pd.read_csv(csv_path, chunksize=CHUNK_SIZE, low_memory=False)
    ):
        total += len(chunk)
        print(f"已统计第 {i + 1} 个数据块，累计 {total} 行")

    return total


def sample_csv(csv_path: Path, output_path: Path, sample_size: int) -> None:
    """从大 CSV 中随机抽样 sample_size 行。"""
    if not csv_path.exists():
        raise FileNotFoundError(f"找不到原始文件: {csv_path}")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    total_rows = count_rows(csv_path)

    print(f"\n原始数据总行数: {total_rows}")

    if total_rows <= sample_size:
        print("原始数据行数少于或等于抽样数量，将直接保存全部数据。")
        df = pd.read_csv(csv_path, low_memory=False)
        df.to_csv(output_path, index=False, encoding="utf-8-sig")
        print(f"已保存到: {output_path}")
        print(f"输出规模: {df.shape}")
        return

    rng = np.random.default_rng(RANDOM_SEED)

    # 在全部行号中随机选择 50000 个行号
    sample_indices = set(rng.choice(total_rows, size=sample_size, replace=False))

    print(f"\n已生成 {sample_size} 个随机抽样行号，开始第二遍读取并抽取数据...")

    sampled_chunks = []
    start_idx = 0

    for i, chunk in enumerate(
        pd.read_csv(csv_path, chunksize=CHUNK_SIZE, low_memory=False)
    ):
        end_idx = start_idx + len(chunk)

        # 当前 chunk 覆盖的全局行号范围：[start_idx, end_idx)
        local_indices = [
            idx - start_idx for idx in sample_indices
            if start_idx <= idx < end_idx
        ]

        if local_indices:
            sampled_chunks.append(chunk.iloc[local_indices])

        current_sampled = sum(len(x) for x in sampled_chunks)
        print(
            f"已处理第 {i + 1} 个数据块，"
            f"当前抽到 {current_sampled} / {sample_size} 行"
        )

        start_idx = end_idx

    sampled_df = pd.concat(sampled_chunks, ignore_index=True)

    # 打乱顺序，避免样本仍按原始文件时间/顺序排列
    sampled_df = sampled_df.sample(frac=1, random_state=RANDOM_SEED).reset_index(drop=True)

    sampled_df.to_csv(output_path, index=False, encoding="utf-8-sig")

    print("\n抽样完成！")
    print(f"输出文件: {output_path}")
    print(f"输出规模: {sampled_df.shape}")
    print("字段列表:")
    print(list(sampled_df.columns))


if __name__ == "__main__":
    sample_csv(INPUT_FILE, OUTPUT_FILE, SAMPLE_SIZE)
