from convert_to_text import convert_pdf_to_text
from convert_to_vector import EmbeddingGenerator
from upload_to_db import PineconeStore

if __name__ == '__main__':
    print("Converting PDF to text...\n")
    text = convert_pdf_to_text()
    print("Completed converting PDF to text.\n")

    print("Generating chunks and embeddings...\n")
    generator = EmbeddingGenerator()
    chunks, embedding = generator.process_text(text, chunk_size=800)
    print("Completed generating chunks and embeddings.\n")

    print("Saving vectors to Pinecone...\n")
    vector_store = PineconeStore()
    vector_store.save_vectors(
        embedding, {"id": "doc_1", "source": "../public/pdf/spec-book-0924.pdf"}, chunks)
    print("Completed saving vectors to Pinecone.")
