//Variables y Funciones

Blockly.Blocks['priomh'] = {
  init: function() {
    this.appendStatementInput("priomh")
        .setCheck(null)
        .appendField("priomh");
    this.setInputsInline(true);
    this.setNextStatement(true, null);
    this.setColour(300);
    this.setTooltip('');
    this.setHelpUrl('');
  }
};
Blockly.Blocks['return'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("return")
        .appendField(new Blockly.FieldTextInput("value"), "returnValue");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(60);
    this.setTooltip('');
    this.setHelpUrl('');
  }
};

Blockly.Blocks['print'] = {
  init: function() {
    this.appendValueInput("print")
        .setCheck(null)
        .appendField("print");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(60);
    this.setTooltip('');
    this.setHelpUrl('');
  }
};

Blockly.Blocks['var'] = {
  init: function() {
    this.appendValueInput("print")
        .setCheck(null)
        .appendField(new Blockly.FieldDropdown([["int","int"], ["string","string"], ["double","double"], ["bool","bool"]]), "type")
        .appendField(new Blockly.FieldTextInput("varName"), "varname")
        .appendField("=");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
    this.setTooltip('');
    this.setHelpUrl('');
  }
};
//Blockly.Blocks['function'] = {
//   init: function() {
//     this.appendValueInput("NAME")
//         .setCheck(null)
//         .appendField("function")
//         .appendField(new Blockly.FieldDropdown([["int","int"], ["double","double"], ["float","float"]]), "NAME")
//         .appendField(new Blockly.FieldTextInput("functionName"), "funcName");
//     this.setInputsInline(true);
//     this.setPreviousStatement(true, null);
//     this.setNextStatement(true, null);
//     this.setColour(230);
//     this.setTooltip('');
//     this.setHelpUrl('');
//   }
// };

Blockly.Blocks['function'] = {
  init: function() {
    this.appendValueInput("function1")
        .setCheck(null)
        .appendField("function")
        .appendField(new Blockly.FieldDropdown([["int","int"], ["float","float"], ["bool","bool"], ["char","char"], ["string","string"]]), "type")
        .appendField(new Blockly.FieldTextInput("functionName"), "funcName");
    this.appendStatementInput("function2")
        .setCheck(null);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
    this.setTooltip('');
    this.setHelpUrl('');
  }
};

Blockly.Blocks['endfunc'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("endFunc");
     this.setPreviousStatement(true, null);
    this.setColour(60);
    this.setTooltip('');
    this.setHelpUrl('');
  }
};

Blockly.Blocks['param'] = {
  init: function() {
    this.appendValueInput("var")
        .setCheck(null)
        .appendField(new Blockly.FieldDropdown([["int","int"], ["double","double"], ["float","float"], ["string","string"]]), "var")
        .appendField(new Blockly.FieldTextInput("varName"), "varName");
    this.setInputsInline(false);
    this.setOutput(true, null);
    this.setColour(230);
    this.setTooltip('');
    this.setHelpUrl('');
  }
};

Blockly.Blocks['param2'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldDropdown([["int","int"], ["double","double"], ["float","float"], ["string","string"]]), "var")
        .appendField(new Blockly.FieldTextInput("varName"), "varName");
    this.setOutput(true, null);
    this.setColour(230);
    this.setTooltip('');
    this.setHelpUrl('');
  }
};

Blockly.Blocks['string'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("\"")
        .appendField(new Blockly.FieldTextInput(""), "stnInput")
        .appendField("\"");
    this.setOutput(true, "String");
    this.setColour(230);
    this.setTooltip('');
    this.setHelpUrl('');
  }
};

Blockly.Blocks['assingvalue'] = {
  init: function() {
    this.appendValueInput("print")
        .setCheck(null)
        .appendField(new Blockly.FieldTextInput("varName"), "varname")
        .appendField("=");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
    this.setTooltip('');
    this.setHelpUrl('');
  }
};
//....................................................................................................................
//Operaciones

Blockly.Blocks['sum'] = {
  init: function() {
    this.appendValueInput("var1")
        .setCheck(null);
    this.appendDummyInput()
        .appendField("+");
    this.appendValueInput("var2")
        .setCheck(null);
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
    this.setTooltip('');
    this.setHelpUrl('');
  }
};

Blockly.Blocks['sub'] = {
  init: function() {
    this.appendValueInput("var1")
        .setCheck(null);
    this.appendDummyInput()
        .appendField("-");
    this.appendValueInput("var2")
        .setCheck(null);
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
    this.setTooltip('');
    this.setHelpUrl('');
  }
};

