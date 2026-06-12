from phrasis import GibberishDetector

detector = GibberishDetector()

detector.model.train(
    [
        "hello world",
        "computer science",
        "natural language processing",
        "machine learning",
    ]
)

print(detector.analyze("xqzkjr"))
print(detector.analyze("computer"))
