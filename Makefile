.PHONY: update-references update-last-updated-notice all

all: update-references update-last-updated-notice

update-references:
	python scripts/update_references.py

update-last-updated-notice:
	sh scripts/update-last-updated-notice.sh
