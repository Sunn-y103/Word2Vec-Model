import gensim
import pandas as pd

# Load dataset
df = pd.read_json(
    r"C:\Users\sunny\Documents\GENSIM_MODEL\reviews_Sports_and_Outdoors_5.json\Sports_and_Outdoors_5.json",
    lines=True
)

print("Data loaded successfully!")
print(df.head())  # show first few rows

# Preprocess reviews
review_text = df.reviewText.apply(gensim.utils.simple_preprocess)
print("Text preprocessing done!")
print(review_text.head())

# Train Word2Vec model
model = gensim.models.Word2Vec(
    sentences=review_text,
    window=10,
    min_count=2
)

print("Model training completed!")

model.save("word2vec_model.model")

