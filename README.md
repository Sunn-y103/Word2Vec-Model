# Word2Vec Model: Amazon Sports & Outdoors Reviews

[![Hugging Face Model](https://img.shields.io/badge/🤗%20Hugging%20Face-Model-blue)](https://huggingface.co/Sunny6727/Word2Vec_gensim_lib)

A Word2Vec model trained on a large corpus of Amazon product reviews from the **Sports & Outdoors** category. This project generates high-quality word embeddings that capture the semantic relationships between words specific to the language of sports equipment, outdoor gear, and customer feedback.

## 📁 Project Structure

```
Word2Vec-Model/
├── model.py            # Script to train the model
├── test.py             # Script to test and evaluate the model                           
├── README.md                         # This file
└── requirements.txt                  # Python dependencies
```

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Sunn-y103/Word2Vec-Model.git
   cd Word2Vec-Model
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

**Load the pre-trained model and use it:**
```python
import gensim

# Load the model
model = gensim.models.Word2Vec.load("models/word2vec_model.model")

# Find similar words
similar_words = model.wv.most_similar("hiking", topn=5)
print(similar_words)
# Output: [('backpacking', 0.78), ('camping', 0.75), ('trail', 0.72), ...]

# Get word vector
vector = model.wv['tent']

# Calculate similarity score
similarity = model.wv.similarity('running', 'training')
```

## 🧠 Model Details

- **Architecture:** Word2Vec (Skip-gram)
- **Vector Dimension:** 100
- **Window Size:** 10
- **Minimum Word Count:** 2
- **Training Data:** 296,337 Amazon reviews
- **Vocabulary Size:** ~20,000 words (est.)

## 📊 Training Data

The model was trained on the [Amazon Sports and Outdoors Reviews dataset](https://snap.stanford.edu/data/amazon/productGraph/categoryFiles/reviews_Sports_and_Outdoors_5.json.gz) from the Stanford Network Analysis Project (SNAP).

**Dataset Statistics:**
- **Reviews:** 296,337
- **Time Period:** Up to 2015
- **Columns:** 9 (including reviewText, overall rating, summary, etc.)

## 🛠️ Development

## Retrain the Model

If you want to retrain the model with different parameters:

```bash
python model.py
```

## Test the Model

Run the evaluation script to see example outputs:

```bash
python test.py
```

## 📋 Results

The model successfully learns semantic relationships specific to the sports domain:

**Similarity Examples:**
- `hiking` → backpacking, camping, trail, outdoors, gear
- `football` → soccer, basketball, sports, game, player
- `comfortable` → comfortable, great, nice, perfect, excellent

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License

This project is shared for research and educational purposes. The original data follows Amazon's terms of use.


---

**Related Links:**  
[🤗 Hugging Face Model Page](https://huggingface.co/Sunny6727/Word2Vec_gensim_lib) • 
[📊 Original Dataset](https://snap.stanford.edu/data/amazon/productGraph/categoryFiles/reviews_Sports_and_Outdoors_5.json.gz)

---
