#!/bin/bash

# Define the blog post content directory
POSTS_DIR="./content/blog"

# Get the current date and time in the format YYYY-MM-DD
DATE=$(date +"%Y-%m-%d")

# Prompt the user for the post title
read -p "Enter the title for your new post: " POST_TITLE

# Convert the title to a URL-friendly slug
POST_SLUG=$(echo "$POST_TITLE" | tr '[:upper:]' '[:lower:]' | tr ' ' '-' | tr -cd 'a-z0-9-')

# Combine date and slug to create the filename
FILE_NAME="${POST_SLUG}.md"

# Create the full file path
FILE_PATH="${POSTS_DIR}/${FILE_NAME}"

# Check if the posts directory exists; create it if not
mkdir -p "$POSTS_DIR"

# Write the YAML front matter and a placeholder title to the new file
cat > "$FILE_PATH" << EOF
---
title: $POST_TITLE
date: $DATE
taxonomies:
  categories: []
  tags: []
draft: true
---

# $POST_TITLE

Start writing your post here...
EOF

echo "Created new post (no "): $FILE_PATH"
# Open the file for editing (optional)
open "$FILE_PATH" # macOS
# xdg-open "$FILE_PATH" # Linux
