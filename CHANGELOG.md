# Changelog

All notable changes to this project will be documented in this file.

---

## [0.2.0] - 2025-07-03

### Added
- 🧠 `.topic(query)` — AI-powered semantic search for relevant Bible verses by concept or theme
- Embedding support for `nkjv` and `kjv` via `sentence-transformers`
- Support for `top_k` and multiple versions in semantic search
- Clean formatting of semantic results with proper verse references

### Changed
- Project description and README updated to reflect new capabilities
- `setup.py` `description` field improved to include AI functionality

---

## [0.1.0] - 2025-06-17

### Added
- 📖 `.get_verse()` — Lookup a single verse or a range
- 📚 `.get_books()` — List of all 66 Bible books
- 🔄 `.get_versions()` — Detects and lists available versions
- Support for multiple versions (KJV and NKJV via JSON files)
