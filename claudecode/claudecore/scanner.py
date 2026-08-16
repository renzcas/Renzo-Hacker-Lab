import os, math, re

def compute_entropy(text):
    freq = {}
    for c in text:
        freq[c] = freq.get(c, 0) + 1
    total = len(text)
    return -sum((count/total) * math.log2(count/total) for count in freq.values())

def scan_repo(root="."):
    results = []
    for dirpath, _, files in os.walk(root):
        for f in files:
            if f.endswith(".py"):
                path = os.path.join(dirpath, f)
                with open(path, "r", encoding="utf-8") as fh:
                    content = fh.read()
                entropy = compute_entropy(content)
                weird = re.findall(r"[^\w\s]", content)
                score = entropy + len(weird)
                results.append({"path": path, "entropy": entropy, "weird": weird, "score": score})
    return results
