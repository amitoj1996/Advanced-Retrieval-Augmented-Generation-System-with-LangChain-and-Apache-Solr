import os
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.retrievers import BaseRetriever
import pysolr

# Set up OpenAI API key
openai_api_key = os.getenv('OPENAI_API_KEY')

# Define Solr Retriever
class SolrRetriever(BaseRetriever):
    def __init__(self, solr_url, top_k=5):
        self.solr = pysolr.Solr(solr_url, timeout=10)
        self.top_k = top_k

    def get_relevant_documents(self, query):
        params = {
            'defType': 'edismax',
            'qf': 'content_txt',
            'fl': 'content_txt',
            'rows': self.top_k
        }
        results = self.solr.search(query, **params)
        return [result['content_txt'] for result in results]

# Initialize LLM
llm = OpenAI(model_name='text-davinci-003', openai_api_key=openai_api_key)

# Define Prompt Template
prompt_template = PromptTemplate(
    input_variables=['context', 'question'],
    template="""
You are an expert assistant. Use the following context to answer the question.

Context:
{context}

Question:
{question}

Answer:"""
)

# Define the main function to answer questions
def answer_question(question):
    # Initialize retriever
    retriever = SolrRetriever('http://localhost:8983/solr/rag_system')

    # Retrieve relevant documents
    context_documents = retriever.get_relevant_documents(question)
    context = ' '.join(context_documents)

    # Initialize LLM Chain
    chain = LLMChain(llm=llm, prompt=prompt_template)

    # Generate answer
    answer = chain.run(context=context, question=question)
    return answer.strip()
