import jinja2
from pathlib import Path
import sass

ROOT_DIR = Path(__file__).parent.absolute()

TEMPLATE_DIR = ROOT_DIR / Path('templates')
STYLES_DIR = ROOT_DIR / Path('style')
BUILD_DIR = ROOT_DIR / Path('www')

if not BUILD_DIR.exists():
    BUILD_DIR.mkdir()

BUILD_DIR_STYLES = BUILD_DIR / Path('styles')
if not BUILD_DIR_STYLES.exists():
    BUILD_DIR_STYLES.mkdir()

GLOBAL_CONTENT = {
    'topbar_items': {
        'About': '/',
        'Tools': '/code',
        'Sketches': '/sketches',
        'Renders': '/renders',
        'Music': '/music',
        'Ramblings': '/ramblings'
    }
}

if __name__ == '__main__':
    sass.compile(dirname=(STYLES_DIR, BUILD_DIR_STYLES), output_style='expanded')
    templates = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR), trim_blocks=True, lstrip_blocks=True)

    for template_name in templates.list_templates():
        if 'base' in template_name:
            continue
        
        template = templates.get_template(template_name)
        build_file = Path(template_name).with_suffix('.html')
        build_file = BUILD_DIR / build_file
        build_path = build_file.parent

        if not build_path.exists():
            build_path.mkdir()

        section = {
            'header': 'Test'
        }

        content = dict(GLOBAL_CONTENT)
        template_url = template_name.replace('jinja', 'html')
        print(template_name, template_url)
        if 'index.html' in template_url:
            template_url = template_url.replace('index.html', '')
            if template_url and template_url[-1] == '/':
                template_url = template_url[:-1]

        content['active_page'] = f'/{template_url}'
        content['sections'] = [section]

        print(content)

        with open(build_file, 'w+') as fn:
            fn.write(template.render(**content))
