import Levenshtein


class SuggestionEngine:
    def __init__(self):
        pass

    def suggest(self, queries, current_query):
        # Sliding window / two pointers to find substring overlaps
        # Common prefix, suffix, or words in common
        current_query_len = len(current_query)
        threshold = max(1, current_query_len // 3)  # adaptive threshold
        query_suggestion = []
        seen = set()
        for query in queries:
            min_distance = float("inf")
            if len(query) < current_query_len:
                distance = Levenshtein.distance(query, current_query)
                if distance <= threshold:
                    min_distance = distance

            else:
                # Slide window over query
                for i in range(len(query) - current_query_len + 1):
                    sub_word = query[i : i + current_query_len]
                    distance = Levenshtein.distance(current_query, sub_word)
                    if distance <= threshold and distance < min_distance:
                        min_distance = distance

            if min_distance <= threshold and query not in seen:
                query_suggestion.append((query, min_distance))
                seen.add(query)

        # sort by closest match
        query_suggestion.sort(key=lambda x: x[1])

        return [query for query, distance in query_suggestion]

    # To implement helper functions come after learning Dynamic Programming (DP)
    # optional helper function
    def longest_common_substring(self):
        # Implement later
        pass

    # optional helper function two
    def shared_words(slef, current_query, past_query):
        # implement later
        pass
