"""
Shared data for the Mood Machine lab.

This file defines:
  - POSITIVE_WORDS: starter list of positive words
  - NEGATIVE_WORDS: starter list of negative words
  - SAMPLE_POSTS: short example posts for evaluation and training
  - TRUE_LABELS: human labels for each post in SAMPLE_POSTS
"""

# ---------------------------------------------------------------------
# Starter word lists
# ---------------------------------------------------------------------

POSITIVE_WORDS = [
    "happy",
    "great",
    "good",
    "love",
    "excited",
    "awesome",
    "fun",
    "chill",
    "relaxed",
    "amazing",
    "emoji_joy",    # 😂 — laughter/hype in this dataset
]

NEGATIVE_WORDS = [
    "sad",
    "bad",
    "terrible",
    "awful",
    "angry",
    "upset",
    "tired",
    "stressed",
    "hate",
    "boring",
    "emoji_skull",  # 💀 — "I'm dead" slang; negative in this dataset
]

# ---------------------------------------------------------------------
# Starter labeled dataset
# ---------------------------------------------------------------------

# Short example posts written as if they were social media updates or messages.
SAMPLE_POSTS = [
    "I love this class soooo much!", # easy: everything is pos
    "Today was a terrible day", # easy
    "Feeling tired but kind of hopeful", # mixed
    "This is fine", # mixed
    "So excited for the weekend", # easy: everything pos
    "I am not happy about this", #easy
    
    "This party was awesome",
    "This thing sucks",
    "Lowkey loving the energy but highkey tired 😅", #mixed, copilot
    "No cap, this is the best day ever 😂", #easy, copilot
    "I’m dead 💀 that test was so long", # easy, copilot
]

# Human labels for each post above.
# Allowed labels in the starter:
#   - "positive"
#   - "negative"
#   - "neutral"
#   - "mixed"
TRUE_LABELS = [
    "positive",  # "I love this class so much"
    "negative",  # "Today was a terrible day"
    "mixed",     # "Feeling tired but kind of hopeful"
    "neutral",   # "This is fine"
    "positive",  # "So excited for the weekend"
    "negative",  # "I am not happy about this"

    "positive", # "This party was awesome"
    "negative", # "This thing sucks"
    "mixed", # "Lowkey loving the energy but highkey tired 😅" #mixed, copilot
    "positive", # "No cap, this is the best day ever 😂" #easy, copilot
    "negative", # "I’m dead 💀 that test was so long" # easy, copilot
]

# Add 5-10 more posts and labels.
#
# Requirements:
#   - For every new post you add to SAMPLE_POSTS, you must add one
#     matching label to TRUE_LABELS.
#   - SAMPLE_POSTS and TRUE_LABELS must always have the same length.
#   - Include a variety of language styles, such as:
#       * Slang ("lowkey", "highkey", "no cap")
#       * Emojis (":)", ":(", "🥲", "😂", "💀")
#       * Sarcasm ("I absolutely love getting stuck in traffic")
#       * Ambiguous or mixed feelings
#
# Tips:
#   - Try to create some examples that are hard to label even for you.
#   - Make a note of any examples that you and a friend might disagree on.
#     Those "edge cases" are interesting to inspect for both the rule based
#     and ML models.
#
# Example of how you might extend the lists:
#
# SAMPLE_POSTS.append("Lowkey stressed but kind of proud of myself")
# TRUE_LABELS.append("mixed")

SAMPLE_POSTS.append("Lowkey stressed but kind of proud of myself")
TRUE_LABELS.append("mixed")

SAMPLE_POSTS.append("Messi is legit the best player in the world cup rn")
TRUE_LABELS.append("neutral")

SAMPLE_POSTS.append("Morocco won the penalty shootout!")
TRUE_LABELS.append("positive")

SAMPLE_POSTS.append("Ugh why is this team lowkey not it")
TRUE_LABELS.append("negative")

SAMPLE_POSTS.append("Happy I get to watch the world cup but sad I'm not watching in person")
TRUE_LABELS.append("mixed")


# Remember to keep them aligned:
print(len(SAMPLE_POSTS) == len(TRUE_LABELS))
