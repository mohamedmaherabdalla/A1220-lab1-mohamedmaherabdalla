run:
	./.venv/bin/python -m src.receipt_parser.main app/receipts --print

docs:
	./.venv/bin/pdoc src/receipt_parser -o docs