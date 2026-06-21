from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

embedding = OpenAIEmbeddings(
    model="text-embedding-3-large",
    dimensions=300
)

documents = [
    "ms dhoni is the greatest indian cricketer of all time. he is known for his captaincy and his match finishing ability. he is the only captain in history to win all ICC tournaments.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "Jasprit Bumrah is an Indian cricketer known for his fast bowling and unorthodox bowling action."
]

query = "tell me about ms dhoni"

doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

similarity_scores = cosine_similarity(
    [query_embedding],
    doc_embeddings
)[0]

index, best_score = sorted(
    list(enumerate(similarity_scores)),
    key=lambda x: x[1]
)[-1]

print(documents[index])
print("Similarity score:", best_score)