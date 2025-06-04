import tabulate
import datetime as dt
class DocumentStore:
    def __init__(self):
        self.document = {}
        self.document_id = -1
        self.timestamps = {}

    # methods
    def add_documents(self, text):
        """
        Adds a new documents and returns its id
        """
        self.document_id += 1
        self.document[self.document_id] = text
        self.timestamps[self.document_id] = dt.datetime.now()
        return self.document_id

    def get_document(self, doc_id):
        """
        Returns the document with that id
        """
        # return f"{self.document[doc_id]}"
        return tabulate.tabulate(
            [[doc_id, self.document[doc_id]]],
            headers=["document_id", "document"],
            tablefmt="grid",
        )

    def list_documents(self):
        """
        Returns all the stored documents or its metadata
        """
        datas = tabulate.tabulate(
            self.document.items(), headers=["document_id", "document"], tablefmt="grid"
        )
        print(datas)

    def get_all_documents(self):
        return self.document