define([
    'dijit/form/ValidationTextBox', 'dojo/_base/declare'
    ], function (ValidationTextBox, declare) {
        return declare('anthrax.AnthraxTextBox', [ValidationTextBox], {
            minLen: null,
            maxLen: null,
            minLenMessage: '$_unset_$',
            maxLenMessage: '$_unset_$',
            validate: function (isFocused) {
                var tooShort, isValid = false;
                if (
                    this.maxLen !== null && 
                    this.textbox.value.length > this.maxLen
                ) {
                    this._set('state', 'Error');
                    this.set('message', this.maxLenMessage);
                    return false;
                }
                if (
                    this.minLen !== null && 
                    this.textbox.value.length < this.minLen
                ) {
                    if (!isFocused) {
                        this._set('state', 'Error');
                        this.set('message', this.minLenMessage);
                        return false;
                    } else {
                        tooShort = true;
                    }
                }
                isValid = this.inherited(arguments);
                if (!isValid && tooShort) {
                    this._set('state', 'Incomplete');
                }
                return isValid;
            } 
        });
    }
);
