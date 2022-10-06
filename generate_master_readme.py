from pathlib import Path
from urllib.parse import quote

readme_content = '''
# QuicklyIn is a collection of scrips, docs and automations to make life easy :)


'''

readme_paths = [f for f in Path('.').rglob(
    "*") if f.is_file() and f.suffix == '.md']


readme_list = list()

for readme_path in readme_paths:
    readme_list.append(
        f'- [{readme_path.parent.name}]({quote(str(readme_path))})')

readme_list = '\n'.join(readme_list)

readme_content = f'{readme_content}{readme_list}'

with open("Readme.md", "w") as main_readme:
    main_readme.write(readme_content)
