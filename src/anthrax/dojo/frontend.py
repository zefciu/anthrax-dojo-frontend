from anthrax.frontend import Frontend
from anthrax.dojo import view as v

dojo_frontend = Frontend({
    'text_input': v.anthrax_text_box_view,
    'hidden': v.hidden,
    'spinner': v.spinner_view,
    'wysiwyg_editor': v.editor,
    'button': v.button,
}, v.html_tabular_form_view)
