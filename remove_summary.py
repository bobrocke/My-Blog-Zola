import os
import glob

def process_file(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    if len(lines) == 0 or not lines[0].startswith('---'):
        return

    in_front_matter = False
    summary_line_index = -1
    
    for i, line in enumerate(lines):
        if i == 0 and line.startswith('---'):
            in_front_matter = True
            continue
        if in_front_matter and line.startswith('---'):
            break
        if in_front_matter and line.startswith('summary:'):
            summary_line_index = i
            break
            
    if summary_line_index != -1:
        lines.pop(summary_line_index)
        with open(filepath, 'w') as f:
            f.writelines(lines)
        print(f"Removed summary from {os.path.basename(filepath)}")

for filepath in glob.glob('content/blog/*.md'):
    process_file(filepath)
