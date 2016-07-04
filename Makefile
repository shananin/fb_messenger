lint:
	. venv/bin/activate && \
	pylint fb_messenger

tests:
	. venv/bin/activate && \
	nosetests --cover-branches --with-coverage --cover-erase --cover-package=fb_messenger

clean:
	rm -rf venv

virtualenv:
	virtualenv venv && \
	pip install --upgrade pip && \
	pip install -r requirements.txt