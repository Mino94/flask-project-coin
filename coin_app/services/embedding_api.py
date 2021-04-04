from embedding_as_service_client import EmbeddingClient
from typing import List

en = EmbeddingClient(host='54.180.124.154', port=8989)

def get_embeddings(text_list: List[str]) -> List[List[float]]:
    vecs = en.encode(texts=text_list)

    return vecs
