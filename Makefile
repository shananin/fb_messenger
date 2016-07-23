install:
	virtualenv venv && \
	. venv/bin/activate && \
	pip install --upgrade pip && \
	pip install -r requirements.txt

lint:
	. venv/bin/activate && \
	pylint fb_messenger

test:
	. venv/bin/activate && \
	py.test -v --cov=fb_messenger --cov coveralls --cov-report term-missing tests/

clean:
	rm -rf venv

virtualenv:
	virtualenv venv && \
	pip install --upgrade pip && \
	pip install -r requirements.txt
