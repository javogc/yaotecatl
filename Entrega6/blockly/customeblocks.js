Blockly.Blocks['var'] = {
  init: function() {
    this.appendValueInput("var")
        .setCheck(null)
        .appendField(new Blockly.FieldDropdown([["int","INT"], ["double","DOUBLE"], ["float","FLOAT"], ["string","STRING"]]), "var")
        .appendField(new Blockly.FieldTextInput("nameOfVar"), "NAME")
        .appendField("=");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
    this.setTooltip('');
    this.setHelpUrl('');
  }
};

//GENERATORS STUBS

Blockly.JavaScript['var'] = function(block) {
  var dropdown_var = block.getFieldValue('var');
  var text_name = block.getFieldValue('NAME');
  var value_var = Blockly.JavaScript.valueToCode(block, 'var', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = '...;\n';
  return code;
};