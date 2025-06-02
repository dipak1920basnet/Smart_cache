# import hashlib
from simhash import Simhash

class Deduplicator:

    def __init__(self):
        self.fingerprints = set()

    def _hash(self, text):

        def clean_text(text):
            # write a function to clean text
            # hashlib.md5(text.encode()).hexdigest()
            # return Simhash(text)
            ...

        cleaned_text = clean_text(text)

        # write a function to produce hash 
        return Simhash(text)
    
    def is_duplicate(self, text):
        # returns true if hash exists in set
        # this threshold 6 was selected assuming it would work for all short to long text
        threshold = 6
        hash_value = self._hash(text)
        for i in self.fingerprints:
            if i.distance(hash_value) <= threshold:
                return True
        return False
        

    def add(self, text):
        produced_hash = self._hash(text)
        self.fingerprints.add(produced_hash)

    

    