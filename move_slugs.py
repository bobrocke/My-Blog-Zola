import os
import glob

def process_file(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    if len(lines) == 0 or not lines[0].startswith('---'):
        return

    in_front_matter = False
    front_matter_end = -1
    slug_line_index = -1
    date_line_index = -1
    
    for i, line in enumerate(lines):
        if i == 0 and line.startswith('---'):
            in_front_matter = True
            continue
        if in_front_matter and line.startswith('---'):
            front_matter_end = i
            break
        if in_front_matter and line.startswith('slug:'):
            slug_line_index = i
        if in_front_matter and line.startswith('date:'):
            date_line_index = i
            
    if slug_line_index != -1 and date_line_index != -1:
        if slug_line_index == date_line_index + 1:
            return
            
        slug_line = lines.pop(slug_line_index)
        
        if slug_line_index < date_line_index:
            date_line_index -= 1
            
        lines.insert(date_line_index + 1, slug_line)
        
        with open(filepath, 'w') as f:
            f.writelines(lines)
        print(f"Moved slug in {os.path.basename(filepath)}")

for filepath in glob.glob('content/blog/*.md'):
    process_file(filepath)
