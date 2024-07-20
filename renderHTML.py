from jinja2 import Template, Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("."))

def render_html(file, json_dict):
    template = env.get_template(file)

    return template.render(json_dict)