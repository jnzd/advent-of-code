.PHONY: p1
p1:
	ghc --make -dynamic ./p1.hs
	./p1

kotlin:
	kotlinc p1.kt -include-runtime -d p1.jar
	java -jar p1.jar