import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download NLTK data files (if not already downloaded)
nltk.download('punkt')
nltk.download('stopwords')

def preprocess_document(text):
    # Tokenize the text
    words = word_tokenize(text)
    # Remove stop words and non-alphabetic characters
    words = [word.lower() for word in words if word.isalpha() and word.lower() not in stopwords.words('english')]
    # Rejoin words into a single string
    return ' '.join(words)

def preprocess_documents(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for filename in os.listdir(input_dir):
        if filename.endswith('.txt'):
            with open(os.path.join(input_dir, filename), 'r', encoding='utf-8') as file:
                text = file.read()
                cleaned_text = preprocess_document(text)
                with open(os.path.join(output_dir, filename), 'w', encoding='utf-8') as output_file:
                    output_file.write(cleaned_text)
            print(f"Processed {filename}")

if __name__ == "__main__":
    input_directory = 'data/raw/'
    output_directory = 'data/processed/'
    preprocess_documents(input_directory, output_directory)
