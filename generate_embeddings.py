import json
import pickle
from tqdm import tqdm
from sentence_transformers import SentenceTransformer

# Load your Bible version
with open("bbible/data/kjv.json", "r", encoding="utf-8") as f:
    bible_data = json.load(f)

# Prepare verses for embedding
verses = []
for book, chapters in bible_data.items():
    for chapter, verse_dict in chapters.items():
        for verse, text in verse_dict.items():
            ref = f"{book} {chapter}:{verse}"
            verses.append((ref, text.strip()))

# Load transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Generate and store embeddings
embeddings = [(ref, text, model.encode(text)) for ref, text in tqdm(verses)]

# Save to file
with open("bbible/data/embeddings_kjv.pkl", "wb") as f:
    pickle.dump(embeddings, f)

print("✅ Embeddings saved to 'data/embeddings_kjv.pkl'")


# import bbible
# print(bbible.topic("fear", version="nkjv", top_k=50))