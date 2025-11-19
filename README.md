# 📘 KnowledgeGraph — Russia–Ukraine Conflict (Interactive KG Viewer)

This repository contains a manually constructed **Knowledge Graph (KG)** based on Reddit posts related to the Russia–Ukraine conflict.  
The KG is encoded in **RDF/Turtle** format and visualized through an **interactive web viewer** built using *vis-network* and hosted via **GitHub Pages**.

---

## 🌐 Interactive Knowledge Graph Viewer

Explore the knowledge graph interactively:

👉 **https://daksh26tiku.github.io/KnowledgeGraph/**

This viewer supports zooming, panning, dragging nodes, and inspecting relationships in real time.

---

## 📁 Repository Structure

```
KnowledgeGraph/
│
├── kg.ttl          # Knowledge Graph encoded in RDF/Turtle format
├── kg-data.json    # JSON representation auto-generated from kg.ttl
├── index.html      # Interactive viewer (vis-network)
├── ttl_to_json.py  # Script to convert .ttl → kg-data.json
└── README.md       # Documentation
```

---

## 📄 About the Knowledge Graph

The KG represents:

- **Entities** such as countries, leaders, organizations, locations, military hardware, and events.
- **Relations** such as `attacks`, `meets`, `supports`, `addresses`, and many more.
- Extracted manually from a curated dataset of ~250 Reddit posts.
- No NLP libraries (NER, spaCy, transformers, etc.) were used, per project constraints.

All entities and predicates use a unified namespace:

```ttl
@prefix ex: <https://daksh26tiku.github.io/KnowledgeGraph#> .
```

This ensures compatibility with web-based RDF tools.

---

## 🛠️ Generation Pipeline

1. The graph is authored manually in **Turtle (.ttl)**.
2. `ttl_to_json.py` converts RDF triples into a JSON structure suitable for `vis-network`.
3. GitHub Pages hosts:
   - `index.html` (interactive viewer)
   - `kg-data.json` (graph data)

To regenerate the JSON after editing the TTL file:

```bash
python ttl_to_json.py
```

This updates `kg-data.json` for the viewer.

---

## 🔍 Viewer Features

The viewer provides:

- ✔ Smooth pan and zoom  
- ✔ Hover tooltips on nodes & edges  
- ✔ Drag nodes to rearrange the layout  
- ✔ Force-directed layout  
- ✔ Fully client-side (no backend or server needed)

Built with the lightweight **vis-network** JavaScript library.

---

## 🚀 GitHub Pages Deployment

This repository is automatically deployed via **GitHub Pages**.

Live site:

```
https://daksh26tiku.github.io/KnowledgeGraph/
```

Deployment happens directly from the root of the `main` branch.  
Any change to `index.html` or `kg-data.json` updates the live site automatically.

---

## 📦 TTL → JSON Conversion

To convert the RDF file into the visualization-ready JSON:

```bash
python ttl_to_json.py
```

The script:

- Parses each RDF triple  
- Creates node objects  
- Creates edge objects with labeled predicates  
- Outputs a clean JSON file for the viewer

---

## 🤝 Contributing

Contributions are welcome!

You may:

- Improve entity categorization  
- Add new nodes/relations  
- Enhance the viewer UI (colors, filters, search)  
- Visualize clusters or categories  

Fork the repo and submit a pull request.

---

## 📜 License

Distributed under the **MIT License**.  
You are free to use, modify, and distribute this project.

---
