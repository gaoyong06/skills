#!/usr/bin/env python3
"""按固定权重给内容选题排序。输入和输出均为 JSON。"""

import json
import sys
from pathlib import Path


WEIGHTS = {
    "pain": 0.30,
    "frequency": 0.25,
    "product_fit": 0.25,
    "evidence": 0.10,
    "shareability": 0.10,
}


def score_topic(topic: dict) -> float:
    """计算单个选题的加权分数，并限制每个维度为 0 到 5。"""
    total = 0.0
    for field, weight in WEIGHTS.items():
        value = topic.get(field, 0)
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise ValueError(f"Field '{field}' must be a number")
        if not 0 <= value <= 5:
            raise ValueError(f"Field '{field}' must be between 0 and 5")
        total += value * weight
    return round(total, 2)


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: score_topics.py <topics.json>", file=sys.stderr)
        return 2

    input_path = Path(sys.argv[1])
    try:
        topics = json.loads(input_path.read_text(encoding="utf-8"))
        if not isinstance(topics, list):
            raise ValueError("Input must be a JSON array")
        ranked = []
        for index, topic in enumerate(topics):
            if not isinstance(topic, dict):
                raise ValueError(f"Topic at index {index} must be an object")
            item = dict(topic)
            item["score"] = score_topic(item)
            ranked.append(item)
        ranked.sort(key=lambda item: item["score"], reverse=True)
    except (OSError, json.JSONDecodeError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    json.dump(ranked, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
