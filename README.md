# 📖 bbible

**bbible** is a lightweight and extensible Python library for Bible verse access and exploration — combining classic reference lookups with AI-powered semantic topic search.

It helps you retrieve verses by **book/chapter/verse**, or discover scriptures related to **concepts like hope, peace, or grace**, using transformer embeddings.

---

## ✨ Features

- 🔍 **Get verses by reference** (single or range)
- 🧠 **Semantic topic search** – find verses that match meaning, not just keywords
- 📚 **Multi-version support** – supports `nkjv`, `kjv`, and others via JSON
- 💬 **Formatted output** – reader-friendly for display or printing
- 📦 **Local-first design** – no API calls, 100% offline

---

## 📦 Installation

```bash
pip install bbible
```

**To enable semantic search**

```python
pip install sentence-transformers tqdm
```

## 🧪 Basic Usage

### 🔹 Get books and versions

```python
import bbible

print(bbible.get_books())      # List all 66 Bible books
print(bbible.get_versions())   # Available versions (e.g. nkjv, kjv)
```

### 🔹 Get a verse or range
```python
print(bbible.get_verse("john", 3, 16))

print(bbible.get_verse("psalms", 23, (1, 6), version="kjv"))
```

## 🔥 Semantic Topic Search
Use `.topic()` to explore verses that relate to a theme or concept, not just a keyword.
```python
print(bbible.topic("hope"))

print(bbible.topic("faith in hard times", version="kjv", top_k=5))
```

## 🧠 How it works
- Verse texts are converted into embeddings using sentence-transformers
- Your query is embedded and compared to all verses
- Verses are ranked by cosine similarity to your concept

```text
Input: "grace"
→ Matches: forgiveness, love, undeserved mercy, etc.
```
✅ Works per version (e.g., NKJV, KJV) for theological clarity.


## 🔍 Bible Structure
All supported versions use the same format:

```json
{
  "genesis": {
    "1": {
      "1": "In the beginning God created...",
      "2": "And the earth was without form..."
    },
    "2": {
      "1": "Thus the heavens and the earth..."
    }
  },
  ...
}
```


## 📘 Sample Output
```python
print(bbible.topic("peace", version="nkjv", top_k=2))
```
```vbnet
        You will keep him in perfect peace, whose mind is stayed on You, because he trusts in You.
Isaiah 26:3 NKJV

        Peace I leave with you, My peace I give to you; not as the world gives do I give to you.
John 14:27 NKJV

—from bbible by Biyi✨
```


## 🧰 API Reference

### 🔹 `get_books() → list`
Returns all 66 books of the Bible.

### 🔹 `get_versions() → list`
Returns a list of available Bible versions (based on loaded JSONs).

### 🔹 `get_verse(book, chapter, verse, version="nkjv")`
Returns a verse or range (tuple) formatted with or without attribution.

### 🔹 `topic(query, version="nkjv", top_k=5, tag=True)`
Performs semantic search. Returns verses most related to the query.

---

## 📄 License

MIT License © Biyi Adebayo  
Built with ❤️ and the Word.

## 🌐 Project Links

- 📦 [PyPI](https://pypi.org/project/bbible)
- 🛠 [GitHub](https://github.com/Biyi003/bbible)