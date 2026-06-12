from phrasis import corpora

from phrasis import GibberishDetector

corpus = corpora.load_builtin("sherlock_holmes")
detector = GibberishDetector()
detector.model.train(corpus)
print(detector.analyze("xqzfdsfadfasdfasdfbdvrnjmukukjuhysfbadfbadbfadfkjr"))
print(detector.analyze("Beautiful day in the neighborhood!"))
