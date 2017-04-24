
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'LFTBRAC RGTBRAC LFTPAREN RGTPAREN LFTBRACSQR RGTBRACSQR AND DOUBEQUAL NOT OR SEMICOLON EQUAL LESSTHANEQUAL GREATTHANEQUAL GREATTHAN LESSTHAN PLUS MINUS MULTIPLICATION DIVISION ID COMMA FUNCTION INT FALSE STRING READ VOID FLOAT PRIOMH CHAR PRINT WHILE PROGRAM BOOL ELSEIF RETURN ELSE TRUE IFprogram : PROGRAM ID LFTBRAC auxprogramvars codeGOTOMain auxprogramfunct main RGTBRACauxprogramvars : vars auxprogramvars \n    | empty auxprogramfunct : function auxprogramfunct \n    | empty array : ID LFTBRACSQR exp RGTBRACSQRarrayvals : LFTBRACSQR arrayvalsaux RGTBRACSQR arrayvalsaux : cteNcteS codeAddValueArray \n    | cteNcteS codeAddValueArray COMMA arrayvalsaux cteNcteS : cteN  \n    | cteSassignment : assignmentaux EQUAL expression SEMICOLONassignmentaux : ID \n    | arrayblockreturn : LFTBRAC blockneutral RGTBRAC \n    | LFTBRAC blockneutral RETURN exp codeReturnQuad SEMICOLON RGTBRAC blockneutral : statement blockneutral \n    | vars blockneutral\n    | empty block : LFTBRAC blockneutral RGTBRACcondition : IF conditionaux codeEndIf\n    | IF conditionaux ELSE codeElse block  codeEndIfconditionaux : LFTPAREN expression RGTPAREN codeGOTOF block codeGotoElseIf conditionaux2 conditionaux2 : codeNextIf ELSEIF conditionaux\n    | empty constant : ID \n    | array \n    | cteN\n    | cteS\n    | TRUE codeAddConstBool\n    | FALSE codeAddConstBool\n    | call codeIsCalll cteN : FLOAT codeAddConstNumber\n    | INT codeAddConstNumbercteS : STRING codeAddConstStringexp : term\n    | term PLUS codeAddOperator exp\n    | term MINUS codeAddOperator exp  factoraux : constant\n    | PLUS constant\n    | MINUS constant factor : LFTPAREN codeAddOpenParen expression RGTPAREN codeDeleteOpenParen codeAskFactor\n    | factoraux codeAskFactorexpression : exp \n    | exp expressionaux codeAddOperator exp codeAskExpressionexpressionaux : AND \n    | DOUBEQUAL \n    | NOT \n    | OR \n    | LESSTHANEQUAL \n    | GREATTHANEQUAL \n    | GREATTHAN \n    | LESSTHAN loop : WHILE codeWhileCondition LFTPAREN expression RGTPAREN codeGOTOF block codeGOTOWhile write : PRINT LFTPAREN constant RGTPAREN SEMICOLON parameter : type codeCheckType ID codeAddParameters\n    | type codeCheckType ID codeAddParameters COMMA parameter \n    | empty  term : factor MULTIPLICATION codeAddOperator term\n    | factor DIVISION codeAddOperator term \n    | factor codeAskTerm statement : assignment \n    | condition \n    | loop \n    | write \n    | read \n    | call SEMICOLON type : INT  \n    | FLOAT \n    | CHAR \n    | BOOL \n    | STRING   main : codeLocationMain PRIOMH codeScope block  function : FUNCTION codeScope functionaux ID codeNameOfFunct LFTPAREN parameter RGTPAREN codeAddFunctQuad blockreturn codeScope  functionaux : VOID codeTypeVoid codeCheckType \n    | codeFuncIndicator type codeCheckType vars : type codeCheckType varsaux     varsaux2 : COMMA varsaux \n    |  SEMICOLON  varsaux : ID codeAddVar EQUAL expression varsaux2 \n    | ID  codeAddVarArreglo LFTBRACSQR INT RGTBRACSQR EQUAL arrayvals varsaux2 callaux : codeMovePointer COMMA exp codeAddArguments callaux\n    | empty call : ID codeVerifyFunct LFTPAREN codeEraQuad exp codeAddArguments callaux RGTPAREN codeVerifyNull codeGOSUB codeTempReturn  read : READ LFTPAREN readaux RGTPAREN SEMICOLON readaux : ID\n    | array empty : codeGotoElseIf : codeAddValueArray : emptycodeTempReturn : emptycodeIsCalll : emptycodeGOSUB : emptycodeVerifyNull : emptycodeVerifyNull2 : emptycodeMovePointer : emptycodeAddArguments : emptycodeEraQuad : emptycodeVerifyFunct : emptycodeReturnQuad : codeAddFunctQuad : codeLocationMain : codeGOTOMain : codeElse : codeEndIf : codeNextIf : codeGOTOF : codeGOTOWhile : codeWhileCondition : codeScope : codeCheckType : codeAddVar : codeAddVarArreglo : codeAddParameters : codeNameOfFunct : codeTypeVoid : codeFuncIndicator : codeDeleteOpenParen : emptycodeAddOpenParen : emptycodeAddConstBool : emptycodeAddConstString : emptycodeAddConstNumber : emptycodeAddOperator : emptycodeAskTerm : emptycodeAskFactor : emptycodeAskExpression : empty'
    
