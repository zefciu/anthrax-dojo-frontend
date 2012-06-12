import unittest

from lxml.html import assertHTMLEqual

from anthrax.container import Form, Container
import anthrax.field as f
from anthrax.html_input.field import HtmlField


class Test(unittest.TestCase):
    """Rendering forms"""

    def setUp(self):
        def purity_test(form):
            if form['name'] == 'Galahad' and form['nickname'] != 'the Pure':
                raise FormValidationError(
                    ['name', 'nickname'], 
                    'Sir Galahad must be pure',
                )
        class TestForm(Form):
            __frontend__ = 'dojo'
            class personals(Container):
                __validators__ = [purity_test]
                name = f.TextField(
                    label='Name',
                    regexp=r'^[A-Z][a-z]+$',
                    regexp_message='Write your name with a capital',
                    max_len=20, max_len_message='You must be kidding!',
                )
                nickname = f.TextField(label='Nickname', max_len=30)
                age = f.IntegerField(label='Age', min=7, max=99)
                long_description = HtmlField(id='wysiwyg',
                    label='Long description')
        self.form = TestForm()

    def test_render(self):
        assertHTMLEqual(self.form.render(), r"""<form>
    <table>
    <tbody>
        <tr>
            <td>Name</td>
            <td><input data-dojo-type="anthrax.AnthraxTextBox" name="name" 
            data-dojo-props="regexp: /^[A-Z][a-z]+$/, invalidMessage: 'Write your name with a capital', maxLen: 20, maxLenMessage: 'You must be kidding!'" />
            </td>
            <td></td>
        </tr><tr>
            <td>Nickname</td>
            <td><input data-dojo-type="anthrax.AnthraxTextBox" name="nickname" 
            data-dojo-props="maxLen: 30, maxLenMessage: 'Value can\'t be longer than 30'" />
            </td>
            <td></td>
        </tr><tr>
            <td>Age</td>
            <td><input data-dojo-type="dijit.form.NumberSpinner"
            data-dojo-props="constraints: {min: 7, max: 99}"
            name="age" /></td>
            <td></td>
        </tr><tr>
            <td>Long description</td>
            <td><input id="wysiwyg-value" name="long_description" type="hidden" />
            <div data-dojo-type="dijit.Editor"
            onchange="dojo.byId('wysiwyg-value').value = this.getValue();">
            </div>
            </td>
            <td></td>
        </tr>
    </tbody>
    </table>

</form>
<script type="text/javascript">
    require(['anthrax/js/AnthraxTextBox', 'dijit/Editor', 'dijit/form/Form', 'dijit/form/NumberSpinner', 'dojo/domReady', 'dojo/parser']);
</script>
""")

