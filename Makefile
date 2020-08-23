all: build/protokoll.pdf


build/protokoll.pdf: protokoll.tex		
	latexmk --lualatex --output-directory=build protokoll.tex

data:# build/EMPTY.tex

#ERZEUGE				ZUTATEN		REZEPT(TERMINAL BEFEHL)

#build/EMPTY.tex: EMPTY.py | build
#	TEXINPUTS=$$(pwd)/..: python EMPTY.py
	
#build/EMPTY.tex: EMPTY.py | build
#	TEXINPUTS=$$(pwd)/..: python EMPTY.py

#build/EMPTY.tex: EMPTY.py | build
#	TEXINPUTS=$$(pwd)/..: python EMPTY.py

#build/EMPTY.tex: EMPTY.py | build
#	TEXINPUTS=$$(pwd)/..: python EMPTY.py

build: 
	mkdir -p build

clean:
	rm -r build
