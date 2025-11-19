import json

ttl_path = "kg.ttl"          # your TTL file
json_path = "kg-data.json"   # output file

def clean_term(t):
    t = t.strip()
    # strip angle brackets if any
    if t.startswith("<") and t.endswith(">"):
        t = t[1:-1]
    # drop leading urn:
    if t.startswith("urn:"):
        t = t[4:]
    return t

def short_label(u):
    # last part after / or #
    if "/" in u:
        u = u.rsplit("/", 1)[-1]
    if "#" in u:
        u = u.rsplit("#", 1)[-1]
    return u.replace("_", " ")

nodes = {}
edges = []

with open(ttl_path, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if not line.endswith("."):
            continue

        parts = line[:-1].strip().split()
        if len(parts) < 3:
            continue

        s, p, o = parts[0], parts[1], " ".join(parts[2:])
        s_clean = clean_term(s)
        p_clean = clean_term(p)
        o_clean = clean_term(o)

        for term in (s_clean, o_clean):
            if term not in nodes:
                nodes[term] = {
                    "id": term,
                    "label": short_label(term)
                }

        edges.append({
            "from": s_clean,
            "to": o_clean,
            "label": short_label(p_clean)
        })

data = {
    "nodes": list(nodes.values()),
    "edges": edges
}

with open(json_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Wrote {len(nodes)} nodes and {len(edges)} edges to {json_path}")
