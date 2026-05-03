import os
import glob

def process_file(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    if len(lines) == 0 or not lines[0].startswith('---'):
        return

    in_front_matter = False
    has_slug = False
    front_matter_end = -1
    for i, line in enumerate(lines):
        if i == 0 and line.startswith('---'):
            in_front_matter = True
            continue
        if in_front_matter and line.startswith('---'):
            front_matter_end = i
            break
        if in_front_matter and line.startswith('slug:'):
            has_slug = True
            break
            
    if not has_slug and front_matter_end != -1:
        filename = os.path.basename(filepath)
        if filename == '_index.md':
            return
        slug = filename[:-3] # remove .md
        lines.insert(front_matter_end, f"slug: {slug}\n")
        with open(filepath, 'w') as f:
            f.writelines(lines)
        print(f"Added slug to {filename}")

for filepath in glob.glob('content/blog/*.md'):
    process_file(filepath)
