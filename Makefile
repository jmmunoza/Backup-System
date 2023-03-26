compress:
	python app/store/main.py ./data/input/ ./data/output/

decompress:
	python app/restore/main.py ./data/output/ ./data/restore/