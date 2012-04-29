import tempfile
import pkg_resources as pr

import mako.lookup

from anthrax.dojo import view_helpers

LOOKUP = mako.lookup.TemplateLookup(directories=[
    pr.resource_filename('anthrax.dojo', '/templates')
], module_directory=tempfile.mkdtemp())


class SimpleDojoView():
    lookup = LOOKUP

    def __init__(self, require, template_name):
        self.require = require
        self.template_name = template_name

    def __call__(self, **kwargs):
        kwargs['h'] = view_helpers
        return (
            self.require,
            self.lookup.get_template(self.template_name).render(**kwargs)
        )

anthrax_text_box_view = SimpleDojoView(
    'anthrax/AnthraxTextBox', 'anthrax_text_box.mako'
)
spinner_view = SimpleDojoView('dijit/form/NumberSpinner', 'spinner.mako')
editor = SimpleDojoView('dijit/Editor', 'editor.mako')

def html_tabular_form_view(form):
    return LOOKUP.get_template('tabular_form.mako').render(
        form=form, h=view_helpers
    )
