CACHE=__pycache__
ALLRULES="punteros reales unicode igualdad error overflow casts"

ECHO=echo
PYTHON=python


do: all

all:
	@$(ECHO) "make $(ALLRULES)"


%.exe: %.c
	@$(ECHO) "Tutorial $@..."
	cc -o $* $< && ./$@

%: %.c
	@$(ECHO) "Tutorial $@..."
	cc -o $* $< && ./$@

errorpy: error.py error
	@$(ECHO) "Tutorial $@..."
	$(PYTHON) error.py

unicode: unicode-propiedades.py
	@$(ECHO) "Tutorial $@..."
	$(PYTHON) $<

reales: ieee754-vs-decimal.py
	@$(ECHO) "Tutorial $@..."
	$(PYTHON) $<

igualdad: igualdad-identidad.py
	@echo "Tutorial $@..."
	$(PYTHON) $<

clean:
	@echo "Limpiando..."
	$(RM) -f *.exe *.o $(ALLRULES) $(ALLRULES:=.exe)
	$(RM) -rf $(CACHE)
