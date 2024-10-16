import os
import pysolr

def index_documents(solr_url, docs_dir):
    # Connect to Solr
    solr = pysolr.Solr(solr_url, always_commit=True, timeout=10)

    documents = []
    for filename in os.listdir(docs_dir):
        if filename.endswith('.txt'):
            with open(os.path.join(docs_dir, filename), 'r', encoding='utf-8') as file:
                content = file.read()
                doc = {
                    'id': filename,
                    'content_txt': content
                }
                documents.append(doc)
                print(f"Loaded {filename} for indexing.")

    # Index documents in batches
    solr.add(documents)
    print(f"Indexed {len(documents)} documents.")

if __name__ == "__main__":
    solr_core_url = 'http://localhost:8983/solr/rag_system'
    processed_docs_dir = 'data/processed/'
    index_documents(solr_core_url, processed_docs_dir)
