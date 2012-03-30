<% requirements = set() %>
<%def name="render_tabular(container)">
% for fname, field in container.__fields__.items():
    % if h.is_container(field):
        ${render_tabular(field)}
    % else:
    <tr>
    <% require, rendering = field.render() %>
    <% requirements.add(require) %>
    <td>${field.label}</td>
    <td>${rendering}</td>
    <td></td>
    </tr>
    % endif
% endfor
</%def>

<form>
    <table>
    <tbody>
    ${render_tabular(form)}
    </tbody>
    </table>
</form>
<script type="text/javascript">
    require([${h.render_requirements(requirements)}]);
</script>
