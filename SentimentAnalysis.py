from transformers import pipeline

classifier = pipeline("sentiment-analysis")
abc = classifier("This is such a great movie!")
print(abc)

