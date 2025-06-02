from document_store import DocumentStore
from inverted_index import InvertIndex
from deduplicator import Deduplicator

store_1 = DocumentStore()
# pass the document to InvertedIndex method for indexing the keywords
invert = InvertIndex()

# pass the document to Deduplicator to check if documents already exists
deduper = Deduplicator()

document_one = "Hello World"
document_two = "New World"

# Check if near-duplicate document exists
if deduper.is_duplicate(document_one) == False:
    doc_id_one = store_1.add_documents(document_one)
    deduper.add(document_one)
    print("document is added")
    invert.add_document(doc_id_one, store_1.get_document(doc_id_one))

else:
    print("Duplicate found")

if deduper.is_duplicate(document_two) == False:
    doc_id_two = store_1.add_documents(document_two)
    deduper.add(document_two)
    print("document is added")
    invert.add_document(doc_id_two, store_1.get_document(doc_id_two))
else:
    print("Duplicate found")

document_id_list = invert.lookup("world")
for i in document_id_list:
    print(store_1.get_document(i))
