import heapq

class SearchRanker:

    def __init__(self):
        pass

    def score(self, text, keyword):
        # count frequency of keyword in given text
        text = text.lower().strip()
        keyword = keyword.lower().strip()
        return text.split().count(keyword)

    def rank(self, documents:dict, keyword, k):
        # use a heap to return top-k doc ID by score
        heap = []
        for doc_id, text in documents.items():
            # get score
            score = self.score(text, keyword)
            # push (-score, doc_id) to heap to get max-heap behavior
            heap.append((-score,doc_id))
        heapq.heapify(heap)

        top_documents = []
        # Pop top-k and return sorted list of doc_ids
        for i in range(min(k, len(heap))):
            scores, document_id = heapq.heappop(heap)
            top_documents.append(document_id)

        return top_documents
        
