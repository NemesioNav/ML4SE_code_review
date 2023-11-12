class InvertedIndex:
    def __init__(self):
        self.index = {}

    def add_document(self, doc_id, text):
        words = text.split()
        for word in set(words):  # Using a set to avoid duplicate entries for the same word in a document
            if word in self.index:
                self.index[word].append(doc_id)
            else:
                self.index[word] = [doc_id]

    def search(self, query):
        if query in self.index:
            return self.index[query]
        else:
            return []

# Example Usage:
if __name__ == "__main__":
    inverted_index = InvertedIndex()

    # Adding documents to the inverted index
    inverted_index.add_document(1, "Python is a powerful programming language")
    inverted_index.add_document(2, "Inverted index is used in information retrieval")
    inverted_index.add_document(3, "Python code can be written in an efficient way")

    # Searching for terms in the inverted index
    search_result_python = inverted_index.search("Python")
    search_result_index = inverted_index.search("index")
    search_result_java = inverted_index.search("Java")

    # Displaying search results
    print("Documents containing 'Python':", search_result_python)
    print("Documents containing 'index':", search_result_index)
    print("Documents containing 'Java':", search_result_java)
