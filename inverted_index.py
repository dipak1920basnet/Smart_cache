import re


class InvertIndex:
    def __init__(self):
        self.index = {}

    def add_document(self, doc_id, text):
        """
        Tokenize and index the documents
        """

        # This functions can be removed later
        def remove_punctuation(doc):
            # remove punction with regex
            clean_text = re.sub(r"[^\w\s]", " ", doc)
            clean_text = clean_text.lower()
            return clean_text.split(" ")

        text = remove_punctuation(text)

        for word in text:
            # add word of doc as key and its id as value
            self.index.setdefault(word, set()).add(doc_id)

    def lookup(self, keyword):
        """
        Return the list of documents
        """
        # get the list of document id that has this keyword
        documet_id_list = self.index[keyword]
        """
        # list of documents with keyword
        document_list = []
        # for i in documet_id_list:
        #     document_list.append(smartcache.store_1.get_document(i))
        """
        return documet_id_list

    def print_index():
        """
        Print the current index for inspection
        """
        ...
        # Since this method is optional come back when needed
