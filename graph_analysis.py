"""課題3：所属ごとの円グラフを作成し、画像として保存する。"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

# 日本語表示用（Windows）
plt.rcParams["font.family"] = ["Yu Gothic", "Meiryo", "MS Gothic"]
plt.rcParams["axes.unicode_minus"] = False

BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "課題3.csv"


def main() -> None:
    df = pd.read_csv(CSV_PATH)

    # 所属ごとの参加者数
    counts = df["所属"].value_counts()

    fig, ax = plt.subplots(figsize=(8, 8))
    wedges, texts, autotexts = ax.pie(
        counts,
        labels=counts.index,  # 各セクションに所属名
        autopct="%1.1f%%",  # 各セクションにパーセンテージ
        startangle=90,
        counterclock=False,
        pctdistance=0.6,
        explode=[0.02] * len(counts),
    )
    for text in texts:
        text.set_fontsize(12)
    for autotext in autotexts:
        autotext.set_fontsize(11)
        autotext.set_color("white")
        autotext.set_fontweight("bold")

    ax.set_title("所属ごとの参加者数（割合）", fontsize=16, pad=16)
    ax.legend(
        wedges,
        [f"{name}：{count}人" for name, count in counts.items()],
        title="所属（人数）",
        loc="center left",
        bbox_to_anchor=(1.0, 0.5),
    )

    output_path = BASE_DIR / "pie_chart.png"
    fig.tight_layout()
    fig.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"保存完了: {output_path.name}")
    average_scores = df.groupby("所属")["スコア"].mean()
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(average_scores.index, average_scores.values)
    ax.set_title("所属ごとの平均スコア")
    ax.set_xlabel("所属")
    ax.set_ylabel("平均スコア")
    bar_output_path = BASE_DIR / "bar_chart.png"
    fig.savefig(bar_output_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    all_scores = df["スコア"]
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.hist(all_scores, bins=5)
    ax.set_title("全参加者のスコア分布")
    ax.set_xlabel("スコア")
    ax.set_ylabel("人数")
    histogram_output_path = BASE_DIR / "histogram.png"
    fig.savefig(histogram_output_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
if __name__ == "__main__":
    main()

