# bbible

**bbible** is a simple and lightweight Bible verse lookup library for Python.

- 🔍 Fetch any verse or range by book, chapter, and verse
- 📚 Supports multiple versions (currently: NKJV, KJV)
- ✨ Returns reader-friendly formatted results

## Example

```python
import bbible

print(bbible.get_books())
print(bbible.get_versions())
print(bbible.get_verse("genesis", 1, 1))
print(bbible.get_verse("genesis", 1, (1, 3)))
```
