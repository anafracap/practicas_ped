SRC1=oop1
SRC2=oop2
EXE=.exe
CPPOPTIONS="-std=c++11"


do: all

all: c++1 py1 c++2 py2 ejemplo-oop

c++1: $(SRC1).cpp
	@echo "Tutorial $@..."
	g++ $(CPPOPTIONS) -o $(SRC1)$(EXE) $< && ./$(SRC1)$(EXE)

c++2: $(SRC2).cpp
	@echo "Tutorial $@..."
	g++ $(CPPOPTIONS) -o $(SRC2)$(EXE) $< && ./$(SRC2)$(EXE)

py1: $(SRC1).py
	@echo "Tutorial $@..."
	python $<

py2: $(SRC2).py
	@echo "Tutorial $@..."
	python $<

ejemplo-oop: ejemplo-oop.py
	@echo "Tutorial $@..."
	python $<


clean:
	@echo "Limpiando..."
	rm -f $(SRC1)$(EXE) $(SRC2)$(EXE)
