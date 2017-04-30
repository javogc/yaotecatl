//Variables y Funciones

Blockly.Blocks['priomh'] = {
  init: function() {
    this.appendStatementInput("priomh")
        .setCheck(null)
        .appendField("priomh");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
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
    this.setColour(255);
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

// Blockly.Blocks['function'] = {
//   init: function() {
//     this.appendValueInput("function1")
//         .setCheck(null)
//         .appendField("function")
//         .appendField(new Blockly.FieldDropdown([["int","int"], ["float","float"], ["bool","bool"], ["char","char"], ["string","string"]]), "type")
//         .appendField(new Blockly.FieldTextInput("functionName"), "funcName");
//     this.appendStatementInput("function2")
//         .setCheck(null);
//     this.setPreviousStatement(true, null);
//     this.setNextStatement(true, null);
//     this.setColour(230);
//     this.setTooltip('');
//     this.setHelpUrl('');
//   }
// };

Blockly.Blocks['function'] = {
  init: function() {
    this.appendValueInput("parameters")
        .setCheck(null)
        .appendField("function")
        .appendField(new Blockly.FieldDropdown([["int","int"], ["float","float"], ["string","string"], ["boolean","boolean"], ["void","void"]]), "functionType")
        .appendField(new Blockly.FieldTextInput(""), "NAME");
    this.appendStatementInput("content")
        .setCheck(null);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
    this.setTooltip('');
    this.setHelpUrl('');
  }
};

Blockly.Blocks['vars3'] = {
  init: function() {
    this.appendValueInput("var")
        .setCheck(null)
        .appendField(new Blockly.FieldDropdown([["int","int"], ["double","double"], ["float","float"], ["string","string"]]), "var")
        .appendField(new Blockly.FieldTextInput("varName"), "varName")
        .appendField("=")
        .appendField(new Blockly.FieldTextInput("varValue"), "varValue");
    this.setInputsInline(false);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
    this.setTooltip('');
    this.setHelpUrl('');
  }
};

Blockly.Blocks['vars4'] = {
  init: function() {
    this.appendValueInput("var")
        .setCheck(null)
        .appendField(new Blockly.FieldTextInput("varName"), "varName")
        .appendField("=")
        .appendField(new Blockly.FieldTextInput("varValue"), "varValue");
    this.setInputsInline(false);
    this.setOutput(true, null);
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
    this.setColour(255);
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
    this.setColour(255);
    this.setTooltip('');
    this.setHelpUrl('');
  }
};

Blockly.Blocks['parameter'] = {
  init: function() {
    this.appendValueInput("param")
        .setCheck(null)
        .appendField(new Blockly.FieldDropdown([["int","int"], ["float","float"], ["string","string"], ["boolean","boolean"], ["void","void"]]), "paramType")
        .appendField(new Blockly.FieldTextInput(""), "paramVar");
    this.setOutput(true, null);
    this.setColour(255);
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
    this.setColour(255);
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
    this.setColour(255);
    this.setTooltip('');
    this.setHelpUrl('');
  }
};

Blockly.Blocks['array'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("array")
        .appendField(new Blockly.FieldDropdown([["int","int"], ["double","double"], ["bool","bool"], ["string","string"]]), "type")
        .appendField(new Blockly.FieldTextInput("arrayName"), "arrayName")
        .appendField("[")
        .appendField(new Blockly.FieldTextInput("arraySize"), "arraySize")
        .appendField("]");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setColour(255);
    this.setTooltip('');
    this.setHelpUrl('');
  }
};

Blockly.Blocks['arrayparam1'] = {
  init: function() {
    this.appendValueInput("var")
        .setCheck(null)
        .appendField(new Blockly.FieldDropdown([["int","int"], ["double","double"], ["float","float"], ["string","string"]]), "var")
        .appendField(new Blockly.FieldTextInput("arrayName"), "arrayName")
        .appendField("[")
        .appendField(new Blockly.FieldTextInput("arraySize"), "arraySize")
        .appendField("]");
    this.setInputsInline(false);
    this.setOutput(true, null);
    this.setColour(255);
    this.setTooltip('');
    this.setHelpUrl('');
  }
};

Blockly.Blocks['arrayparam2'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldDropdown([["int","INT"], ["double","DOUBLE"], ["float","FLOAT"], ["string","STRING"]]), "var")
        .appendField(new Blockly.FieldTextInput("arrayName"), "arrayName")
        .appendField("[")
        .appendField(new Blockly.FieldTextInput("arraySize"), "arraySize")
        .appendField("]");
    this.setInputsInline(false);
    this.setOutput(true, null);
    this.setColour(255);
    this.setTooltip('');
    this.setHelpUrl('');
  }
};

