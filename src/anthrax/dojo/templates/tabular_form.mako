<% requirements = set(['dijit/form/Form', 'dojo/parser', 'dojo/domReady']) %>
<%def name="render_tabular(container)">
% for fname, field in container.__fields__.items():
    % if h.is_container(field):
        ${render_tabular(field)}
    % else:
    <tr>
    <%
require, rendering = field.render(form=form)
if require:
    requirements.add(require)
endif
    %>
    <td>${field.label}</td>
    <td>${rendering}</td>
    <td></td>
    </tr>
    % endif
% endfor
</%def>

<form\
   data-dojo-type='dijit.form.Form'
   % if 'action' in form.kwargs:
   action = "${form.kwargs['action']}"
   % endif
   % if 'method' in form.kwargs:
   method = "${form.kwargs['method']}"
   % endif
   % if form.has_uploads():
   enctype="multipart/form-data"
   % endif
   id="${form.id}"
>
    <table>
    <tbody>
    ${render_tabular(form)}
    </tbody>
    </table>
</form>
<script type="text/javascript">
    require([${h.render_requirements(requirements)}]
    % if form.kwargs.get('do_parsing', False):
    , function () {
        dojo.parser.parse(dojo.byId('${form.id}'));
    }
    % endif
    );
</script>
