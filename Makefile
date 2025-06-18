.PHONY: update-references add-ui-elements update-last-updated-notice all

all: update-references add-ui-elements update-last-updated-notice

update-references:
	python scripts/update_references.py

add-ui-elements:
	python scripts/add_ui_elements.py

update-last-updated-notice:
	sh scripts/update-last-updated-notice.sh
