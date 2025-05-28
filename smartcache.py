from document_store import DocumentStore

store_1 = DocumentStore()
doc_id = store_1.add_documents("Hello World")
doc_id = store_1.add_documents("New World")
store_1.list_documents()
documents = store_1.get_document(1)
print(documents)
