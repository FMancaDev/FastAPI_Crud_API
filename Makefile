VENV = venv

PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

all: install

$(VENV):
	python3 -m venv $(VENV)

install: $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install fastapi "uvicorn[standard]"

run:
	$(VENV)/bin/uvicorn main:app --reload

# Limpar venv
clean:
	rm -rf $(VENV)
