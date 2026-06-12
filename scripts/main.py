from phrasis import corpora

from phrasis import GibberishDetector

corpus = corpora.load_builtin("zen_of_python")
detector = GibberishDetector()
detector.model.train(corpus)
print(detector.analyze("xqzfdsfadfasdfasdfbdvrnjmukukjuhysfbadfbadbfadfkjr"))
print(detector.analyze("Beautiful"))
