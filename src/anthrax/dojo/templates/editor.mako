<input type="hidden" name="${field.name}" id="${field.id}-value" />
<div onChange="dojo.byId('${field.id}-value').value = this.getValue();"
data-dojo-type="dijit.Editor"
>
% if value:
${field.raw_value}
% endif
</div>
