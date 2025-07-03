# bbible/__init__.py

import json
import os

_LOADED_VERSIONS = {}

def load_version(version):
    version = version.lower()
    if version in _LOADED_VERSIONS:
        return _LOADED_VERSIONS[version]

    path = os.path.join(os.path.dirname(__file__), "data", f"{version}.json")
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
            _LOADED_VERSIONS[version] = data
            return data
    except FileNotFoundError:
        return None

def get_verse(book, chapter, verse, version="nkjv", tag=True):
    version = version.lower()
    book = book.lower()
    chapter = str(chapter)

    data = load_version(version)
    if not data:
        return "Version not found"
    if book not in data:
        return "Book not found"
    if chapter not in data[book]:
        return "Chapter not found"

    verses = data[book][chapter]

    if isinstance(verse, int):
        v = str(verse)
        if v not in verses:
            return "Verse not found"
        body = f"        {v} {verses[v]}"
        ref = f"{book.capitalize()} {chapter}:{v} {version.upper()}"
        return f"{body}\n\n{ref}\n—from bbible by Biyi✨" if tag else f"{body}\n\n{ref}"

    if isinstance(verse, (tuple, list)) and len(verse) == 2:
        start, end = verse
        lines = [
            f"        {v} {verses[str(v)]}"
            for v in range(start, end + 1)
            if str(v) in verses
        ]
        if not lines:
            return "No verses found in range"
        body = "\n".join(lines)
        ref = f"{book.capitalize()} {chapter}:{start}–{end} {version.upper()}"
        return f"{body}\n\n{ref}\n—from bbible by Biyi✨" if tag else f"{body}\n\n{ref}"

    return "Invalid verse input"

    version = version.lower()
    book = book.lower()
    chapter = str(chapter)

    data = load_version(version)
    if not data:
        return "Version not found"
    if book not in data:
        return "Book not found"
    if chapter not in data[book]:
        return "Chapter not found"

    verses = data[book][chapter]

    if isinstance(verse, int):
        v = str(verse)
        if v not in verses:
            return "Verse not found"
        body = f"        {v} {verses[v]}"
        ref = f"{book.capitalize()} {chapter}:{v}"
        return f"{body}\n\n{ref}\n—from bbible by Biyi✨" if tag else f"{body}\n\n{ref}"

    if isinstance(verse, (tuple, list)) and len(verse) == 2:
        start, end = verse
        lines = [
            f"        {v} {verses[str(v)]}"
            for v in range(start, end + 1)
            if str(v) in verses
        ]
        if not lines:
            return "No verses found in range"
        body = "\n".join(lines)
        ref = f"{book.capitalize()} {chapter}:{start}–{end}"
        return f"{body}\n\n{ref}\n—from bbible by Biyi✨" if tag else f"{body}\n\n{ref}"

    return "Invalid verse input"

BOOKS = [
    "Genesis", "Exodus", "Leviticus", "Numbers", "Deuteronomy",
    "Joshua", "Judges", "Ruth", "1 Samuel", "2 Samuel",
    "1 Kings", "2 Kings", "1 Chronicles", "2 Chronicles",
    "Ezra", "Nehemiah", "Esther", "Job", "Psalms", "Proverbs",
    "Ecclesiastes", "Song of Solomon", "Isaiah", "Jeremiah", "Lamentations",
    "Ezekiel", "Daniel", "Hosea", "Joel", "Amos", "Obadiah", "Jonah", "Micah",
    "Nahum", "Habakkuk", "Zephaniah", "Haggai", "Zechariah", "Malachi",
    "Matthew", "Mark", "Luke", "John", "Acts", "Romans", "1 Corinthians",
    "2 Corinthians", "Galatians", "Ephesians", "Philippians", "Colossians",
    "1 Thessalonians", "2 Thessalonians", "1 Timothy", "2 Timothy", "Titus",
    "Philemon", "Hebrews", "James", "1 Peter", "2 Peter", "1 John", "2 John",
    "3 John", "Jude", "Revelation"
]

def get_books():
    return BOOKS

def get_versions():
    data_dir = os.path.join(os.path.dirname(__file__), "data")
    versions = []
    for filename in os.listdir(data_dir):
        if filename.endswith(".json"):
            versions.append(filename.replace(".json", ""))
    return sorted(versions)

def topic(query, version="nkjv", top_k=5, tag=True):
    import pickle
    import numpy as np
    from sentence_transformers import SentenceTransformer
    from sklearn.metrics.pairwise import cosine_similarity

    version = version.lower()
    embed_path = os.path.join(os.path.dirname(__file__), "data", f"embeddings_{version}.pkl")
    if not os.path.exists(embed_path):
        return f"Embeddings not found for version '{version}'. Please generate them first."

    # Load embeddings
    with open(embed_path, "rb") as f:
        verse_embeddings = pickle.load(f)

    # Prepare data
    refs, texts, vectors = zip(*verse_embeddings)
    vectors = np.array(vectors)

    # Embed the query
    model = SentenceTransformer("all-MiniLM-L6-v2")
    query_vec = model.encode([query])

    # Compute cosine similarity
    sims = cosine_similarity(query_vec, vectors)[0]
    top_indices = np.argsort(sims)[-top_k:][::-1]

    # Format results
    results = []
    for i in top_indices:
        results.append(f"        {texts[i]}\n{refs[i]} {version.upper()}")
    
    return "\n\n".join(results) + ("\n\n—from bbible by Biyi✨" if tag else "")