import gensim
# Load the saved model
loaded_model = gensim.models.Word2Vec.load("word2vec_model.model")
print("Model loaded successfully!")

# Test model
print(loaded_model.wv.most_similar("good", topn=5))

print(loaded_model.wv.most_similar("slow", topn=5))