Blockly.Blocks['text1'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldTextInput("text"), "NAME");
    this.setOutput(true, null);
    this.setColour(230);
    this.setTooltip('');
    this.setHelpUrl('');
  }
};

Blockly.Blocks['funccall1'] = {
  init: function() {
    this.appendValueInput("var1")
        .setCheck(null)
        .appendField(new Blockly.FieldTextInput("functionName"), "funcName")
        .appendField("(");
    this.appendDummyInput()
        .appendField(")");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
    this.setTooltip('');
    this.setHelpUrl('');
  }
};

Blockly.Blocks['funccall2'] = {
  init: function() {
    this.appendValueInput("func")
        .setCheck(null)
        .appendField(new Blockly.FieldTextInput("functionName"), "funcName")
        .appendField("(");
    this.appendDummyInput()
        .appendField(")");
    this.setInputsInline(true);
    this.setOutput(true, null);
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
    this.setOutput(true, null); 
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(195);
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
    this.setOutput(true, null);    
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(195);
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
    this.setOutput(true, null); 
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(195);
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
    this.setOutput(true, null); 
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(195);
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
    this.setColour(195);
    this.setTooltip('');
    this.setHelpUrl('');
  }
};

Blockly.Blocks['sub2'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldNumber(0), "var1")
        .appendField("-")
        .appendField(new Blockly.FieldNumber(0), "NAME");
    this.setInputsInline(false);
    this.setOutput(true, null);
    this.setColour(195);
    this.setTooltip('');
    this.setHelpUrl('');
  }
};

Blockly.Blocks['div2'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldNumber(0), "var1")
        .appendField("/")
        .appendField(new Blockly.FieldNumber(0), "NAME");
    this.setInputsInline(false);
    this.setOutput(true, null);
    this.setColour(195);
    this.setTooltip('');
    this.setHelpUrl('');
  }
};

Blockly.Blocks['mult2'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldNumber(0), "var1")
        .appendField("*")
        .appendField(new Blockly.FieldNumber(0), "NAME");
    this.setInputsInline(false);
    this.setOutput(true, null);
    this.setColour(195);
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
    this.setColour(135);
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
    this.setColour(135);
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
    this.setColour(135);
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
    this.setColour(135);
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
    this.setColour(135);
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
    this.setColour(135);
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
    this.setColour(135);
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
    this.setColour(135);
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
    this.setColour(330);
    this.setTooltip('');
    this.setHelpUrl('');
  }
};


Blockly.Blocks['else_if'] = {
  init: function() {
    this.appendValueInput("if")
        .setCheck(null)
        .appendField("if");
    this.appendStatementInput("ifstate")
        .setCheck(null)
        .appendField("");
    this.appendValueInput("else if")
        .setCheck(null)
        .appendField("else if");
    this.appendStatementInput("elseifstate")
        .setCheck(null);
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(330);
    this.setTooltip('');
    this.setHelpUrl('');
  }
};

Blockly.Blocks['else'] = {
  init: function() {
    this.appendStatementInput("else")
        .setCheck(null)
        .appendField("else");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(330);
    this.setTooltip('');
    this.setHelpUrl('');
  }
};

