.PHONY: create-env run

create-env:
	python3 -m venv venv && \
	source venv/bin/activate && \
	pip install -r requirements.txt ;\

run:
	source venv/bin/activate && \
	python3 main.py ;\
