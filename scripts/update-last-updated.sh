#!/bin/bash

BRANCH="main"
git fetch origin

# Get list of changed files since last push (relative to remote)
CHANGED=$(git diff --name-only origin/$BRANCH...HEAD)

# Go through all .md files under docs/
while IFS= read -r -d '' FILE; do

  find docs/ -type f -name '*.md' -print0 |
  if [ ! -f "$FILE" ]; then
    echo "❌ File not found: $FILE"
    continue
  fi

  # Get latest Git commit date for the file
  DATE=$(git log -1 --date=short --format="%ad" -- "$FILE")
  if [ -z "$DATE" ]; then
    DATE=$(date +%F)
    echo "ℹ️  $FILE is uncommitted — using today's date: $DATE"
  fi

  # Backup the file
  cp "$FILE" "$FILE.bak"

  # Check if it already has a "Last updated" line
  if grep -q "^_Last updated:" "$FILE"; then
    if echo "$CHANGED" | grep -q "^$FILE$"; then
      # It's changed → update the existing line
      awk -v date="$DATE" '
        BEGIN { updated = 0 }
        /^# / {
          print
          getline
          if ($0 ~ /^_Last updated:/) {
            print "_Last updated: " date "_"
            updated = 1
          } else {
            print $0
            print "_Last updated: " date "_"
            updated = 1
          }
          next
        }
        { print }
      ' "$FILE.bak" >"$FILE"
      echo "🔁 Updated: $FILE → $DATE"
    else
      echo "✅ No change: $FILE — last updated line preserved"
    fi
  else
    # No existing line → insert after first header
    awk -v date="$DATE" '
      BEGIN { inserted = 0 }
      /^# / {
        print
        print "_Last updated: " date "_"
        inserted = 1
        next
      }
      { print }
    ' "$FILE.bak" >"$FILE"
    echo "➕ Added: $FILE → $DATE"
  fi

  rm -f "$FILE.bak"
done