Blockly.Blocks['while'] = {
  init: function() {
    this.appendValueInput("while")
        .setCheck(null)
        .appendField("while");
    this.appendStatementInput("ifstate")
        .setCheck(null)
        .appendField("");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(330);
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
  var code = dropdown_type + ' ' + text_varname + ' = ' + value_print + '; \n';
  return code;
};


// Blockly.JavaScript['function'] = function(block) {
//   var dropdown_type = block.getFieldValue('type');
//   var text_funcname = block.getFieldValue('funcName');
//   var value_function1 = Blockly.JavaScript.valueToCode(block, 'function1', Blockly.JavaScript.ORDER_ATOMIC);
//   var statements_function2 = Blockly.JavaScript.statementToCode(block, 'function2');
//   // TODO: Assemble JavaScript into code variable.
 
//   var code = 'function ' + dropdown_type + ' ' + text_funcname + ' ' + value_function1 + '' + '{ \n' + statements_function2 + '}   \n \n';
//   code = code.replace(/[()]/g,'');
//   return [code, Blockly.JavaScript.ORDER_NONE];
// };

Blockly.JavaScript['function'] = function(block) {
  var dropdown_functiontype = block.getFieldValue('functionType');
  var text_name = block.getFieldValue('NAME');
  var value_parameters = Blockly.JavaScript.valueToCode(block, 'parameters', Blockly.JavaScript.ORDER_ATOMIC);
  var statements_content = Blockly.JavaScript.statementToCode(block, 'content');
  // TODO: Assemble JavaScript into code variable.
  var code = 'function ' + dropdown_functiontype + ' ' + text_name +
   '¡' + value_parameters + '! {\n' + statements_content + '}\n';
  code = code.replace(/[()]/g,'');
  return code;
};


Blockly.JavaScript['vars3'] = function(block) {
  var dropdown_var = block.getFieldValue('var');
  var text_varname = block.getFieldValue('varName');
  var text_varvalue = block.getFieldValue('varValue');
  var value_var = Blockly.JavaScript.valueToCode(block, 'var', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = dropdown_var + ' ' + text_varname + ' = ' + text_varvalue + value_var + ';\n';
  code = code.replace(/[()]/g,'');
  return [code, Blockly.JavaScript.ORDER_NONE];
};


Blockly.JavaScript['vars4'] = function(block) {
  var text_varname = block.getFieldValue('varName');
  var text_varvalue = block.getFieldValue('varValue');
  var value_var = Blockly.JavaScript.valueToCode(block, 'var', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = ', '+text_varname + ' = ' + text_varvalue + value_var;
  // TODO: Change ORDER_NONE to the correct strength.
  code = code.replace(/[()]/g,'');
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['priomh'] = function(block) {
  var statements_priomh = Blockly.JavaScript.statementToCode(block, 'priomh');
  // TODO: Assemble JavaScript into code variable.
  var code = 'priomh { \n' + statements_priomh + '\n  }';
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
  var code = 'print¡'+value_print + '!;\n';
  code = code.replace(/[()]/g,'');
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
  var code = dropdown_var+' '+text_varname+', ';
  // TODO: Change ORDER_NONE to the correct strength.
 code = code.replace(/[()]/g,'');
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['param2'] = function(block) {
  var dropdown_var = block.getFieldValue('var');
  var text_varname = block.getFieldValue('varName');
  // TODO: Assemble JavaScript into code variable.
  var code = dropdown_var + ' ' + text_varname;
  // TODO: Change ORDER_NONE to the correct strength.
  return code;
};


Blockly.JavaScript['parameter'] = function(block) {
  var dropdown_paramtype = block.getFieldValue('paramType');
  var text_paramvar = block.getFieldValue('paramVar');
  var value_param = Blockly.JavaScript.valueToCode(block, 'param', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  if(value_param == ''){
    var code = dropdown_paramtype + ' ' + text_paramvar;
  }
  else{
    var code = dropdown_paramtype + ' ' + text_paramvar + ', ' + value_param;
  }
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
  code = code.replace(/[()]/g,'');
  return code;
};

Blockly.JavaScript['array'] = function(block) {
  var dropdown_type = block.getFieldValue('type');
  var text_arrayname = block.getFieldValue('arrayName');
  var text_arraysize = block.getFieldValue('arraySize');
  // TODO: Assemble JavaScript into code variable.
  var code = dropdown_type + ' ' + text_arrayname + ' [' + text_arraysize + ']; \n';
  return code;
};

Blockly.JavaScript['arrayparam1'] = function(block) {
  var dropdown_var = block.getFieldValue('var');
  var text_arrayname = block.getFieldValue('arrayName');
  var text_arraysize = block.getFieldValue('arraySize');
  var value_var = Blockly.JavaScript.valueToCode(block, 'var', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = dropdown_var + ' ' + text_arrayname + ' ' + '[' + text_arraysize + '], \n';
  // TODO: Change ORDER_NONE to the correct strength.
  code = code.replace(/[()]/g,'');
  return code;
};



Blockly.JavaScript['arrayparam2'] = function(block) {
  var dropdown_var = block.getFieldValue('var');
  var text_arrayname = block.getFieldValue('arrayName');
  var text_arraysize = block.getFieldValue('arraySize');
  // TODO: Assemble JavaScript into code variable.
  var code = dropdown_var + ' ' + text_arrayname + ' [' + text_arraysize; + '] \n'
  // TODO: Change ORDER_NONE to the correct strength.
  code = code.replace(/[()]/g,'');
  return code;
};

Blockly.JavaScript['text1'] = function(block) {
  var text_name = block.getFieldValue('NAME');
  // TODO: Assemble JavaScript into code variable.
  var code = text_name;
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['funccall1'] = function(block) {
  var text_funcname = block.getFieldValue('funcName');
  var value_var1 = Blockly.JavaScript.valueToCode(block, 'var1', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = text_funcname + '¡' + value_var1 + '!;';
  code = code.replace(/[()]/g,'');
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['funccall2'] = function(block) {
  var text_funcname = block.getFieldValue('funcName');
  var value_func = Blockly.JavaScript.valueToCode(block, 'func', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = text_funcname+'¡'+value_func+'!';
  // TODO: Change ORDER_NONE to the correct strength.
  code = code.replace(/[()]/g,'');
  return [code, Blockly.JavaScript.ORDER_NONE];
};


//....................................................................................................................
//Operaciones 
Blockly.JavaScript['sum'] = function(block) {
  var value_var1 = Blockly.JavaScript.valueToCode(block, 'var1', Blockly.JavaScript.ORDER_ATOMIC);
  var value_var2 = Blockly.JavaScript.valueToCode(block, 'var2', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = value_var1 + '+' + value_var2;
    code = code.replace(/[()]/g,'');
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['sub'] = function(block) {
  var value_var1 = Blockly.JavaScript.valueToCode(block, 'var1', Blockly.JavaScript.ORDER_ATOMIC);
  var value_var2 = Blockly.JavaScript.valueToCode(block, 'var2', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = value_var1 + '-' + value_var2;
    code = code.replace(/[()]/g,'');
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['mult'] = function(block) {
  var value_var1 = Blockly.JavaScript.valueToCode(block, 'var1', Blockly.JavaScript.ORDER_ATOMIC);
  var value_var2 = Blockly.JavaScript.valueToCode(block, 'var2', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = value_var1 + '*' + value_var2;
   code = code.replace(/[()]/g,'');
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['div'] = function(block) {
  var value_var1 = Blockly.JavaScript.valueToCode(block, 'var1', Blockly.JavaScript.ORDER_ATOMIC);
  var value_var2 = Blockly.JavaScript.valueToCode(block, 'var2', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = value_var1 + '/' + value_var2;
  code = code.replace(/[()]/g,'');
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['sum2'] = function(block) {
  var number_var1 = block.getFieldValue('var1');
  var number_name = block.getFieldValue('NAME');
  // TODO: Assemble JavaScript into code variable.
  var code = number_var1 + '+ ' + number_name;
  // TODO: Change ORDER_NONE to the correct strength.
   code = code.replace(/[()]/g,'');
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['sub2'] = function(block) {
  var number_var1 = block.getFieldValue('var1');
  var number_name = block.getFieldValue('NAME');
  // TODO: Assemble JavaScript into code variable.
  var code = number_var1 + '- ' + number_name;
  // TODO: Change ORDER_NONE to the correct strength.
    code = code.replace(/[()]/g,'');
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['mult2'] = function(block) {
  var number_var1 = block.getFieldValue('var1');
  var number_name = block.getFieldValue('NAME');
  // TODO: Assemble JavaScript into code variable.
  var code = number_var1 + '* ' + number_name;
  // TODO: Change ORDER_NONE to the correct strength.
  code = code.replace(/[()]/g,'');
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['div2'] = function(block) {
  var number_var1 = block.getFieldValue('var1');
  var number_name = block.getFieldValue('NAME');
  // TODO: Assemble JavaScript into code variable.
  var code = number_var1 + '/ ' + number_name;
  // TODO: Change ORDER_NONE to the correct strength.
    code = code.replace(/[()]/g,'');
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
   code = code.replace(/[()]/g,'');
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['greaterthan'] = function(block) {
  var value_less1 = Blockly.JavaScript.valueToCode(block, 'var1', Blockly.JavaScript.ORDER_ATOMIC);
  var value_less2 = Blockly.JavaScript.valueToCode(block, 'var2', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = value_less1 + ' > ' + value_less2;
  // TODO: Change ORDER_NONE to the correct strength.
    code = code.replace(/[()]/g,'');
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['equality'] = function(block) {
  var value_less1 = Blockly.JavaScript.valueToCode(block, 'var1', Blockly.JavaScript.ORDER_ATOMIC);
  var value_less2 = Blockly.JavaScript.valueToCode(block, 'var2', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = value_less1 + ' == ' + value_less2;
  // TODO: Change ORDER_NONE to the correct strength.

  code = code.replace(/[()]/g,'');
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['lessthanEquals'] = function(block) {
  var value_less1 = Blockly.JavaScript.valueToCode(block, 'var1', Blockly.JavaScript.ORDER_ATOMIC);
  var value_less2 = Blockly.JavaScript.valueToCode(block, 'var2', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = value_less1 + ' <=' + value_less2;
  // TODO: Change ORDER_NONE to the correct strength.
    code = code.replace(/[()]/g,'');
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['greaterthanEquals'] = function(block) {
  var value_less1 = Blockly.JavaScript.valueToCode(block, 'var1', Blockly.JavaScript.ORDER_ATOMIC);
  var value_less2 = Blockly.JavaScript.valueToCode(block, 'var2', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = value_less1 + ' >=' + value_less2;
  // TODO: Change ORDER_NONE to the correct strength.
    code = code.replace(/[()]/g,'');
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['not'] = function(block) {
  var value_less1 = Blockly.JavaScript.valueToCode(block, 'var1', Blockly.JavaScript.ORDER_ATOMIC);
  var value_less2 = Blockly.JavaScript.valueToCode(block, 'var2', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = value_less1 + ' !=' + value_less2;
  // TODO: Change ORDER_NONE to the correct strength.
  code = code.replace(/[()]/g,'');
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['or'] = function(block) {
  var value_less1 = Blockly.JavaScript.valueToCode(block, 'var1', Blockly.JavaScript.ORDER_ATOMIC);
  var value_less2 = Blockly.JavaScript.valueToCode(block, 'var2', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = value_less1 + ' ||' + value_less2;
  // TODO: Change ORDER_NONE to the correct strength.
   code = code.replace(/[()]/g,'');
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['and'] = function(block) {
  var value_less1 = Blockly.JavaScript.valueToCode(block, 'var1', Blockly.JavaScript.ORDER_ATOMIC);
  var value_less2 = Blockly.JavaScript.valueToCode(block, 'var2', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = value_less1 + ' &&' + value_less2;
  // TODO: Change ORDER_NONE to the correct strength.
   code = code.replace(/[()]/g,'');
  return [code, Blockly.JavaScript.ORDER_NONE];
};
//....................................................................................................................
//Ciclos y Condiciones
Blockly.JavaScript['if'] = function(block) {
  var value_var = Blockly.JavaScript.valueToCode(block, 'var', Blockly.JavaScript.ORDER_ATOMIC);
  var statements_name = Blockly.JavaScript.statementToCode(block, 'NAME');
  // TODO: Assemble JavaScript into code variable.
  var code = 'if ¡' + value_var + '!{ \n' + statements_name + '\n }';
  code = code.replace(/[()]/g,'');
  return code;
};


Blockly.JavaScript['else_if'] = function(block) {
  var value_if = Blockly.JavaScript.valueToCode(block, 'if', Blockly.JavaScript.ORDER_ATOMIC);
  var statements_ifstate = Blockly.JavaScript.statementToCode(block, 'ifstate');
  var value_else_if = Blockly.JavaScript.valueToCode(block, 'else if', Blockly.JavaScript.ORDER_ATOMIC);
  var statements_elseifstate = Blockly.JavaScript.statementToCode(block, 'elseifstate');
  // TODO: Assemble JavaScript into code variable.
  var code = 'if¡' + value_if +'!{ \n' + statements_ifstate + '\n } \n' + 'elseif¡' + value_else_if +'!{ \n' + statements_elseifstate + '\n }\n' ;
  code = code.replace(/[()]/g,'');
  return code;
};

Blockly.JavaScript['else'] = function(block) {
  var statements_else = Blockly.JavaScript.statementToCode(block, 'else');
  // TODO: Assemble JavaScript into code variable.
  var code = 'else{\n ' + statements_else + ' \n } \n';
  return code;
};

Blockly.JavaScript['while'] = function(block) {
  var value_while = Blockly.JavaScript.valueToCode(block, 'while', Blockly.JavaScript.ORDER_ATOMIC);
  var statements_ifstate = Blockly.JavaScript.statementToCode(block, 'ifstate');
  // TODO: Assemble JavaScript into code variable.
  var code = 'while¡' + value_while + '!{ \n' + statements_ifstate + '\n } \n';
  code = code.replace(/[()]/g,'');
  return code;
};
