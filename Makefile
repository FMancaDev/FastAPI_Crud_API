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
	$(VENV)/bin/uvicorn my_api.app.main:app --reload

freeze:
	$(PIP) freeze > my_api/requirements.txt

clean:
	rm -rf $(VENV)