Blockly.Blocks['mult'] = {
  init: function() {
    this.appendValueInput("var1")
        .setCheck(null);
    this.appendDummyInput()
        .appendField("*");
    this.appendValueInput("var2")
        .setCheck(null);
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
    this.setTooltip('');
    this.setHelpUrl('');
  }
};

Blockly.Blocks['div'] = {
  init: function() {
    this.appendValueInput("var1")
        .setCheck(null);
    this.appendDummyInput()
        .appendField("/");
    this.appendValueInput("var2")
        .setCheck(null);
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
    this.setTooltip('');
    this.setHelpUrl('');
  }
};

Blockly.Blocks['sum2'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldNumber(0), "var1")
        .appendField("+")
        .appendField(new Blockly.FieldNumber(0), "NAME");
    this.setInputsInline(false);
    this.setOutput(true, null);
    this.setColour(230);
    this.setTooltip('');
    this.setHelpUrl('');
  }
};

Blockly.Blocks['sub2'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldNumber(0), "var1")
        .appendField("+")
        .appendField(new Blockly.FieldNumber(0), "NAME");
    this.setInputsInline(false);
    this.setOutput(true, null);
    this.setColour(230);
    this.setTooltip('');
    this.setHelpUrl('');
  }
};

Blockly.Blocks['div2'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldNumber(0), "var1")
        .appendField("+")
        .appendField(new Blockly.FieldNumber(0), "NAME");
    this.setInputsInline(false);
    this.setOutput(true, null);
    this.setColour(230);
    this.setTooltip('');
    this.setHelpUrl('');
  }
};

Blockly.Blocks['mult2'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldNumber(0), "var1")
        .appendField("+")
        .appendField(new Blockly.FieldNumber(0), "NAME");
    this.setInputsInline(false);
    this.setOutput(true, null);
    this.setColour(230);
    this.setTooltip('');
    this.setHelpUrl('');
  }
};

//....................................................................................................................
//Operadores Logicos

Blockly.Blocks['lessthan'] = {
  init: function() {
    this.appendValueInput("var1")
        .setCheck("Number");
    this.appendValueInput("var2")
        .setCheck("Number")
        .appendField("<");
    this.setInputsInline(true);
    this.setOutput(true, "Boolean");
    this.setColour(230);
    this.setTooltip('');
    this.setHelpUrl('');
  }
};


Blockly.Blocks['greaterthan'] = {
  init: function() {
    this.appendValueInput("var1")
        .setCheck("Number");
    this.appendValueInput("var2")
        .setCheck("Number")
        .appendField(">");
    this.setInputsInline(true);
    this.setOutput(true, "Boolean");
    this.setColour(230);
    this.setTooltip('');
    this.setHelpUrl('');
  }
};

Blockly.Blocks['equality'] = {
  init: function() {
    this.appendValueInput("var1")
        .setCheck("Number");
    this.appendValueInput("var2")
        .setCheck("Number")
        .appendField("==");
    this.setInputsInline(true);
    this.setOutput(true, "Boolean");
    this.setColour(230);
    this.setTooltip('');
    this.setHelpUrl('');
  }
};

Blockly.Blocks['lessthanEquals'] = {
  init: function() {
    this.appendValueInput("var1")
        .setCheck("Number");
    this.appendValueInput("var2")
        .setCheck("Number")
        .appendField(">=");
    this.setInputsInline(true);
    this.setOutput(true, "Boolean");
    this.setColour(230);
    this.setTooltip('');
    this.setHelpUrl('');
  }
};

Blockly.Blocks['greaterthanEquals'] = {
  init: function() {
    this.appendValueInput("var1")
        .setCheck("Number");
    this.appendValueInput("var2")
        .setCheck("Number")
        .appendField(">=");
    this.setInputsInline(true);
    this.setOutput(true, "Boolean");
    this.setColour(230);
    this.setTooltip('');
    this.setHelpUrl('');
  }
};

Blockly.Blocks['not'] = {
  init: function() {
    this.appendValueInput("var1")
        .setCheck("Number");
    this.appendValueInput("var2")
        .setCheck("Number")
        .appendField("!=");
    this.setInputsInline(true);
    this.setOutput(true, "Boolean");
    this.setColour(230);
    this.setTooltip('');
    this.setHelpUrl('');
  }
};

Blockly.Blocks['or'] = {
  init: function() {
    this.appendValueInput("var1")
        .setCheck("Number");
    this.appendValueInput("var2")
        .setCheck("Number")
        .appendField("||");
    this.setInputsInline(true);
    this.setOutput(true, "Boolean");
    this.setColour(230);
    this.setTooltip('');
    this.setHelpUrl('');
  }
};