_lr_action_items = {'RGTPAREN':([41,42,43,44,46,48,49,50,51,53,54,55,56,57,58,66,67,68,69,70,71,73,75,76,77,78,79,87,88,89,90,103,125,133,134,147,148,149,152,153,154,155,158,159,160,161,164,172,173,174,175,176,177,181,188,189,190,191,200,202,203,210,212,217,218,219,225,226,227,230,231,232,],[-39,-88,-27,-28,-88,-88,-88,-88,-29,-26,-36,-88,-88,-88,-44,-43,-125,-41,-30,-120,-40,-61,-124,-92,-32,-35,-121,-31,-34,-122,-33,-88,149,157,-58,-60,-59,-88,-6,-37,-38,-88,179,-87,-86,180,183,-88,-118,-88,-126,-45,-114,196,-42,-88,-97,-56,210,-83,-88,-88,-57,-88,-94,-88,-88,-93,-88,-84,-91,-82,]),'RETURN':([22,100,101,104,109,110,112,113,114,117,120,131,135,139,140,143,144,166,171,182,192,194,195,198,204,207,208,215,216,221,222,224,234,],[-77,-79,-80,-88,-65,-66,-19,-88,-62,-63,-64,-78,-18,-67,-17,-105,-20,-21,-81,-12,-88,-85,-55,-105,213,-89,-22,-108,-88,-54,-23,-25,-24,]),'READ':([22,63,100,101,104,109,110,113,114,117,120,131,139,143,144,166,171,182,192,194,195,198,207,208,215,216,221,222,224,234,],[-77,105,-79,-80,105,-65,-66,105,-62,-63,-64,-78,-67,-105,-20,-21,-81,-12,105,-85,-55,-105,-89,-22,-108,-88,-54,-23,-25,-24,]),'VOID':([18,24,],[-110,31,]),'EQUAL':([21,28,65,108,115,116,152,],[-112,35,121,-14,141,-13,-6,]),'CHAR':([4,6,18,22,24,30,63,100,101,103,104,109,110,113,114,117,120,131,139,143,144,166,171,182,192,194,195,198,203,207,208,215,216,221,222,224,234,],[9,9,-110,-77,-117,9,9,-79,-80,9,9,-65,-66,9,-62,-63,-64,-78,-67,-105,-20,-21,-81,-12,9,-85,-55,-105,9,-89,-22,-108,-88,-54,-23,-25,-24,]),'MULTIPLICATION':([41,42,43,44,46,48,49,50,51,53,55,56,57,66,67,68,69,70,71,76,77,78,79,87,88,89,90,149,152,172,173,188,210,217,218,225,226,230,231,],[-39,-88,-27,-28,-88,74,-88,-88,-29,-26,-88,-88,-88,-43,-125,-41,-30,-120,-40,-92,-32,-35,-121,-31,-34,-122,-33,-88,-6,-88,-118,-42,-88,-88,-94,-88,-93,-84,-91,]),'WHILE':([22,63,100,101,104,109,110,113,114,117,120,131,139,143,144,166,171,182,192,194,195,198,207,208,215,216,221,222,224,234,],[-77,107,-79,-80,107,-65,-66,107,-62,-63,-64,-78,-67,-105,-20,-21,-81,-12,107,-85,-55,-105,-89,-22,-108,-88,-54,-23,-25,-24,]),'PROGRAM':([0,],[2,]),'PRINT':([22,63,100,101,104,109,110,113,114,117,120,131,139,143,144,166,171,182,192,194,195,198,207,208,215,216,221,222,224,234,],[-77,106,-79,-80,106,-65,-66,106,-62,-63,-64,-78,-67,-105,-20,-21,-81,-12,106,-85,-55,-105,-89,-22,-108,-88,-54,-23,-25,-24,]),'RGTBRACSQR':([40,41,42,43,44,46,48,49,50,51,53,54,55,56,57,66,67,68,69,70,71,73,75,76,77,78,79,87,88,89,90,127,147,148,149,152,153,154,167,168,169,170,172,173,185,186,188,209,210,217,218,225,226,230,231,],[65,-39,-88,-27,-28,-88,-88,-88,-88,-29,-26,-36,-88,-88,-88,-43,-125,-41,-30,-120,-40,-61,-124,-92,-32,-35,-121,-31,-34,-122,-33,152,-60,-59,-88,-6,-37,-38,-11,-88,-10,187,-88,-118,-8,-90,-42,-9,-88,-88,-94,-88,-93,-84,-91,]),'TRUE':([35,45,47,52,72,74,80,81,83,85,86,91,92,93,94,95,96,97,98,99,122,123,124,126,128,129,130,137,141,142,150,151,162,211,213,],[46,46,46,-88,-88,-88,46,-119,46,-88,-88,-46,-88,-51,-52,-50,-53,-48,-47,-49,46,-123,46,-88,46,46,46,46,46,46,46,-98,46,46,46,]),'MINUS':([35,41,42,43,44,46,48,49,50,51,52,53,54,55,56,57,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,83,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,122,123,124,126,128,129,130,141,142,147,148,149,150,151,152,162,172,173,188,210,211,213,217,218,225,226,230,231,],[45,-39,-88,-27,-28,-88,-88,-88,-88,-29,-88,-26,86,-88,-88,-88,-43,-125,-41,-30,-120,-40,-88,-61,-88,-124,-92,-32,-35,-121,45,-119,45,-88,-88,-31,-34,-122,-33,-46,-88,-51,-52,-50,-53,-48,-47,-49,45,-123,45,-88,45,45,45,45,45,-60,-59,-88,45,-98,-6,45,-88,-118,-42,-88,45,45,-88,-94,-88,-93,-84,-91,]),'SEMICOLON':([41,42,43,44,46,48,49,50,51,53,54,55,56,57,58,59,66,67,68,69,70,71,73,75,76,77,78,79,87,88,89,90,111,146,147,148,149,152,153,154,155,163,172,173,175,176,179,180,187,188,210,217,218,220,225,226,228,230,231,],[-39,-88,-27,-28,-88,-88,-88,-88,-29,-26,-36,-88,-88,-88,-44,100,-43,-125,-41,-30,-120,-40,-61,-124,-92,-32,-35,-121,-31,-34,-122,-33,139,100,-60,-59,-88,-6,-37,-38,-88,182,-88,-118,-126,-45,194,195,-7,-42,-88,-88,-94,-100,-88,-93,233,-84,-91,]),'GREATTHAN':([41,42,43,44,46,48,49,50,51,53,54,55,56,57,58,66,67,68,69,70,71,73,75,76,77,78,79,87,88,89,90,147,148,149,152,153,154,172,173,188,210,217,218,225,226,230,231,],[-39,-88,-27,-28,-88,-88,-88,-88,-29,-26,-36,-88,-88,-88,94,-43,-125,-41,-30,-120,-40,-61,-124,-92,-32,-35,-121,-31,-34,-122,-33,-60,-59,-88,-6,-37,-38,-88,-118,-42,-88,-88,-94,-88,-93,-84,-91,]),'LESSTHANEQUAL':([41,42,43,44,46,48,49,50,51,53,54,55,56,57,58,66,67,68,69,70,71,73,75,76,77,78,79,87,88,89,90,147,148,149,152,153,154,172,173,188,210,217,218,225,226,230,231,],[-39,-88,-27,-28,-88,-88,-88,-88,-29,-26,-36,-88,-88,-88,95,-43,-125,-41,-30,-120,-40,-61,-124,-92,-32,-35,-121,-31,-34,-122,-33,-60,-59,-88,-6,-37,-38,-88,-118,-42,-88,-88,-94,-88,-93,-84,-91,]),'LFTBRACSQR':([21,27,53,116,121,160,],[-113,34,83,83,145,83,]),'PLUS':([35,41,42,43,44,46,48,49,50,51,52,53,54,55,56,57,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,83,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,122,123,124,126,128,129,130,141,142,147,148,149,150,151,152,162,172,173,188,210,211,213,217,218,225,226,230,231,],[47,-39,-88,-27,-28,-88,-88,-88,-88,-29,-88,-26,85,-88,-88,-88,-43,-125,-41,-30,-120,-40,-88,-61,-88,-124,-92,-32,-35,-121,47,-119,47,-88,-88,-31,-34,-122,-33,-46,-88,-51,-52,-50,-53,-48,-47,-49,47,-123,47,-88,47,47,47,47,47,-60,-59,-88,47,-98,-6,47,-88,-118,-42,-88,47,47,-88,-94,-88,-93,-84,-91,]),'COMMA':([41,42,43,44,46,48,49,50,51,53,54,55,56,57,58,59,66,67,68,69,70,71,73,75,76,77,78,79,87,88,89,90,146,147,148,149,152,153,154,155,167,168,169,172,173,174,175,176,177,185,186,187,188,189,190,191,201,202,210,217,218,219,225,226,227,230,231,],[-39,-88,-27,-28,-88,-88,-88,-88,-29,-26,-36,-88,-88,-88,-44,102,-43,-125,-41,-30,-120,-40,-61,-124,-92,-32,-35,-121,-31,-34,-122,-33,102,-60,-59,-88,-6,-37,-38,-88,-11,-88,-10,-88,-118,-88,-126,-45,-114,199,-90,-7,-42,-88,-97,203,211,-96,-88,-88,-94,-88,-88,-93,-88,-84,-91,]),'$end':([1,32,],[0,-1,]),'FUNCTION':([4,5,6,13,14,15,17,22,100,101,131,171,193,205,214,235,],[-88,-103,-88,-3,18,-2,18,-77,-79,-80,-78,-81,-110,-74,-15,-16,]),'DIVISION':([41,42,43,44,46,48,49,50,51,53,55,56,57,66,67,68,69,70,71,76,77,78,79,87,88,89,90,149,152,172,173,188,210,217,218,225,226,230,231,],[-39,-88,-27,-28,-88,72,-88,-88,-29,-26,-88,-88,-88,-43,-125,-41,-30,-120,-40,-92,-32,-35,-121,-31,-34,-122,-33,-88,-6,-88,-118,-42,-88,-88,-94,-88,-93,-84,-91,]),'STRING':([4,6,18,22,24,30,35,45,47,52,63,72,74,80,81,83,85,86,91,92,93,94,95,96,97,98,99,100,101,103,104,109,110,113,114,117,120,122,123,124,126,128,129,130,131,137,139,141,142,143,144,145,150,151,162,166,171,182,192,194,195,198,199,203,207,208,211,213,215,216,221,222,224,234,],[11,11,-110,-77,-117,11,50,50,50,-88,11,-88,-88,50,-119,50,-88,-88,-46,-88,-51,-52,-50,-53,-48,-47,-49,-79,-80,11,11,-65,-66,11,-62,-63,-64,50,-123,50,-88,50,50,50,-78,50,-67,50,50,-105,-20,50,50,-98,50,-21,-81,-12,11,-85,-55,-105,50,11,-89,-22,50,50,-108,-88,-54,-23,-25,-24,]),'RGTBRAC':([22,25,63,64,100,101,104,109,110,112,113,114,117,119,120,131,135,139,140,143,144,166,171,182,192,194,195,198,204,207,208,215,216,221,222,224,233,234,],[-77,32,-88,-73,-79,-80,-88,-65,-66,-19,-88,-62,-63,144,-64,-78,-18,-67,-17,-105,-20,-21,-81,-12,-88,-85,-55,-105,214,-89,-22,-108,-88,-54,-23,-25,235,-24,]),'LFTPAREN':([35,36,52,53,60,72,74,80,81,82,83,84,85,86,91,92,93,94,95,96,97,98,99,105,106,107,116,118,122,123,124,126,128,129,130,138,141,142,150,151,162,211,213,229,],[52,-115,-88,-88,103,-88,-88,52,-119,126,52,-99,-88,-88,-46,-88,-51,-52,-50,-53,-48,-47,-49,136,137,-109,-88,142,52,-123,52,-88,52,52,52,162,52,52,52,-98,52,52,52,142,]),'ELSE':([143,144,207,216,222,224,234,],[165,-20,-89,-88,-23,-25,-24,]),'ELSEIF':([144,207,216,223,],[-20,-89,-106,229,]),'GREATTHANEQUAL':([41,42,43,44,46,48,49,50,51,53,54,55,56,57,58,66,67,68,69,70,71,73,75,76,77,78,79,87,88,89,90,147,148,149,152,153,154,172,173,188,210,217,218,225,226,230,231,],[-39,-88,-27,-28,-88,-88,-88,-88,-29,-26,-36,-88,-88,-88,93,-43,-125,-41,-30,-120,-40,-61,-124,-92,-32,-35,-121,-31,-34,-122,-33,-60,-59,-88,-6,-37,-38,-88,-118,-42,-88,-88,-94,-88,-93,-84,-91,]),'DOUBEQUAL':([41,42,43,44,46,48,49,50,51,53,54,55,56,57,58,66,67,68,69,70,71,73,75,76,77,78,79,87,88,89,90,147,148,149,152,153,154,172,173,188,210,217,218,225,226,230,231,],[-39,-88,-27,-28,-88,-88,-88,-88,-29,-26,-36,-88,-88,-88,98,-43,-125,-41,-30,-120,-40,-61,-124,-92,-32,-35,-121,-31,-34,-122,-33,-60,-59,-88,-6,-37,-38,-88,-118,-42,-88,-88,-94,-88,-93,-84,-91,]),'ID':([2,7,8,9,10,11,12,16,22,29,31,35,37,38,45,47,52,61,62,63,72,74,80,81,83,85,86,91,92,93,94,95,96,97,98,99,100,101,102,104,109,110,113,114,117,120,122,123,124,126,128,129,130,131,132,136,137,139,141,142,143,144,150,151,156,162,166,171,182,192,194,195,198,207,208,211,213,215,216,221,222,224,234,],[3,-69,-68,-70,-71,-72,-111,21,-77,36,-116,53,-111,-111,53,53,-88,-76,-75,116,-88,-88,53,-119,53,-88,-88,-46,-88,-51,-52,-50,-53,-48,-47,-49,-79,-80,21,116,-65,-66,116,-62,-63,-64,53,-123,53,-88,53,53,53,-78,-111,160,53,-67,53,53,-105,-20,53,-98,177,53,-21,-81,-12,116,-85,-55,-105,-89,-22,53,53,-108,-88,-54,-23,-25,-24,]),'IF':([22,63,100,101,104,109,110,113,114,117,120,131,139,143,144,166,171,182,192,194,195,198,207,208,215,216,221,222,224,234,],[-77,118,-79,-80,118,-65,-66,118,-62,-63,-64,-78,-67,-105,-20,-21,-81,-12,118,-85,-55,-105,-89,-22,-108,-88,-54,-23,-25,-24,]),'AND':([41,42,43,44,46,48,49,50,51,53,54,55,56,57,58,66,67,68,69,70,71,73,75,76,77,78,79,87,88,89,90,147,148,149,152,153,154,172,173,188,210,217,218,225,226,230,231,],[-39,-88,-27,-28,-88,-88,-88,-88,-29,-26,-36,-88,-88,-88,91,-43,-125,-41,-30,-120,-40,-61,-124,-92,-32,-35,-121,-31,-34,-122,-33,-60,-59,-88,-6,-37,-38,-88,-118,-42,-88,-88,-94,-88,-93,-84,-91,]),'FALSE':([35,45,47,52,72,74,80,81,83,85,86,91,92,93,94,95,96,97,98,99,122,123,124,126,128,129,130,137,141,142,150,151,162,211,213,],[55,55,55,-88,-88,-88,55,-119,55,-88,-88,-46,-88,-51,-52,-50,-53,-48,-47,-49,55,-123,55,-88,55,55,55,55,55,55,55,-98,55,55,55,]),'LFTBRAC':([3,33,39,157,165,178,183,184,196,197,206,],[4,-110,63,-101,-104,192,-107,63,-107,63,63,]),'INT':([4,6,18,22,24,30,34,35,45,47,52,63,72,74,80,81,83,85,86,91,92,93,94,95,96,97,98,99,100,101,103,104,109,110,113,114,117,120,122,123,124,126,128,129,130,131,137,139,141,142,143,144,145,150,151,162,166,171,182,192,194,195,198,199,203,207,208,211,213,215,216,221,222,224,234,],[8,8,-110,-77,-117,8,40,56,56,56,-88,8,-88,-88,56,-119,56,-88,-88,-46,-88,-51,-52,-50,-53,-48,-47,-49,-79,-80,8,8,-65,-66,8,-62,-63,-64,56,-123,56,-88,56,56,56,-78,56,-67,56,56,-105,-20,56,56,-98,56,-21,-81,-12,8,-85,-55,-105,56,8,-89,-22,56,56,-108,-88,-54,-23,-25,-24,]),'FLOAT':([4,6,18,22,24,30,35,45,47,52,63,72,74,80,81,83,85,86,91,92,93,94,95,96,97,98,99,100,101,103,104,109,110,113,114,117,120,122,123,124,126,128,129,130,131,137,139,141,142,143,144,145,150,151,162,166,171,182,192,194,195,198,199,203,207,208,211,213,215,216,221,222,224,234,],[7,7,-110,-77,-117,7,57,57,57,-88,7,-88,-88,57,-119,57,-88,-88,-46,-88,-51,-52,-50,-53,-48,-47,-49,-79,-80,7,7,-65,-66,7,-62,-63,-64,57,-123,57,-88,57,57,57,-78,57,-67,57,57,-105,-20,57,57,-98,57,-21,-81,-12,7,-85,-55,-105,57,7,-89,-22,57,57,-108,-88,-54,-23,-25,-24,]),'LESSTHAN':([41,42,43,44,46,48,49,50,51,53,54,55,56,57,58,66,67,68,69,70,71,73,75,76,77,78,79,87,88,89,90,147,148,149,152,153,154,172,173,188,210,217,218,225,226,230,231,],[-39,-88,-27,-28,-88,-88,-88,-88,-29,-26,-36,-88,-88,-88,96,-43,-125,-41,-30,-120,-40,-61,-124,-92,-32,-35,-121,-31,-34,-122,-33,-60,-59,-88,-6,-37,-38,-88,-118,-42,-88,-88,-94,-88,-93,-84,-91,]),'PRIOMH':([4,5,6,13,14,15,17,19,20,22,23,26,100,101,131,171,193,205,214,235,],[-88,-103,-88,-3,-88,-2,-88,-102,-5,-77,-4,33,-79,-80,-78,-81,-110,-74,-15,-16,]),'BOOL':([4,6,18,22,24,30,63,100,101,103,104,109,110,113,114,117,120,131,139,143,144,166,171,182,192,194,195,198,203,207,208,215,216,221,222,224,234,],[10,10,-110,-77,-117,10,10,-79,-80,10,10,-65,-66,10,-62,-63,-64,-78,-67,-105,-20,-21,-81,-12,10,-85,-55,-105,10,-89,-22,-108,-88,-54,-23,-25,-24,]),'NOT':([41,42,43,44,46,48,49,50,51,53,54,55,56,57,58,66,67,68,69,70,71,73,75,76,77,78,79,87,88,89,90,147,148,149,152,153,154,172,173,188,210,217,218,225,226,230,231,],[-39,-88,-27,-28,-88,-88,-88,-88,-29,-26,-36,-88,-88,-88,97,-43,-125,-41,-30,-120,-40,-61,-124,-92,-32,-35,-121,-31,-34,-122,-33,-60,-59,-88,-6,-37,-38,-88,-118,-42,-88,-88,-94,-88,-93,-84,-91,]),'OR':([41,42,43,44,46,48,49,50,51,53,54,55,56,57,58,66,67,68,69,70,71,73,75,76,77,78,79,87,88,89,90,147,148,149,152,153,154,172,173,188,210,217,218,225,226,230,231,],[-39,-88,-27,-28,-88,-88,-88,-88,-29,-26,-36,-88,-88,-88,99,-43,-125,-41,-30,-120,-40,-61,-124,-92,-32,-35,-121,-31,-34,-122,-33,-60,-59,-88,-6,-37,-38,-88,-118,-42,-88,-88,-94,-88,-93,-84,-91,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'cteS':([35,45,47,80,83,122,124,128,129,130,137,141,142,145,150,162,199,211,213,],[51,51,51,51,51,51,51,51,51,51,51,51,51,167,51,51,167,51,51,]),'constant':([35,45,47,80,83,122,124,128,129,130,137,141,142,150,162,211,213,],[41,68,71,41,41,41,41,41,41,41,161,41,41,41,41,41,41,]),'vars':([4,6,63,104,113,192,],[6,6,104,104,104,104,]),'expressionaux':([58,],[92,]),'codeGOTOMain':([5,],[14,]),'codeGOSUB':([217,],[225,]),'codeNameOfFunct':([36,],[60,]),'codeDeleteOpenParen':([149,],[172,]),'codeAddConstBool':([46,55,],[69,87,]),'codeReturnQuad':([220,],[228,]),'codeGOTOF':([183,196,],[197,206,]),'factoraux':([35,80,83,122,124,128,129,130,141,142,150,162,211,213,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'codeAddParameters':([177,],[191,]),'array':([35,45,47,63,80,83,104,113,122,124,128,129,130,136,137,141,142,150,162,192,211,213,],[43,43,43,108,43,43,108,108,43,43,43,43,43,159,43,43,43,43,43,108,43,43,]),'codeWhileCondition':([107,],[138,]),'cteN':([35,45,47,80,83,122,124,128,129,130,137,141,142,145,150,162,199,211,213,],[44,44,44,44,44,44,44,44,44,44,44,44,44,169,44,44,169,44,44,]),'codeFuncIndicator':([24,],[30,]),'arrayvals':([121,],[146,]),'codeAskExpression':([155,],[176,]),'codeMovePointer':([189,227,],[201,201,]),'codeAddArguments':([174,219,],[189,227,]),'codeAskTerm':([48,],[73,]),'arrayvalsaux':([145,199,],[170,209,]),'auxprogramvars':([4,6,],[5,15,]),'functionaux':([24,],[29,]),'codeAddConstNumber':([56,57,],[88,90,]),'codeNextIf':([216,],[223,]),'write':([63,104,113,192,],[109,109,109,109,]),'program':([0,],[1,]),'call':([35,45,47,63,80,83,104,113,122,124,128,129,130,137,141,142,150,162,192,211,213,],[49,49,49,111,49,49,111,111,49,49,49,49,49,49,49,49,49,49,111,49,49,]),'statement':([63,104,113,192,],[113,113,113,113,]),'factor':([35,80,83,122,124,128,129,130,141,142,150,162,211,213,],[48,48,48,48,48,48,48,48,48,48,48,48,48,48,]),'codeAskFactor':([42,172,],[66,188,]),'main':([19,],[25,]),'type':([4,6,30,63,103,104,113,192,203,],[12,12,37,12,132,12,12,12,132,]),'codeAddVar':([21,],[28,]),'empty':([4,6,14,17,42,46,48,49,50,52,53,55,56,57,63,72,74,85,86,92,103,104,113,116,126,149,155,168,172,174,189,192,203,210,216,217,219,225,227,],[13,13,20,20,67,70,75,76,79,81,84,70,89,89,112,123,123,123,123,123,134,112,112,84,151,173,175,186,67,190,202,112,134,218,224,226,190,231,202,]),'codeEndIf':([143,198,],[166,208,]),'function':([14,17,],[17,17,]),'codeTypeVoid':([31,],[38,]),'codeElse':([165,],[184,]),'codeLocationMain':([19,],[26,]),'codeAddValueArray':([168,],[185,]),'read':([63,104,113,192,],[110,110,110,110,]),'assignment':([63,104,113,192,],[114,114,114,114,]),'codeAddVarArreglo':([21,],[27,]),'codeAddOpenParen':([52,],[80,]),'callaux':([189,227,],[200,232,]),'readaux':([136,],[158,]),'varsaux2':([59,146,],[101,171,]),'codeGOTOWhile':([215,],[221,]),'codeGotoElseIf':([207,],[216,]),'cteNcteS':([145,199,],[168,168,]),'codeAddOperator':([72,74,85,86,92,],[122,124,128,129,130,]),'parameter':([103,203,],[133,212,]),'condition':([63,104,113,192,],[117,117,117,117,]),'codeVerifyNull':([210,],[217,]),'codeScope':([18,33,193,],[24,39,205,]),'codeTempReturn':([225,],[230,]),'term':([35,80,83,122,124,128,129,130,141,142,150,162,211,213,],[54,54,54,147,148,54,54,54,54,54,54,54,54,54,]),'conditionaux2':([216,],[222,]),'codeEraQuad':([126,],[150,]),'codeCheckType':([12,37,38,132,],[16,61,62,156,]),'codeVerifyFunct':([53,116,],[82,82,]),'codeAddFunctQuad':([157,],[178,]),'assignmentaux':([63,104,113,192,],[115,115,115,115,]),'codeIsCalll':([49,],[77,]),'blockneutral':([63,104,113,192,],[119,135,140,204,]),'blockreturn':([178,],[193,]),'auxprogramfunct':([14,17,],[19,23,]),'codeAddConstString':([50,],[78,]),'loop':([63,104,113,192,],[120,120,120,120,]),'exp':([35,80,83,128,129,130,141,142,150,162,211,213,],[58,58,127,153,154,155,58,58,174,58,219,220,]),'conditionaux':([118,229,],[143,234,]),'expression':([35,80,141,142,162,],[59,125,163,164,181,]),'block':([39,184,197,206,],[64,198,207,215,]),'varsaux':([16,102,],[22,131,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID LFTBRAC auxprogramvars codeGOTOMain auxprogramfunct main RGTBRAC','program',8,'p_program','Yaotecatl.py',87),
  ('auxprogramvars -> vars auxprogramvars','auxprogramvars',2,'p_auxprogramvars','Yaotecatl.py',124),
  ('auxprogramvars -> empty','auxprogramvars',1,'p_auxprogramvars','Yaotecatl.py',125),
  ('auxprogramfunct -> function auxprogramfunct','auxprogramfunct',2,'p_auxprogramfunct','Yaotecatl.py',127),
  ('auxprogramfunct -> empty','auxprogramfunct',1,'p_auxprogramfunct','Yaotecatl.py',128),
  ('array -> ID LFTBRACSQR exp RGTBRACSQR','array',4,'p_array','Yaotecatl.py',132),
  ('arrayvals -> LFTBRACSQR arrayvalsaux RGTBRACSQR','arrayvals',3,'p_arrayvals','Yaotecatl.py',184),
  ('arrayvalsaux -> cteNcteS codeAddValueArray','arrayvalsaux',2,'p_arrayvalsaux','Yaotecatl.py',187),
  ('arrayvalsaux -> cteNcteS codeAddValueArray COMMA arrayvalsaux','arrayvalsaux',4,'p_arrayvalsaux','Yaotecatl.py',188),
  ('cteNcteS -> cteN','cteNcteS',1,'p_cteNcteS','Yaotecatl.py',191),
  ('cteNcteS -> cteS','cteNcteS',1,'p_cteNcteS','Yaotecatl.py',192),
  ('assignment -> assignmentaux EQUAL expression SEMICOLON','assignment',4,'p_assignment','Yaotecatl.py',200),
  ('assignmentaux -> ID','assignmentaux',1,'p_assignmentaux','Yaotecatl.py',238),
  ('assignmentaux -> array','assignmentaux',1,'p_assignmentaux','Yaotecatl.py',239),
  ('blockreturn -> LFTBRAC blockneutral RGTBRAC','blockreturn',3,'p_blockreturn','Yaotecatl.py',245),
  ('blockreturn -> LFTBRAC blockneutral RETURN exp codeReturnQuad SEMICOLON RGTBRAC','blockreturn',7,'p_blockreturn','Yaotecatl.py',246),
  ('blockneutral -> statement blockneutral','blockneutral',2,'p_blockneutral','Yaotecatl.py',248),
  ('blockneutral -> vars blockneutral','blockneutral',2,'p_blockneutral','Yaotecatl.py',249),
  ('blockneutral -> empty','blockneutral',1,'p_blockneutral','Yaotecatl.py',250),
  ('block -> LFTBRAC blockneutral RGTBRAC','block',3,'p_block','Yaotecatl.py',252),
  ('condition -> IF conditionaux codeEndIf','condition',3,'p_condition','Yaotecatl.py',255),
  ('condition -> IF conditionaux ELSE codeElse block codeEndIf','condition',6,'p_condition','Yaotecatl.py',256),
  ('conditionaux -> LFTPAREN expression RGTPAREN codeGOTOF block codeGotoElseIf conditionaux2','conditionaux',7,'p_conditionaux','Yaotecatl.py',258),
  ('conditionaux2 -> codeNextIf ELSEIF conditionaux','conditionaux2',3,'p_conditionaux2','Yaotecatl.py',260),
  ('conditionaux2 -> empty','conditionaux2',1,'p_conditionaux2','Yaotecatl.py',261),
  ('constant -> ID','constant',1,'p_constant','Yaotecatl.py',265),
  ('constant -> array','constant',1,'p_constant','Yaotecatl.py',266),
  ('constant -> cteN','constant',1,'p_constant','Yaotecatl.py',267),
  ('constant -> cteS','constant',1,'p_constant','Yaotecatl.py',268),
  ('constant -> TRUE codeAddConstBool','constant',2,'p_constant','Yaotecatl.py',269),
  ('constant -> FALSE codeAddConstBool','constant',2,'p_constant','Yaotecatl.py',270),
  ('constant -> call codeIsCalll','constant',2,'p_constant','Yaotecatl.py',271),
  ('cteN -> FLOAT codeAddConstNumber','cteN',2,'p_cteN','Yaotecatl.py',279),
  ('cteN -> INT codeAddConstNumber','cteN',2,'p_cteN','Yaotecatl.py',280),
  ('cteS -> STRING codeAddConstString','cteS',2,'p_cteS','Yaotecatl.py',285),
  ('exp -> term','exp',1,'p_exp','Yaotecatl.py',290),
  ('exp -> term PLUS codeAddOperator exp','exp',4,'p_exp','Yaotecatl.py',291),
  ('exp -> term MINUS codeAddOperator exp','exp',4,'p_exp','Yaotecatl.py',292),
  ('factoraux -> constant','factoraux',1,'p_factoraux','Yaotecatl.py',295),
  ('factoraux -> PLUS constant','factoraux',2,'p_factoraux','Yaotecatl.py',296),
  ('factoraux -> MINUS constant','factoraux',2,'p_factoraux','Yaotecatl.py',297),
  ('factor -> LFTPAREN codeAddOpenParen expression RGTPAREN codeDeleteOpenParen codeAskFactor','factor',6,'p_factor','Yaotecatl.py',335),
  ('factor -> factoraux codeAskFactor','factor',2,'p_factor','Yaotecatl.py',336),
  ('expression -> exp','expression',1,'p_expression','Yaotecatl.py',339),
  ('expression -> exp expressionaux codeAddOperator exp codeAskExpression','expression',5,'p_expression','Yaotecatl.py',340),
  ('expressionaux -> AND','expressionaux',1,'p_expressionaux','Yaotecatl.py',342),
  ('expressionaux -> DOUBEQUAL','expressionaux',1,'p_expressionaux','Yaotecatl.py',343),
  ('expressionaux -> NOT','expressionaux',1,'p_expressionaux','Yaotecatl.py',344),
  ('expressionaux -> OR','expressionaux',1,'p_expressionaux','Yaotecatl.py',345),
  ('expressionaux -> LESSTHANEQUAL','expressionaux',1,'p_expressionaux','Yaotecatl.py',346),
  ('expressionaux -> GREATTHANEQUAL','expressionaux',1,'p_expressionaux','Yaotecatl.py',347),
  ('expressionaux -> GREATTHAN','expressionaux',1,'p_expressionaux','Yaotecatl.py',348),
  ('expressionaux -> LESSTHAN','expressionaux',1,'p_expressionaux','Yaotecatl.py',349),
  ('loop -> WHILE codeWhileCondition LFTPAREN expression RGTPAREN codeGOTOF block codeGOTOWhile','loop',8,'p_loop','Yaotecatl.py',354),
  ('write -> PRINT LFTPAREN constant RGTPAREN SEMICOLON','write',5,'p_write','Yaotecatl.py',357),
  ('parameter -> type codeCheckType ID codeAddParameters','parameter',4,'p_parameter','Yaotecatl.py',380),
  ('parameter -> type codeCheckType ID codeAddParameters COMMA parameter','parameter',6,'p_parameter','Yaotecatl.py',381),
  ('parameter -> empty','parameter',1,'p_parameter','Yaotecatl.py',382),
  ('term -> factor MULTIPLICATION codeAddOperator term','term',4,'p_term','Yaotecatl.py',385),
  ('term -> factor DIVISION codeAddOperator term','term',4,'p_term','Yaotecatl.py',386),
  ('term -> factor codeAskTerm','term',2,'p_term','Yaotecatl.py',387),
  ('statement -> assignment','statement',1,'p_statement','Yaotecatl.py',392),
  ('statement -> condition','statement',1,'p_statement','Yaotecatl.py',393),
  ('statement -> loop','statement',1,'p_statement','Yaotecatl.py',394),
  ('statement -> write','statement',1,'p_statement','Yaotecatl.py',395),
  ('statement -> read','statement',1,'p_statement','Yaotecatl.py',396),
  ('statement -> call SEMICOLON','statement',2,'p_statement','Yaotecatl.py',397),
  ('type -> INT','type',1,'p_type','Yaotecatl.py',400),
  ('type -> FLOAT','type',1,'p_type','Yaotecatl.py',401),
  ('type -> CHAR','type',1,'p_type','Yaotecatl.py',402),
  ('type -> BOOL','type',1,'p_type','Yaotecatl.py',403),
  ('type -> STRING','type',1,'p_type','Yaotecatl.py',404),
  ('main -> codeLocationMain PRIOMH codeScope block','main',4,'p_main','Yaotecatl.py',409),
  ('function -> FUNCTION codeScope functionaux ID codeNameOfFunct LFTPAREN parameter RGTPAREN codeAddFunctQuad blockreturn codeScope','function',11,'p_function','Yaotecatl.py',413),
  ('functionaux -> VOID codeTypeVoid codeCheckType','functionaux',3,'p_functionaux','Yaotecatl.py',424),
  ('functionaux -> codeFuncIndicator type codeCheckType','functionaux',3,'p_functionaux','Yaotecatl.py',425),
  ('vars -> type codeCheckType varsaux','vars',3,'p_vars','Yaotecatl.py',428),
  ('varsaux2 -> COMMA varsaux','varsaux2',2,'p_varsaux2','Yaotecatl.py',431),
  ('varsaux2 -> SEMICOLON','varsaux2',1,'p_varsaux2','Yaotecatl.py',432),
  ('varsaux -> ID codeAddVar EQUAL expression varsaux2','varsaux',5,'p_varsaux','Yaotecatl.py',435),
  ('varsaux -> ID codeAddVarArreglo LFTBRACSQR INT RGTBRACSQR EQUAL arrayvals varsaux2','varsaux',8,'p_varsaux','Yaotecatl.py',436),
  ('callaux -> codeMovePointer COMMA exp codeAddArguments callaux','callaux',5,'p_callaux','Yaotecatl.py',520),
  ('callaux -> empty','callaux',1,'p_callaux','Yaotecatl.py',521),
  ('call -> ID codeVerifyFunct LFTPAREN codeEraQuad exp codeAddArguments callaux RGTPAREN codeVerifyNull codeGOSUB codeTempReturn','call',11,'p_call','Yaotecatl.py',524),
  ('read -> READ LFTPAREN readaux RGTPAREN SEMICOLON','read',5,'p_read','Yaotecatl.py',531),
  ('readaux -> ID','readaux',1,'p_readaux','Yaotecatl.py',554),
  ('readaux -> array','readaux',1,'p_readaux','Yaotecatl.py',555),
  ('empty -> <empty>','empty',0,'p_empty','Yaotecatl.py',560),
  ('codeGotoElseIf -> <empty>','codeGotoElseIf',0,'p_codeGotoElseIf','Yaotecatl.py',578),
  ('codeAddValueArray -> empty','codeAddValueArray',1,'p_codeAddValueArray','Yaotecatl.py',585),
  ('codeTempReturn -> empty','codeTempReturn',1,'p_codeTempReturn','Yaotecatl.py',594),
  ('codeIsCalll -> empty','codeIsCalll',1,'p_codeIsCalll','Yaotecatl.py',613),
  ('codeGOSUB -> empty','codeGOSUB',1,'p_codeGOSUB','Yaotecatl.py',619),
  ('codeVerifyNull -> empty','codeVerifyNull',1,'p_codeVerifyNull','Yaotecatl.py',627),
  ('codeVerifyNull2 -> empty','codeVerifyNull2',1,'p_codeVerifyNull2','Yaotecatl.py',636),
  ('codeMovePointer -> empty','codeMovePointer',1,'p_codeMovePointer','Yaotecatl.py',645),
  ('codeAddArguments -> empty','codeAddArguments',1,'p_codeAddArguments','Yaotecatl.py',652),
  ('codeEraQuad -> empty','codeEraQuad',1,'p_codeEraQuad','Yaotecatl.py',675),
  ('codeVerifyFunct -> empty','codeVerifyFunct',1,'p_codeVerifyFunct','Yaotecatl.py',687),
  ('codeReturnQuad -> <empty>','codeReturnQuad',0,'p_codeReturnQuad','Yaotecatl.py',708),
  ('codeAddFunctQuad -> <empty>','codeAddFunctQuad',0,'p_codeAddFunctQuad','Yaotecatl.py',721),
  ('codeLocationMain -> <empty>','codeLocationMain',0,'p_codeLocationMain','Yaotecatl.py',735),
  ('codeGOTOMain -> <empty>','codeGOTOMain',0,'p_codeGOTOMain','Yaotecatl.py',740),
  ('codeElse -> <empty>','codeElse',0,'p_codeElse','Yaotecatl.py',748),
  ('codeEndIf -> <empty>','codeEndIf',0,'p_codeEndIf','Yaotecatl.py',755),
  ('codeNextIf -> <empty>','codeNextIf',0,'p_codeNextIf','Yaotecatl.py',760),
  ('codeGOTOF -> <empty>','codeGOTOF',0,'p_codeGOTOF','Yaotecatl.py',766),
  ('codeGOTOWhile -> <empty>','codeGOTOWhile',0,'p_codeGOTOWhile','Yaotecatl.py',781),
  ('codeWhileCondition -> <empty>','codeWhileCondition',0,'p_codeWhileCondition','Yaotecatl.py',788),
  ('codeScope -> <empty>','codeScope',0,'p_codeScope','Yaotecatl.py',794),
  ('codeCheckType -> <empty>','codeCheckType',0,'p_codeCheckType','Yaotecatl.py',805),
  ('codeAddVar -> <empty>','codeAddVar',0,'p_codeAddVar','Yaotecatl.py',828),
  ('codeAddVarArreglo -> <empty>','codeAddVarArreglo',0,'p_codeAddVarArreglo','Yaotecatl.py',837),
  ('codeAddParameters -> <empty>','codeAddParameters',0,'p_codeAddParameters','Yaotecatl.py',847),
  ('codeNameOfFunct -> <empty>','codeNameOfFunct',0,'p_codeNameOfFunct','Yaotecatl.py',861),
  ('codeTypeVoid -> <empty>','codeTypeVoid',0,'p_codeTypeVoid','Yaotecatl.py',869),
  ('codeFuncIndicator -> <empty>','codeFuncIndicator',0,'p_codeFuncIndicator','Yaotecatl.py',876),
  ('codeDeleteOpenParen -> empty','codeDeleteOpenParen',1,'p_codeDeleteOpenParen','Yaotecatl.py',883),
  ('codeAddOpenParen -> empty','codeAddOpenParen',1,'p_codeAddOpenParen','Yaotecatl.py',892),
  ('codeAddConstBool -> empty','codeAddConstBool',1,'p_codeAddConstBool','Yaotecatl.py',899),
  ('codeAddConstString -> empty','codeAddConstString',1,'p_codeAddConstString','Yaotecatl.py',906),
  ('codeAddConstNumber -> empty','codeAddConstNumber',1,'p_codeAddConstNumber','Yaotecatl.py',913),
  ('codeAddOperator -> empty','codeAddOperator',1,'p_codeAddOperator','Yaotecatl.py',932),
  ('codeAskTerm -> empty','codeAskTerm',1,'p_codeAskTerm','Yaotecatl.py',940),
  ('codeAskFactor -> empty','codeAskFactor',1,'p_codeAskFactor','Yaotecatl.py',969),
  ('codeAskExpression -> empty','codeAskExpression',1,'p_codeAskExpression','Yaotecatl.py',998),
]