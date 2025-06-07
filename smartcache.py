from document_store import DocumentStore
from inverted_index import InvertIndex
from deduplicator import Deduplicator
from search_ranker import SearchRanker
from history_manager import HistoryManager
from suggestion_engine import SuggestionEngine
from utils import Util


class SmartCache:
    def __init__(self):
        self.document = DocumentStore()
        self.index = InvertIndex()
        self.deduplicator = Deduplicator()
        self.ranker = SearchRanker()
        self.history = HistoryManager()
        self.suggester = SuggestionEngine()
        self.util = Util()

    def add_doc(self, doc):
        if self.deduplicator.is_duplicate(doc):
            print("Similar document detected")
            return None
        self.deduplicator.add(doc)
        doc_id = self.document.add_documents(doc)
        self.index.add_document(doc_id, doc)

    def search_doc(self, keyword, k=3):
        # Search document with this keyword
        matching_doc_ids = self.index.lookup(keyword)

        if not matching_doc_ids:
            suggestions = self.suggester.suggest(
                queries=[query for time, query in self.history.search_queue],
                current_query=keyword,
            )
            return "No matching doc found"

        # Get the matching documents
        matching_docs = {}
        for i in matching_doc_ids:
            matching_docs[i] = self.document.get_document(doc_id=i)

        # Log the search
        self.history.log_search(keyword)

        # Rank top-k elements
        top_k_ids = self.ranker.rank(matching_docs, keyword, k)

        top_documents = []
        for doc_id in top_k_ids:
            top_documents.append(self.document.get_document(doc_id))

        return top_documents

    def view_doc(self, doc_id):
        return self.document.get_document(doc_id)

    def list_doc(self):
        return self.document.list_documents()

    def search_by_timestamp(self, timestamp):
        return self.util.binary_search_doc(self.document.timestamps, timestamp)

    def recent_searches(self, n):
        return self.history.get_recent(n)

    def undo_last_filter(self):
        return self.history.undo_filter()