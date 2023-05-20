init :
	sudo apt install graphviz
	pip install -r requirements.txt

diagrams :
	mkdir -p output
	@for f in $(shell ls diagram_as_code); do python3 diagram_as_code/$${f}; done
