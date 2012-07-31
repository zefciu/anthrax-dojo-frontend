define([
    'dijit/form/DateTextBox', 'dojo/_base/declare', 'dojo/date/locale'
    ], function (DateTextBox, declare, locale) {
        return declare('anthrax.AnthraxDateBox', [DateTextBox], {
            datePattern: 'd-m-Y',
            value: '',
            _getFormat: function () {
                return {
                    selector: 'date', datePattern: this.datePattern,
                    locale: 'en-us'
                };
            },

            beforeMixinProperties: function() {
                this.inherited(arguments)
                this.value = locale.parse(this.value, this._getFormat());
            },

            serialize: function () {
                return locale.format(this.value, this._getFormat());
            } 

        });
    }
);