Blockly.Blocks['and'] = {
  init: function() {
    this.appendValueInput("var1")
        .setCheck("Number");
    this.appendValueInput("var2")
        .setCheck("Number")
        .appendField("&&");
    this.setInputsInline(true);
    this.setOutput(true, "Boolean");
    this.setColour(230);
    this.setTooltip('');
    this.setHelpUrl('');
  }
};
//....................................................................................................................
//Ciclos y Condiciones


Blockly.Blocks['if'] = {
  init: function() {
    this.appendValueInput("var")
        .setCheck(null)
        .appendField("if");
    this.appendStatementInput("NAME")
        .setCheck(null)
        .appendField("then");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
    this.setTooltip('');
    this.setHelpUrl('');
  }
};





//-----------------------------------------------------------------------------------------------------------------------
//GENERATORS STUBS 

//Variables y Funciones

Blockly.JavaScript['var'] = function(block) {
  var dropdown_type = block.getFieldValue('type');
  var text_varname = block.getFieldValue('varname');
  var value_print = Blockly.JavaScript.valueToCode(block, 'print', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = dropdown_type + ' ' + text_varname + ' = ' + value_print + '\n';
  return code;
};


Blockly.JavaScript['function'] = function(block) {
  var dropdown_type = block.getFieldValue('type');
  var text_funcname = block.getFieldValue('funcName');
  var value_function1 = Blockly.JavaScript.valueToCode(block, 'function1', Blockly.JavaScript.ORDER_ATOMIC);
  var statements_function2 = Blockly.JavaScript.statementToCode(block, 'function2');
  // TODO: Assemble JavaScript into code variable.
 
  var code = dropdown_type + ' ' + text_funcname + ' ' + value_function1 + '' + '{ \n' + statements_function2 + '}';
  return code;
};


Blockly.JavaScript['priomh'] = function(block) {
  var statements_priomh = Blockly.JavaScript.statementToCode(block, 'priomh');
  // TODO: Assemble JavaScript into code variable.
  var code = 'priomh { \n' + statements_priomh + '\n}';
  return code;
};
Blockly.JavaScript['return'] = function(block) {
  var text_returnvalue = block.getFieldValue('returnValue');
  // TODO: Assemble JavaScript into code variable.
  var code = 'return ' + text_returnvalue + '; \n';
  return code;
};

Blockly.JavaScript['print'] = function(block) {
  var value_print = Blockly.JavaScript.valueToCode(block, 'print', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'print '+value_print + ' ;\n';
  return code;
};


Blockly.JavaScript['endfunc'] = function(block) {
  // TODO: Assemble JavaScript into code variable.
  var code = '\n }\n';
  return code;
};

Blockly.JavaScript['param'] = function(block) {
  var dropdown_var = block.getFieldValue('var');
  var text_varname = block.getFieldValue('varName');
  var value_var = Blockly.JavaScript.valueToCode(block, 'var', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = dropdown_var+' '+text_varname;
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['param2'] = function(block) {
  var dropdown_var = block.getFieldValue('var');
  var text_varname = block.getFieldValue('varName');
  // TODO: Assemble JavaScript into code variable.
  var code = dropdown_var + ' ' + text_varname;
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['string'] = function(block) {
  var text_stninput = block.getFieldValue('stnInput');
  var code = '"' + text_stninput + '"';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['assingvalue'] = function(block) {
  var text_varname = block.getFieldValue('varname');
  var value_print = Blockly.JavaScript.valueToCode(block, 'print', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = text_varname + ' = ' + value_print + ';\n';
  return code;
};
//....................................................................................................................
//Operaciones 
Blockly.JavaScript['sum'] = function(block) {
  var value_var1 = Blockly.JavaScript.valueToCode(block, 'var1', Blockly.JavaScript.ORDER_ATOMIC);
  var value_var2 = Blockly.JavaScript.valueToCode(block, 'var2', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = value_var1 + '+' + value_var2 + '\n';
  return code;
};

Blockly.JavaScript['sub'] = function(block) {
  var value_var1 = Blockly.JavaScript.valueToCode(block, 'var1', Blockly.JavaScript.ORDER_ATOMIC);
  var value_var2 = Blockly.JavaScript.valueToCode(block, 'var2', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = value_var1 + '-' + value_var2;
  return code;
};

Blockly.JavaScript['mult'] = function(block) {
  var value_var1 = Blockly.JavaScript.valueToCode(block, 'var1', Blockly.JavaScript.ORDER_ATOMIC);
  var value_var2 = Blockly.JavaScript.valueToCode(block, 'var2', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = value_var1 + '*' + value_var2;
  return code;
};

Blockly.JavaScript['div'] = function(block) {
  var value_var1 = Blockly.JavaScript.valueToCode(block, 'var1', Blockly.JavaScript.ORDER_ATOMIC);
  var value_var2 = Blockly.JavaScript.valueToCode(block, 'var2', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = value_var1 + '/' + value_var2;
  return code;
};

Blockly.JavaScript['sum2'] = function(block) {
  var number_var1 = block.getFieldValue('var1');
  var number_name = block.getFieldValue('NAME');
  // TODO: Assemble JavaScript into code variable.
  var code = number_var1 + '+ ' + number_name;
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['sub2'] = function(block) {
  var number_var1 = block.getFieldValue('var1');
  var number_name = block.getFieldValue('NAME');
  // TODO: Assemble JavaScript into code variable.
  var code = number_var1 + '- ' + number_name;
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['mult2'] = function(block) {
  var number_var1 = block.getFieldValue('var1');
  var number_name = block.getFieldValue('NAME');
  // TODO: Assemble JavaScript into code variable.
  var code = number_var1 + '* ' + number_name;
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['div2'] = function(block) {
  var number_var1 = block.getFieldValue('var1');
  var number_name = block.getFieldValue('NAME');
  // TODO: Assemble JavaScript into code variable.
  var code = number_var1 + '/ ' + number_name;
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_NONE];
};

//....................................................................................................................
//Operadores logicos

Blockly.JavaScript['lessthan'] = function(block) {
  var value_less1 = Blockly.JavaScript.valueToCode(block, 'var1', Blockly.JavaScript.ORDER_ATOMIC);
  var value_less2 = Blockly.JavaScript.valueToCode(block, 'var2', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = value_less1 + ' < ' + value_less2;
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['greaterthan'] = function(block) {
  var value_less1 = Blockly.JavaScript.valueToCode(block, 'var1', Blockly.JavaScript.ORDER_ATOMIC);
  var value_less2 = Blockly.JavaScript.valueToCode(block, 'var2', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = value_less1 + ' > ' + value_less2;
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['equality'] = function(block) {
  var value_less1 = Blockly.JavaScript.valueToCode(block, 'var1', Blockly.JavaScript.ORDER_ATOMIC);
  var value_less2 = Blockly.JavaScript.valueToCode(block, 'var2', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = value_less1 + ' == ' + value_less2;
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['lessthanEquals'] = function(block) {
  var value_less1 = Blockly.JavaScript.valueToCode(block, 'var1', Blockly.JavaScript.ORDER_ATOMIC);
  var value_less2 = Blockly.JavaScript.valueToCode(block, 'var2', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = value_less1 + ' <=' + value_less2;
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['greaterthanEquals'] = function(block) {
  var value_less1 = Blockly.JavaScript.valueToCode(block, 'var1', Blockly.JavaScript.ORDER_ATOMIC);
  var value_less2 = Blockly.JavaScript.valueToCode(block, 'var2', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = value_less1 + ' >=' + value_less2;
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['not'] = function(block) {
  var value_less1 = Blockly.JavaScript.valueToCode(block, 'var1', Blockly.JavaScript.ORDER_ATOMIC);
  var value_less2 = Blockly.JavaScript.valueToCode(block, 'var2', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = value_less1 + ' !=' + value_less2;
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['or'] = function(block) {
  var value_less1 = Blockly.JavaScript.valueToCode(block, 'var1', Blockly.JavaScript.ORDER_ATOMIC);
  var value_less2 = Blockly.JavaScript.valueToCode(block, 'var2', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = value_less1 + ' ||' + value_less2;
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['and'] = function(block) {
  var value_less1 = Blockly.JavaScript.valueToCode(block, 'var1', Blockly.JavaScript.ORDER_ATOMIC);
  var value_less2 = Blockly.JavaScript.valueToCode(block, 'var2', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = value_less1 + ' &&' + value_less2;
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_NONE];
};
//....................................................................................................................
//Ciclos y Condiciones
Blockly.JavaScript['if'] = function(block) {
  var value_var = Blockly.JavaScript.valueToCode(block, 'var', Blockly.JavaScript.ORDER_ATOMIC);
  var statements_name = Blockly.JavaScript.statementToCode(block, 'NAME');
  // TODO: Assemble JavaScript into code variable.
  var code = 'if ' + value_var;
  return code;
};



