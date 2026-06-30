# mood_analyzer.py
"""
Rule based mood analyzer for short text snippets.

This class starts with very simple logic:
  - Preprocess the text
  - Look for positive and negative words
  - Compute a numeric score
  - Convert that score into a mood label
"""

import re
from typing import List, Dict, Tuple, Optional

from dataset import POSITIVE_WORDS, NEGATIVE_WORDS

# Map emoji characters to plain tokens so they can be matched against word lists.
# Only emojis that appear in the dataset (or are clearly sentiment-bearing) are included.
# Tradeoff: a hardcoded map is brittle, but a full emoji library would be overkill here.
EMOJI_TOKEN_MAP: Dict[str, str] = {
    "😂": "emoji_joy",       # laughter / positive
    "😅": "emoji_sweat",     # nervous/mixed — intentionally left out of word lists
    "💀": "emoji_skull",     # "I'm dead" slang — negative in this dataset
}


class MoodAnalyzer:
    """
    A very simple, rule based mood classifier.
    """

    def __init__(
        self,
        positive_words: Optional[List[str]] = None,
        negative_words: Optional[List[str]] = None,
    ) -> None:
        # Use the default lists from dataset.py if none are provided.
        positive_words = positive_words if positive_words is not None else POSITIVE_WORDS
        negative_words = negative_words if negative_words is not None else NEGATIVE_WORDS

        # Store as sets for faster lookup.
        self.positive_words = set(w.lower() for w in positive_words)
        self.negative_words = set(w.lower() for w in negative_words)

    # ---------------------------------------------------------------------
    # Preprocessing
    # ---------------------------------------------------------------------

    def preprocess(self, text: str) -> List[str]:
        """
        Convert raw text into a list of tokens the model can work with.

        Steps (in order):
          1. Substitute known emojis with plain tokens ("💀" -> "emoji_skull")
             so downstream scoring can treat them as words.
             Tradeoff: hardcoded map covers only emojis in our dataset; a full
             emoji library would generalize better but adds a dependency.
          2. Lowercase everything.
          3. Strip punctuation via regex so "cap," matches "cap".
             Tradeoff: this also removes apostrophes, turning "I'm" into "im",
             but none of those fragments are in our word lists, so no harm done.
          4. Split and drop empty strings left by the substitutions.

        Intentionally skipped:
          - Repeated-character normalization ("soooo" -> "so"): zero instances
            in the current dataset, not worth the complexity.
          - Negation bigrams ("not_happy"): better handled in score_text where
            we have context about adjacent tokens.
        """
        # Step 1 — emoji substitution (before lowercasing, emojis are case-neutral)
        for emoji, token in EMOJI_TOKEN_MAP.items():
            text = text.replace(emoji, f" {token} ")

        # Step 2 — lowercase
        cleaned = text.strip().lower()

        # Step 3 — remove punctuation (keep word chars and whitespace only)
        cleaned = re.sub(r"[^\w\s]", " ", cleaned)

        # Step 4 — split; filter empty strings produced by multi-char substitutions
        tokens = [t for t in cleaned.split() if t]

        return tokens

    # ---------------------------------------------------------------------
    # Scoring logic
    # ---------------------------------------------------------------------

    def score_text(self, text: str) -> int:
        """
        Compute a numeric "mood score" for the given text.

        Positive words increase the score.
        Negative words decrease the score.

        TODO: You must choose AT LEAST ONE modeling improvement to implement.
        For example:
          - Handle simple negation such as "not happy" or "not bad"
          - Count how many times each word appears instead of just presence
          - Give some words higher weights than others (for example "hate" < "annoyed")
          - Treat emojis or slang (":)", "lol", "💀") as strong signals
        """
        # TODO: Implement this method.
        #   1. Call self.preprocess(text) to get tokens.
        #   2. Loop over the tokens.
        #   3. Increase the score for positive words, decrease for negative words.
        #   4. Return the total score.
        #
        # Hint: if you implement negation, you may want to look at pairs of tokens,
        # like ("not", "happy") or ("never", "fun").
        score = 0
        tokens = self.preprocess(text)

        NEGATORS = {"not", "never", "no", "cant", "dont", "doesnt", "didnt", "isnt", "wasnt"}

        for i, t in enumerate(tokens):
            prev = tokens[i - 1] if i > 0 else ""
            negated = prev in NEGATORS

            if t in self.positive_words:
                score += -1 if negated else 1
            elif t in self.negative_words:
                score -= -1 if negated else 1

        return score

    # ---------------------------------------------------------------------
    # Label prediction
    # ---------------------------------------------------------------------

    def predict_label(self, text: str) -> str:
        """
        Turn the numeric score for a piece of text into a mood label.

        The default mapping is:
          - score > 0  -> "positive"
          - score < 0  -> "negative"
          - score == 0 -> "neutral"

        TODO: You can adjust this mapping if it makes sense for your model.
        For example:
          - Use different thresholds (for example score >= 2 to be "positive")
          - Add a "mixed" label for scores close to zero
        Just remember that whatever labels you return should match the labels
        you use in TRUE_LABELS in dataset.py if you care about accuracy.
        """
        # TODO: Implement this method.
        #   1. Call self.score_text(text) to get the numeric score.
        #   2. Return "positive" if the score is above 0.
        #   3. Return "negative" if the score is below 0.
        #   4. Return "neutral" otherwise.
        if self.score_text(text) > 2:
            return "positive"
        elif self.score_text(text) < 0:
            return "negative"
        elif self.score_text(text) == 0:
            return "neutral"
        else:
            return "mixed"
            

    # ---------------------------------------------------------------------
    # Explanations (optional but recommended)
    # ---------------------------------------------------------------------

    def explain(self, text: str) -> str:
        """
        Return a short string explaining WHY the model chose its label.

        TODO:
          - Look at the tokens and identify which ones counted as positive
            and which ones counted as negative.
          - Show the final score.
          - Return a short human readable explanation.

        Example explanation (your exact wording can be different):
          'Score = 2 (positive words: ["love", "great"]; negative words: [])'

        The current implementation is a placeholder so the code runs even
        before you implement it.
        """
        tokens = self.preprocess(text)

        positive_hits: List[str] = []
        negative_hits: List[str] = []
        score = 0

        for token in tokens:
            if token in self.positive_words:
                positive_hits.append(token)
                score += 1
            if token in self.negative_words:
                negative_hits.append(token)
                score -= 1

        return (
            f"Score = {score} "
            f"(positive: {positive_hits or '[]'}, "
            f"negative: {negative_hits or '[]'})"
        )


if __name__ == "__main__":
    from dataset import SAMPLE_POSTS

    analyzer = MoodAnalyzer()

    print("=== Preprocessing Verification ===")
    print("Checks that punctuation is stripped and emojis become tokens.\n")

    for post in SAMPLE_POSTS:
        tokens = analyzer.preprocess(post)
        # Highlight tokens that actually hit a word list so we can spot misses.
        hits = [t for t in tokens if t in analyzer.positive_words or t in analyzer.negative_words]
        print(f"  Input : {post!r}")
        print(f"  Tokens: {tokens}")
        print(f"  Hits  : {hits if hits else '(none — will score neutral)'}")
        print()

