from dotenv import load_dotenv
import os
import tiktoken
import openai

load_dotenv()  # Load environment variables from .env file


class EmbeddingGenerator:
    def __init__(self):
        # Load API key from environment variables
        openai_api_key = os.getenv("OPENAI_API_KEY")
        if not openai_api_key:
            raise ValueError("OPENAI_API_KEY environment variable not set")

    def chunk_text_by_tokens(self, text, chunk_size, encoding_name="cl100k_base"):
        """
        Splits the text into chunks based on the number of tokens.
        """
        encoding = tiktoken.get_encoding(encoding_name)
        tokens = encoding.encode(text)
        return [encoding.decode(tokens[i:i + chunk_size]) for i in range(0, len(tokens), chunk_size)]

    def generate_embeddings(self, chunks):
        """
        Generates embeddings for each chunk and returns a list of embeddings.
        """
        embeddings = []
        for chunk in chunks:
            response = openai.embeddings.create(
                input=chunk,
                model="text-embedding-ada-002"
            )
            embeddings.append(response.data[0].embedding)
        return embeddings

    def process_text(self, text, chunk_size=1000):
        """
        Splits the text it into chunks, and generates the embeddings.
        """
        chunks = self.chunk_text_by_tokens(text, chunk_size)
        embeddings = self.generate_embeddings(chunks)
        return chunks, embeddings
