<input name="${field.name}"\
% if field.raw_value:
value="${field.raw_value}"
% endif
type="${input_type}"
data-dojo-type="anthrax.AnthraxTextBox"
<% constraints = h.render_textbox_constraints(field) %>
% if constraints:
data-dojo-props="${constraints}"
% endif
/>
