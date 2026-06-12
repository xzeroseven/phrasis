from phrasis import corpora
from phrasis import GibberishDetector

corpus = corpora.load_builtin("zen_of_python")
detector = GibberishDetector()
detector.model.train(corpus)
print(detector.analyze("xqzkjr"))
print(detector.analyze("computer"))
