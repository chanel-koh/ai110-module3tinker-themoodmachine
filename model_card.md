# Model Card: Mood Machine

This model card is for the Mood Machine project, which includes **two** versions of a mood classifier:

1. A **rule based model** implemented in `mood_analyzer.py`
2. A **machine learning model** implemented in `ml_experiments.py` using scikit learn

You may complete this model card for whichever version you used, or compare both if you explored them.

## 1. Model Overview

**Model type:**  
I compared both the rule based and ML model.

**Intended purpose:**  
This model classifies short text messages as moods like positive, negative, neutral, or mixed.

**How it works (brief):**  
For the rule based version, it goes word by word and adds and subtracts based on 
negative or positive association with the word. Then, if the score is greater than two, the message is considered positive. Less than zero is negative. An exactly zero score is netural. A score between 0 and 2 is mixed.  
For the ML version, it uses an ML library called scikit-learn to train on the sample posts and labels in dataset.py. It then uses this learning to classify new messages based on the patterns its learned.



## 2. Data

**Dataset description:**  
There are 16 posts in `SAMPLE_POSTS`, 5 of which are newly added.

**Labeling process:**  
I chose labels for the new examples based on the balance of words in them. If it had both positive and negative words, it is mixed. If only positive, positive (and same for negative). If it's a statement with no emotional words, it's neutral. 

**Important characteristics of your dataset:**   

- Contains slang and emojis  
- Includes sarcasm  
- Some posts express mixed feelings  
- Contains short or ambiguous messages

**Possible issues with the dataset:**  
There could be some abiguity with the mixed sentences to be seen as more positive or negative. Also, there is modern slang included, but older slang may not be represented.

## 3. How the Rule Based Model Works (if used)

**Your scoring rules:**  
Modeling choices made:   

- How positive and negative words affect score incrementally (+ or - 1)
- Negation rules are recognized with a list of negation words  
- Emojis are given a text description and analyzed with that  
- Threshold decisions for labels: positive needs to have multiple positive indicators, otherwise it could be mixed. Same with negative classification. 

**Strengths of this approach:**  
Where does it behave predictably or reasonably well?

Behaves well with clear negative and positive messages.

**Weaknesses of this approach:**  
Where does it fail?  
Mixed moods.

## 4. How the ML Model Works (if used)

**Features used:**  
Describe the representation.  
Bag of words using CountVectorizer.

**Training data:**  
The model trained on `SAMPLE_POSTS` and `TRUE_LABELS`.

**Training behavior:**  
Did you observe changes in accuracy when you added more examples or changed labels?

Yes, adding more examples of mixed increased accuracy for mixed.

**Strengths and weaknesses:**  
Strengths: learns patterns automatically.  
Weaknesses: can overfit to the training data. 

## 5. Evaluation

**How you evaluated the model:**  
Both versions can be evaluated on the labeled posts in `dataset.py`.  
The ML model had 100% accuracy on this dataset.

**Examples of correct predictions:**  
Provide 2 or 3 examples and explain why they were correct.
1. "This is fine" -> neutral. Correct because none of the words have a distinct positive or negative emotion to them, and "fine" is considered very neutral
2. "Messi is legit the best player in the world cup rn" -> neutral. Correct because of the same reason above. 

**Examples of incorrect predictions:**  
Provide 2 or 3 examples and explain why the model made a mistake.  
1. "Feeling tired but kind of hopeful" -> rule-based output: negative. Label: mixed
    The model made a mistake because there is both negative and positive directions in this sentence, making it mixed.
2. "So excited for the weekend" -> rule-based output: mixed. Label: positive
    The model made a mistake because there is only positive emotion in this sentence. It may have gotten confused because there is really only one positive word, "excited", while the other words are neutral. This may indicate the scoring rules need to be modified.

## 6. Limitations

Most prominant limitations:  

- The dataset is small  
- The model does not generalize to longer posts  
- It cannot detect sarcasm reliably  
- It depends heavily on the words chosen or labeled (like the negation words)

## 7. Ethical Considerations

Potential impacts of using mood detection in real applications.  

- Misclassifying a message expressing distress  
- Misinterpreting mood for certain language communities  
- Privacy considerations if analyzing personal messages

## 8. Ideas for Improvement

Ways to improve ML model:   

- Add more labeled data  
- Add a real test set instead of training accuracy only

Ways to improve rule based model:
- Add better preprocessing for emojis or slang  
- Improve the rule based scoring method  
