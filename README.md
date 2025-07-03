# bbible

**bbible** is a Python library for exploring the Bible through both direct verse lookup and AI-powered semantic search.

> 🙏 Find what you’re looking for — whether it’s by reference or meaning.

---

## 🔥 Why bbible?

- 🧠 **Semantic topic search**: Find verses by concept, not just keywords.  
  _e.g., `.topic("grace")` returns verses about grace, trust, and forgiveness._
- 🔍 **Verse-level lookup**: Fetch specific verses or ranges by book, chapter, and verse.
- 📚 **Multi-version support**: Works with multiple translations (`nkjv`, `kjv`, more coming).
- 💬 **Readable output**: Cleanly formatted and suitable for quoting or presentation.

---

## 🚀 Quick Example

```python
import bbible

# Get a verse or passage
print(bbible.get_verse("john", 3, 16))
print(bbible.get_verse("psalms", 23, (1, 6)))

# Semantic search by topic
print(bbible.topic("peace", top_k=3))
print(bbible.topic("trust in God", version="kjv", top_k=5))
