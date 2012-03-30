from anthrax.frontend import Frontend
from anthrax.dojo import view as v

dojo_frontend = Frontend({
    'text_input': v.anthrax_text_box_view,
    'spinner': v.spinner_view
}, v.html_tabular_form_view)
