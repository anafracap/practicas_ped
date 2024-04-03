
SRC=hw
EXE=$(SRC)


do: console

all: console

console: awk bc c c++ factor forth haskell java javascript lisp lua perl python ruby rust scheme sh \
	 clean

python: $(SRC).py
	@echo "Hello world en $@..."
	python $<

clean:
	@echo "Limpiando..."
	rm -f $(EXE) HelloWorld.class

