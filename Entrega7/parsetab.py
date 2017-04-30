
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'LFTBRAC RGTBRAC LFTPAREN RGTPAREN LFTBRACSQR RGTBRACSQR AND DOUBEQUAL NOT OR SEMICOLON EQUAL LESSTHANEQUAL GREATTHANEQUAL GREATTHAN LESSTHAN PLUS MINUS MULTIPLICATION DIVISION ID COMMA FUNCTION INT FALSE STRING READ VOID FLOAT PRIOMH CHAR PRINT WHILE PROGRAM BOOL ELSEIF RETURN ELSE TRUE IFprogram : PROGRAM ID LFTBRAC auxprogramvars codeGOTOMain auxprogramfunct main RGTBRACauxprogramvars : vars auxprogramvars \n    | empty auxprogramfunct : function auxprogramfunct \n    | empty array : ID codeAddOpenParen LFTBRACSQR exp RGTBRACSQR codeDeleteOpenParenarrayvals : LFTBRACSQR arrayvalsaux RGTBRACSQR arrayvalsaux : cteNcteS codeAddValueArray \n    | cteNcteS codeAddValueArray COMMA arrayvalsaux cteNcteS : cteN  \n    | cteSassignment : assignmentaux EQUAL expression SEMICOLONassignmentaux : ID \n    | arrayblockreturn : LFTBRAC blockneutral RGTBRAC \n    | LFTBRAC blockneutral RETURN exp codeReturnQuad SEMICOLON RGTBRAC blockneutral : statement blockneutral \n    | vars blockneutral\n    | empty block : LFTBRAC blockneutral RGTBRACcondition : IF conditionaux codeEndIf\n    | IF conditionaux ELSE codeElse block  codeEndIfconditionaux : LFTPAREN expression RGTPAREN codeGOTOF block codeGotoElseIf conditionaux2 conditionaux2 : codeNextIf ELSEIF conditionaux\n    | empty constant : ID \n    | array \n    | cteN\n    | cteS\n    | TRUE codeAddConstBool\n    | FALSE codeAddConstBool\n    | call codeIsCalll cteN : FLOAT codeAddConstNumber\n    | INT codeAddConstNumbercteS : STRING codeAddConstStringexp : term\n    | term PLUS codeAddOperator exp\n    | term MINUS codeAddOperator exp  factoraux : constant\n    | PLUS constant\n    | MINUS codeMinusSign constant factor : LFTPAREN codeAddOpenParen expression RGTPAREN codeDeleteOpenParen codeAskFactor\n    | factoraux codeAskFactorexpression : exp \n    | exp expressionaux codeAddOperator exp codeAskExpressionexpressionaux : AND \n    | DOUBEQUAL \n    | NOT \n    | OR \n    | LESSTHANEQUAL \n    | GREATTHANEQUAL \n    | GREATTHAN \n    | LESSTHAN loop : WHILE codeWhileCondition LFTPAREN expression RGTPAREN codeGOTOF block codeGOTOWhile write : PRINT LFTPAREN constant RGTPAREN SEMICOLON parameter : type codeCheckType ID codeAddParameters\n    | type codeCheckType ID codeAddParameters COMMA parameter \n    | empty  term : factor MULTIPLICATION codeAddOperator term\n    | factor DIVISION codeAddOperator term \n    | factor codeAskTerm statement : assignment \n    | condition \n    | loop \n    | write \n    | read \n    | call SEMICOLON type : INT  \n    | FLOAT \n    | CHAR \n    | BOOL \n    | STRING   main : codeLocationMain PRIOMH codeScope block  function : FUNCTION codeScope functionaux ID codeNameOfFunct LFTPAREN parameter RGTPAREN codeAddFunctQuad blockreturn codeScope  functionaux : VOID codeTypeVoid codeCheckType \n    | codeFuncIndicator type codeCheckType vars : type codeCheckType varsaux     varsaux2 : COMMA varsaux \n    |  SEMICOLON  varsaux : ID codeAddVar EQUAL expression varsaux2 \n    | ID  codeAddVarArreglo LFTBRACSQR INT RGTBRACSQR EQUAL arrayvals varsaux2 callaux : codeMovePointer COMMA exp codeAddArguments callaux\n    | empty call : ID codeVerifyFunct LFTPAREN codeAddOpenParen codeEraQuad exp codeAddArguments callaux codeDeleteOpenParen RGTPAREN codeVerifyNull codeGOSUB codeTempReturn  read : READ LFTPAREN readaux RGTPAREN SEMICOLON readaux : ID\n    | array empty : codeMinusSign : codeGotoElseIf : codeAddValueArray : emptycodeTempReturn : emptycodeIsCalll : emptycodeGOSUB : emptycodeVerifyNull : emptycodeVerifyNull2 : emptycodeMovePointer : emptycodeAddArguments : emptycodeEraQuad : emptycodeVerifyFunct : emptycodeReturnQuad : codeAddFunctQuad : codeLocationMain : codeGOTOMain : codeElse : codeEndIf : codeNextIf : codeGOTOF : codeGOTOWhile : codeWhileCondition : codeScope : codeCheckType : codeAddVar : codeAddVarArreglo : codeAddParameters : codeNameOfFunct : codeTypeVoid : codeFuncIndicator : codeDeleteOpenParen : emptycodeAddOpenParen : emptycodeAddConstBool : emptycodeAddConstString : emptycodeAddConstNumber : emptycodeAddOperator : emptycodeAskTerm : emptycodeAskFactor : emptycodeAskExpression : empty'
    
_lr_action_items = {'RGTPAREN':([41,42,43,44,46,48,49,50,51,53,54,55,56,57,58,66,67,69,70,71,73,75,76,77,78,79,87,88,89,90,103,122,126,134,135,149,150,151,154,155,156,159,160,161,162,165,173,174,175,178,179,180,184,191,192,193,194,203,204,205,212,214,215,220,227,228,231,232,233,236,237,238,240,241,],[-39,-88,-27,-28,-88,-88,-88,-88,-29,-26,-36,-88,-88,-88,-44,-43,-126,-30,-121,-40,-61,-125,-93,-32,-35,-122,-31,-34,-123,-33,-88,-41,151,158,-58,-60,-59,-88,-37,-38,-88,182,-87,-86,183,186,-88,-119,-88,-127,-45,-115,199,-42,-6,-88,-56,-88,-98,-88,-88,-83,-57,227,-88,-88,-88,-95,-88,-88,-94,-82,-84,-92,]),'RETURN':([22,100,101,104,109,110,112,113,114,117,120,132,136,140,141,145,146,167,172,185,195,197,198,201,206,209,210,218,219,223,224,226,235,],[-77,-79,-80,-88,-65,-66,-19,-88,-62,-63,-64,-78,-18,-67,-17,-106,-20,-21,-81,-12,-88,-85,-55,-106,216,-90,-22,-109,-88,-54,-23,-25,-24,]),'READ':([22,63,100,101,104,109,110,113,114,117,120,132,140,145,146,167,172,185,195,197,198,201,209,210,218,219,223,224,226,235,],[-77,105,-79,-80,105,-65,-66,105,-62,-63,-64,-78,-67,-106,-20,-21,-81,-12,105,-85,-55,-106,-90,-22,-109,-88,-54,-23,-25,-24,]),'VOID':([18,24,],[-111,31,]),'EQUAL':([21,28,65,108,115,116,174,175,192,],[-113,35,121,-14,142,-13,-119,-88,-6,]),'CHAR':([4,6,18,22,24,30,63,100,101,103,104,109,110,113,114,117,120,132,140,145,146,167,172,185,195,197,198,201,205,209,210,218,219,223,224,226,235,],[9,9,-111,-77,-118,9,9,-79,-80,9,9,-65,-66,9,-62,-63,-64,-78,-67,-106,-20,-21,-81,-12,9,-85,-55,-106,9,-90,-22,-109,-88,-54,-23,-25,-24,]),'MULTIPLICATION':([41,42,43,44,46,48,49,50,51,53,55,56,57,66,67,69,70,71,76,77,78,79,87,88,89,90,122,151,173,174,175,191,192,227,231,232,236,237,240,241,],[-39,-88,-27,-28,-88,74,-88,-88,-29,-26,-88,-88,-88,-43,-126,-30,-121,-40,-93,-32,-35,-122,-31,-34,-123,-33,-41,-88,-88,-119,-88,-42,-6,-88,-88,-95,-88,-94,-84,-92,]),'WHILE':([22,63,100,101,104,109,110,113,114,117,120,132,140,145,146,167,172,185,195,197,198,201,209,210,218,219,223,224,226,235,],[-77,107,-79,-80,107,-65,-66,107,-62,-63,-64,-78,-67,-106,-20,-21,-81,-12,107,-85,-55,-106,-90,-22,-109,-88,-54,-23,-25,-24,]),'PROGRAM':([0,],[2,]),'PRINT':([22,63,100,101,104,109,110,113,114,117,120,132,140,145,146,167,172,185,195,197,198,201,209,210,218,219,223,224,226,235,],[-77,106,-79,-80,106,-65,-66,106,-62,-63,-64,-78,-67,-106,-20,-21,-81,-12,106,-85,-55,-106,-90,-22,-109,-88,-54,-23,-25,-24,]),'RGTBRACSQR':([40,41,42,43,44,46,48,49,50,51,53,54,55,56,57,66,67,69,70,71,73,75,76,77,78,79,87,88,89,90,122,149,150,151,152,154,155,168,169,170,171,173,174,175,188,189,191,192,211,227,231,232,236,237,240,241,],[65,-39,-88,-27,-28,-88,-88,-88,-88,-29,-26,-36,-88,-88,-88,-43,-126,-30,-121,-40,-61,-125,-93,-32,-35,-122,-31,-34,-123,-33,-41,-60,-59,-88,175,-37,-38,-11,-88,-10,190,-88,-119,-88,-8,-91,-42,-6,-9,-88,-88,-95,-88,-94,-84,-92,]),'TRUE':([35,45,47,52,68,72,74,80,81,85,86,91,92,93,94,95,96,97,98,99,123,124,125,127,128,129,130,131,138,142,144,153,163,176,177,216,221,],[46,-89,46,-88,46,-88,-88,46,-120,-88,-88,-46,-88,-51,-52,-50,-53,-48,-47,-49,46,-124,46,46,-88,46,46,46,46,46,46,-88,46,46,-99,46,46,]),'MINUS':([35,41,42,43,44,46,48,49,50,51,52,53,54,55,56,57,66,67,69,70,71,72,73,74,75,76,77,78,79,80,81,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,122,123,124,125,127,128,129,130,131,142,144,149,150,151,153,163,173,174,175,176,177,191,192,216,221,227,231,232,236,237,240,241,],[45,-39,-88,-27,-28,-88,-88,-88,-88,-29,-88,-26,86,-88,-88,-88,-43,-126,-30,-121,-40,-88,-61,-88,-125,-93,-32,-35,-122,45,-120,-88,-88,-31,-34,-123,-33,-46,-88,-51,-52,-50,-53,-48,-47,-49,-41,45,-124,45,45,-88,45,45,45,45,45,-60,-59,-88,-88,45,-88,-119,-88,45,-99,-42,-6,45,45,-88,-88,-95,-88,-94,-84,-92,]),'SEMICOLON':([41,42,43,44,46,48,49,50,51,53,54,55,56,57,58,59,66,67,69,70,71,73,75,76,77,78,79,87,88,89,90,111,122,148,149,150,151,154,155,156,164,173,174,175,178,179,182,183,190,191,192,222,227,229,231,232,236,237,240,241,],[-39,-88,-27,-28,-88,-88,-88,-88,-29,-26,-36,-88,-88,-88,-44,100,-43,-126,-30,-121,-40,-61,-125,-93,-32,-35,-122,-31,-34,-123,-33,140,-41,100,-60,-59,-88,-37,-38,-88,185,-88,-119,-88,-127,-45,197,198,-7,-42,-6,-101,-88,234,-88,-95,-88,-94,-84,-92,]),'GREATTHAN':([41,42,43,44,46,48,49,50,51,53,54,55,56,57,58,66,67,69,70,71,73,75,76,77,78,79,87,88,89,90,122,149,150,151,154,155,173,174,175,191,192,227,231,232,236,237,240,241,],[-39,-88,-27,-28,-88,-88,-88,-88,-29,-26,-36,-88,-88,-88,94,-43,-126,-30,-121,-40,-61,-125,-93,-32,-35,-122,-31,-34,-123,-33,-41,-60,-59,-88,-37,-38,-88,-119,-88,-42,-6,-88,-88,-95,-88,-94,-84,-92,]),'LESSTHANEQUAL':([41,42,43,44,46,48,49,50,51,53,54,55,56,57,58,66,67,69,70,71,73,75,76,77,78,79,87,88,89,90,122,149,150,151,154,155,173,174,175,191,192,227,231,232,236,237,240,241,],[-39,-88,-27,-28,-88,-88,-88,-88,-29,-26,-36,-88,-88,-88,95,-43,-126,-30,-121,-40,-61,-125,-93,-32,-35,-122,-31,-34,-123,-33,-41,-60,-59,-88,-37,-38,-88,-119,-88,-42,-6,-88,-88,-95,-88,-94,-84,-92,]),'LFTBRACSQR':([21,27,53,81,82,84,116,121,143,161,],[-114,34,-88,-120,127,-120,-88,147,-120,-88,]),'PLUS':([35,41,42,43,44,46,48,49,50,51,52,53,54,55,56,57,66,67,69,70,71,72,73,74,75,76,77,78,79,80,81,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,122,123,124,125,127,128,129,130,131,142,144,149,150,151,153,163,173,174,175,176,177,191,192,216,221,227,231,232,236,237,240,241,],[47,-39,-88,-27,-28,-88,-88,-88,-88,-29,-88,-26,85,-88,-88,-88,-43,-126,-30,-121,-40,-88,-61,-88,-125,-93,-32,-35,-122,47,-120,-88,-88,-31,-34,-123,-33,-46,-88,-51,-52,-50,-53,-48,-47,-49,-41,47,-124,47,47,-88,47,47,47,47,47,-60,-59,-88,-88,47,-88,-119,-88,47,-99,-42,-6,47,47,-88,-88,-95,-88,-94,-84,-92,]),'COMMA':([41,42,43,44,46,48,49,50,51,53,54,55,56,57,58,59,66,67,69,70,71,73,75,76,77,78,79,87,88,89,90,122,148,149,150,151,154,155,156,168,169,170,173,174,175,178,179,180,188,189,190,191,192,193,194,203,204,213,214,227,228,231,232,233,236,237,240,241,],[-39,-88,-27,-28,-88,-88,-88,-88,-29,-26,-36,-88,-88,-88,-44,102,-43,-126,-30,-121,-40,-61,-125,-93,-32,-35,-122,-31,-34,-123,-33,-41,102,-60,-59,-88,-37,-38,-88,-11,-88,-10,-88,-119,-88,-127,-45,-115,202,-91,-7,-42,-6,-88,205,-88,-98,221,-97,-88,-88,-88,-95,-88,-88,-94,-84,-92,]),'$end':([1,32,],[0,-1,]),'FUNCTION':([4,5,6,13,14,15,17,22,100,101,132,172,196,207,217,239,],[-88,-104,-88,-3,18,-2,18,-77,-79,-80,-78,-81,-111,-74,-15,-16,]),'DIVISION':([41,42,43,44,46,48,49,50,51,53,55,56,57,66,67,69,70,71,76,77,78,79,87,88,89,90,122,151,173,174,175,191,192,227,231,232,236,237,240,241,],[-39,-88,-27,-28,-88,72,-88,-88,-29,-26,-88,-88,-88,-43,-126,-30,-121,-40,-93,-32,-35,-122,-31,-34,-123,-33,-41,-88,-88,-119,-88,-42,-6,-88,-88,-95,-88,-94,-84,-92,]),'STRING':([4,6,18,22,24,30,35,45,47,52,63,68,72,74,80,81,85,86,91,92,93,94,95,96,97,98,99,100,101,103,104,109,110,113,114,117,120,123,124,125,127,128,129,130,131,132,138,140,142,144,145,146,147,153,163,167,172,176,177,185,195,197,198,201,202,205,209,210,216,218,219,221,223,224,226,235,],[11,11,-111,-77,-118,11,50,-89,50,-88,11,50,-88,-88,50,-120,-88,-88,-46,-88,-51,-52,-50,-53,-48,-47,-49,-79,-80,11,11,-65,-66,11,-62,-63,-64,50,-124,50,50,-88,50,50,50,-78,50,-67,50,50,-106,-20,50,-88,50,-21,-81,50,-99,-12,11,-85,-55,-106,50,11,-90,-22,50,-109,-88,50,-54,-23,-25,-24,]),'RGTBRAC':([22,25,63,64,100,101,104,109,110,112,113,114,117,119,120,132,136,140,141,145,146,167,172,185,195,197,198,201,206,209,210,218,219,223,224,226,234,235,],[-77,32,-88,-73,-79,-80,-88,-65,-66,-19,-88,-62,-63,146,-64,-78,-18,-67,-17,-106,-20,-21,-81,-12,-88,-85,-55,-106,217,-90,-22,-109,-88,-54,-23,-25,239,-24,]),'LFTPAREN':([35,36,52,53,60,72,74,80,81,83,84,85,86,91,92,93,94,95,96,97,98,99,105,106,107,116,118,123,124,125,127,128,129,130,131,139,142,143,144,153,163,176,177,216,221,230,],[52,-116,-88,-88,103,-88,-88,52,-120,128,-100,-88,-88,-46,-88,-51,-52,-50,-53,-48,-47,-49,137,138,-110,-88,144,52,-124,52,52,-88,52,52,52,163,52,-100,52,-88,52,52,-99,52,52,144,]),'ELSE':([145,146,209,219,224,226,235,],[166,-20,-90,-88,-23,-25,-24,]),'ELSEIF':([146,209,219,225,],[-20,-90,-107,230,]),'GREATTHANEQUAL':([41,42,43,44,46,48,49,50,51,53,54,55,56,57,58,66,67,69,70,71,73,75,76,77,78,79,87,88,89,90,122,149,150,151,154,155,173,174,175,191,192,227,231,232,236,237,240,241,],[-39,-88,-27,-28,-88,-88,-88,-88,-29,-26,-36,-88,-88,-88,93,-43,-126,-30,-121,-40,-61,-125,-93,-32,-35,-122,-31,-34,-123,-33,-41,-60,-59,-88,-37,-38,-88,-119,-88,-42,-6,-88,-88,-95,-88,-94,-84,-92,]),'DOUBEQUAL':([41,42,43,44,46,48,49,50,51,53,54,55,56,57,58,66,67,69,70,71,73,75,76,77,78,79,87,88,89,90,122,149,150,151,154,155,173,174,175,191,192,227,231,232,236,237,240,241,],[-39,-88,-27,-28,-88,-88,-88,-88,-29,-26,-36,-88,-88,-88,98,-43,-126,-30,-121,-40,-61,-125,-93,-32,-35,-122,-31,-34,-123,-33,-41,-60,-59,-88,-37,-38,-88,-119,-88,-42,-6,-88,-88,-95,-88,-94,-84,-92,]),'ID':([2,7,8,9,10,11,12,16,22,29,31,35,37,38,45,47,52,61,62,63,68,72,74,80,81,85,86,91,92,93,94,95,96,97,98,99,100,101,102,104,109,110,113,114,117,120,123,124,125,127,128,129,130,131,132,133,137,138,140,142,144,145,146,153,157,163,167,172,176,177,185,195,197,198,201,209,210,216,218,219,221,223,224,226,235,],[3,-69,-68,-70,-71,-72,-112,21,-77,36,-117,53,-112,-112,-89,53,-88,-76,-75,116,53,-88,-88,53,-120,-88,-88,-46,-88,-51,-52,-50,-53,-48,-47,-49,-79,-80,21,116,-65,-66,116,-62,-63,-64,53,-124,53,53,-88,53,53,53,-78,-112,161,53,-67,53,53,-106,-20,-88,180,53,-21,-81,53,-99,-12,116,-85,-55,-106,-90,-22,53,-109,-88,53,-54,-23,-25,-24,]),'IF':([22,63,100,101,104,109,110,113,114,117,120,132,140,145,146,167,172,185,195,197,198,201,209,210,218,219,223,224,226,235,],[-77,118,-79,-80,118,-65,-66,118,-62,-63,-64,-78,-67,-106,-20,-21,-81,-12,118,-85,-55,-106,-90,-22,-109,-88,-54,-23,-25,-24,]),'AND':([41,42,43,44,46,48,49,50,51,53,54,55,56,57,58,66,67,69,70,71,73,75,76,77,78,79,87,88,89,90,122,149,150,151,154,155,173,174,175,191,192,227,231,232,236,237,240,241,],[-39,-88,-27,-28,-88,-88,-88,-88,-29,-26,-36,-88,-88,-88,91,-43,-126,-30,-121,-40,-61,-125,-93,-32,-35,-122,-31,-34,-123,-33,-41,-60,-59,-88,-37,-38,-88,-119,-88,-42,-6,-88,-88,-95,-88,-94,-84,-92,]),'FALSE':([35,45,47,52,68,72,74,80,81,85,86,91,92,93,94,95,96,97,98,99,123,124,125,127,128,129,130,131,138,142,144,153,163,176,177,216,221,],[55,-89,55,-88,55,-88,-88,55,-120,-88,-88,-46,-88,-51,-52,-50,-53,-48,-47,-49,55,-124,55,55,-88,55,55,55,55,55,55,-88,55,55,-99,55,55,]),'LFTBRAC':([3,33,39,158,166,181,186,187,199,200,208,],[4,-111,63,-102,-105,195,-108,63,-108,63,63,]),'INT':([4,6,18,22,24,30,34,35,45,47,52,63,68,72,74,80,81,85,86,91,92,93,94,95,96,97,98,99,100,101,103,104,109,110,113,114,117,120,123,124,125,127,128,129,130,131,132,138,140,142,144,145,146,147,153,163,167,172,176,177,185,195,197,198,201,202,205,209,210,216,218,219,221,223,224,226,235,],[8,8,-111,-77,-118,8,40,56,-89,56,-88,8,56,-88,-88,56,-120,-88,-88,-46,-88,-51,-52,-50,-53,-48,-47,-49,-79,-80,8,8,-65,-66,8,-62,-63,-64,56,-124,56,56,-88,56,56,56,-78,56,-67,56,56,-106,-20,56,-88,56,-21,-81,56,-99,-12,8,-85,-55,-106,56,8,-90,-22,56,-109,-88,56,-54,-23,-25,-24,]),'FLOAT':([4,6,18,22,24,30,35,45,47,52,63,68,72,74,80,81,85,86,91,92,93,94,95,96,97,98,99,100,101,103,104,109,110,113,114,117,120,123,124,125,127,128,129,130,131,132,138,140,142,144,145,146,147,153,163,167,172,176,177,185,195,197,198,201,202,205,209,210,216,218,219,221,223,224,226,235,],[7,7,-111,-77,-118,7,57,-89,57,-88,7,57,-88,-88,57,-120,-88,-88,-46,-88,-51,-52,-50,-53,-48,-47,-49,-79,-80,7,7,-65,-66,7,-62,-63,-64,57,-124,57,57,-88,57,57,57,-78,57,-67,57,57,-106,-20,57,-88,57,-21,-81,57,-99,-12,7,-85,-55,-106,57,7,-90,-22,57,-109,-88,57,-54,-23,-25,-24,]),'LESSTHAN':([41,42,43,44,46,48,49,50,51,53,54,55,56,57,58,66,67,69,70,71,73,75,76,77,78,79,87,88,89,90,122,149,150,151,154,155,173,174,175,191,192,227,231,232,236,237,240,241,],[-39,-88,-27,-28,-88,-88,-88,-88,-29,-26,-36,-88,-88,-88,96,-43,-126,-30,-121,-40,-61,-125,-93,-32,-35,-122,-31,-34,-123,-33,-41,-60,-59,-88,-37,-38,-88,-119,-88,-42,-6,-88,-88,-95,-88,-94,-84,-92,]),'PRIOMH':([4,5,6,13,14,15,17,19,20,22,23,26,100,101,132,172,196,207,217,239,],[-88,-104,-88,-3,-88,-2,-88,-103,-5,-77,-4,33,-79,-80,-78,-81,-111,-74,-15,-16,]),'BOOL':([4,6,18,22,24,30,63,100,101,103,104,109,110,113,114,117,120,132,140,145,146,167,172,185,195,197,198,201,205,209,210,218,219,223,224,226,235,],[10,10,-111,-77,-118,10,10,-79,-80,10,10,-65,-66,10,-62,-63,-64,-78,-67,-106,-20,-21,-81,-12,10,-85,-55,-106,10,-90,-22,-109,-88,-54,-23,-25,-24,]),'NOT':([41,42,43,44,46,48,49,50,51,53,54,55,56,57,58,66,67,69,70,71,73,75,76,77,78,79,87,88,89,90,122,149,150,151,154,155,173,174,175,191,192,227,231,232,236,237,240,241,],[-39,-88,-27,-28,-88,-88,-88,-88,-29,-26,-36,-88,-88,-88,97,-43,-126,-30,-121,-40,-61,-125,-93,-32,-35,-122,-31,-34,-123,-33,-41,-60,-59,-88,-37,-38,-88,-119,-88,-42,-6,-88,-88,-95,-88,-94,-84,-92,]),'OR':([41,42,43,44,46,48,49,50,51,53,54,55,56,57,58,66,67,69,70,71,73,75,76,77,78,79,87,88,89,90,122,149,150,151,154,155,173,174,175,191,192,227,231,232,236,237,240,241,],[-39,-88,-27,-28,-88,-88,-88,-88,-29,-26,-36,-88,-88,-88,99,-43,-126,-30,-121,-40,-61,-125,-93,-32,-35,-122,-31,-34,-123,-33,-41,-60,-59,-88,-37,-38,-88,-119,-88,-42,-6,-88,-88,-95,-88,-94,-84,-92,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'cteS':([35,47,68,80,123,125,127,129,130,131,138,142,144,147,163,176,202,216,221,],[51,51,51,51,51,51,51,51,51,51,51,51,51,168,51,51,168,51,51,]),'constant':([35,47,68,80,123,125,127,129,130,131,138,142,144,163,176,216,221,],[41,71,122,41,41,41,41,41,41,41,162,41,41,41,41,41,41,]),'vars':([4,6,63,104,113,195,],[6,6,104,104,104,104,]),'expressionaux':([58,],[92,]),'codeGOTOMain':([5,],[14,]),'codeGOSUB':([231,],[236,]),'codeNameOfFunct':([36,],[60,]),'codeDeleteOpenParen':([151,175,212,],[173,192,220,]),'codeAddConstBool':([46,55,],[69,87,]),'codeReturnQuad':([222,],[229,]),'codeGOTOF':([186,199,],[200,208,]),'factoraux':([35,80,123,125,127,129,130,131,142,144,163,176,216,221,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'codeAddParameters':([180,],[194,]),'array':([35,47,63,68,80,104,113,123,125,127,129,130,131,137,138,142,144,163,176,195,216,221,],[43,43,108,43,43,108,108,43,43,43,43,43,43,160,43,43,43,43,43,108,43,43,]),'codeWhileCondition':([107,],[139,]),'cteN':([35,47,68,80,123,125,127,129,130,131,138,142,144,147,163,176,202,216,221,],[44,44,44,44,44,44,44,44,44,44,44,44,44,170,44,44,170,44,44,]),'codeFuncIndicator':([24,],[30,]),'arrayvals':([121,],[148,]),'codeAskExpression':([156,],[179,]),'codeMovePointer':([203,233,],[213,213,]),'codeAddArguments':([193,228,],[203,233,]),'codeAskTerm':([48,],[73,]),'arrayvalsaux':([147,202,],[171,211,]),'auxprogramvars':([4,6,],[5,15,]),'functionaux':([24,],[29,]),'codeAddConstNumber':([56,57,],[88,90,]),'codeNextIf':([219,],[225,]),'write':([63,104,113,195,],[109,109,109,109,]),'program':([0,],[1,]),'call':([35,47,63,68,80,104,113,123,125,127,129,130,131,138,142,144,163,176,195,216,221,],[49,49,111,49,49,111,111,49,49,49,49,49,49,49,49,49,49,49,111,49,49,]),'statement':([63,104,113,195,],[113,113,113,113,]),'factor':([35,80,123,125,127,129,130,131,142,144,163,176,216,221,],[48,48,48,48,48,48,48,48,48,48,48,48,48,48,]),'codeAskFactor':([42,173,],[66,191,]),'main':([19,],[25,]),'type':([4,6,30,63,103,104,113,195,205,],[12,12,37,12,133,12,12,12,133,]),'codeAddVar':([21,],[28,]),'empty':([4,6,14,17,42,46,48,49,50,52,53,55,56,57,63,72,74,85,86,92,103,104,113,116,128,151,153,156,161,169,173,175,193,195,203,205,212,219,227,228,231,233,236,],[13,13,20,20,67,70,75,76,79,81,84,70,89,89,112,124,124,124,124,124,135,112,112,143,81,174,177,178,81,189,67,174,204,112,214,135,174,226,232,204,237,214,241,]),'codeEndIf':([145,201,],[167,210,]),'function':([14,17,],[17,17,]),'codeTypeVoid':([31,],[38,]),'codeElse':([166,],[187,]),'codeLocationMain':([19,],[26,]),'codeAddValueArray':([169,],[188,]),'read':([63,104,113,195,],[110,110,110,110,]),'assignment':([63,104,113,195,],[114,114,114,114,]),'codeAddVarArreglo':([21,],[27,]),'codeAddOpenParen':([52,53,116,128,161,],[80,82,82,153,82,]),'callaux':([203,233,],[212,238,]),'readaux':([137,],[159,]),'varsaux2':([59,148,],[101,172,]),'codeMinusSign':([45,],[68,]),'codeGOTOWhile':([218,],[223,]),'codeGotoElseIf':([209,],[219,]),'cteNcteS':([147,202,],[169,169,]),'codeAddOperator':([72,74,85,86,92,],[123,125,129,130,131,]),'parameter':([103,205,],[134,215,]),'condition':([63,104,113,195,],[117,117,117,117,]),'codeVerifyNull':([227,],[231,]),'codeScope':([18,33,196,],[24,39,207,]),'codeTempReturn':([236,],[240,]),'term':([35,80,123,125,127,129,130,131,142,144,163,176,216,221,],[54,54,149,150,54,54,54,54,54,54,54,54,54,54,]),'conditionaux2':([219,],[224,]),'codeEraQuad':([153,],[176,]),'codeCheckType':([12,37,38,133,],[16,61,62,157,]),'codeVerifyFunct':([53,116,],[83,83,]),'codeAddFunctQuad':([158,],[181,]),'assignmentaux':([63,104,113,195,],[115,115,115,115,]),'codeIsCalll':([49,],[77,]),'blockneutral':([63,104,113,195,],[119,136,141,206,]),'blockreturn':([181,],[196,]),'auxprogramfunct':([14,17,],[19,23,]),'codeAddConstString':([50,],[78,]),'loop':([63,104,113,195,],[120,120,120,120,]),'exp':([35,80,127,129,130,131,142,144,163,176,216,221,],[58,58,152,154,155,156,58,58,58,193,222,228,]),'conditionaux':([118,230,],[145,235,]),'expression':([35,80,142,144,163,],[59,126,164,165,184,]),'block':([39,187,200,208,],[64,201,209,218,]),'varsaux':([16,102,],[22,132,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID LFTBRAC auxprogramvars codeGOTOMain auxprogramfunct main RGTBRAC','program',8,'p_program','Yaotecatl.py',93),
  ('auxprogramvars -> vars auxprogramvars','auxprogramvars',2,'p_auxprogramvars','Yaotecatl.py',131),
  ('auxprogramvars -> empty','auxprogramvars',1,'p_auxprogramvars','Yaotecatl.py',132),
  ('auxprogramfunct -> function auxprogramfunct','auxprogramfunct',2,'p_auxprogramfunct','Yaotecatl.py',134),
  ('auxprogramfunct -> empty','auxprogramfunct',1,'p_auxprogramfunct','Yaotecatl.py',135),
  ('array -> ID codeAddOpenParen LFTBRACSQR exp RGTBRACSQR codeDeleteOpenParen','array',6,'p_array','Yaotecatl.py',139),
  ('arrayvals -> LFTBRACSQR arrayvalsaux RGTBRACSQR','arrayvals',3,'p_arrayvals','Yaotecatl.py',191),
  ('arrayvalsaux -> cteNcteS codeAddValueArray','arrayvalsaux',2,'p_arrayvalsaux','Yaotecatl.py',194),
  ('arrayvalsaux -> cteNcteS codeAddValueArray COMMA arrayvalsaux','arrayvalsaux',4,'p_arrayvalsaux','Yaotecatl.py',195),
  ('cteNcteS -> cteN','cteNcteS',1,'p_cteNcteS','Yaotecatl.py',198),
  ('cteNcteS -> cteS','cteNcteS',1,'p_cteNcteS','Yaotecatl.py',199),
  ('assignment -> assignmentaux EQUAL expression SEMICOLON','assignment',4,'p_assignment','Yaotecatl.py',207),
  ('assignmentaux -> ID','assignmentaux',1,'p_assignmentaux','Yaotecatl.py',245),
  ('assignmentaux -> array','assignmentaux',1,'p_assignmentaux','Yaotecatl.py',246),
  ('blockreturn -> LFTBRAC blockneutral RGTBRAC','blockreturn',3,'p_blockreturn','Yaotecatl.py',252),
  ('blockreturn -> LFTBRAC blockneutral RETURN exp codeReturnQuad SEMICOLON RGTBRAC','blockreturn',7,'p_blockreturn','Yaotecatl.py',253),
  ('blockneutral -> statement blockneutral','blockneutral',2,'p_blockneutral','Yaotecatl.py',255),
  ('blockneutral -> vars blockneutral','blockneutral',2,'p_blockneutral','Yaotecatl.py',256),
  ('blockneutral -> empty','blockneutral',1,'p_blockneutral','Yaotecatl.py',257),
  ('block -> LFTBRAC blockneutral RGTBRAC','block',3,'p_block','Yaotecatl.py',259),
  ('condition -> IF conditionaux codeEndIf','condition',3,'p_condition','Yaotecatl.py',262),
  ('condition -> IF conditionaux ELSE codeElse block codeEndIf','condition',6,'p_condition','Yaotecatl.py',263),
  ('conditionaux -> LFTPAREN expression RGTPAREN codeGOTOF block codeGotoElseIf conditionaux2','conditionaux',7,'p_conditionaux','Yaotecatl.py',265),
  ('conditionaux2 -> codeNextIf ELSEIF conditionaux','conditionaux2',3,'p_conditionaux2','Yaotecatl.py',267),
  ('conditionaux2 -> empty','conditionaux2',1,'p_conditionaux2','Yaotecatl.py',268),
  ('constant -> ID','constant',1,'p_constant','Yaotecatl.py',272),
  ('constant -> array','constant',1,'p_constant','Yaotecatl.py',273),
  ('constant -> cteN','constant',1,'p_constant','Yaotecatl.py',274),
  ('constant -> cteS','constant',1,'p_constant','Yaotecatl.py',275),
  ('constant -> TRUE codeAddConstBool','constant',2,'p_constant','Yaotecatl.py',276),
  ('constant -> FALSE codeAddConstBool','constant',2,'p_constant','Yaotecatl.py',277),
  ('constant -> call codeIsCalll','constant',2,'p_constant','Yaotecatl.py',278),
  ('cteN -> FLOAT codeAddConstNumber','cteN',2,'p_cteN','Yaotecatl.py',286),
  ('cteN -> INT codeAddConstNumber','cteN',2,'p_cteN','Yaotecatl.py',287),
  ('cteS -> STRING codeAddConstString','cteS',2,'p_cteS','Yaotecatl.py',292),
  ('exp -> term','exp',1,'p_exp','Yaotecatl.py',297),
  ('exp -> term PLUS codeAddOperator exp','exp',4,'p_exp','Yaotecatl.py',298),
  ('exp -> term MINUS codeAddOperator exp','exp',4,'p_exp','Yaotecatl.py',299),
  ('factoraux -> constant','factoraux',1,'p_factoraux','Yaotecatl.py',302),
  ('factoraux -> PLUS constant','factoraux',2,'p_factoraux','Yaotecatl.py',303),
  ('factoraux -> MINUS codeMinusSign constant','factoraux',3,'p_factoraux','Yaotecatl.py',304),
  ('factor -> LFTPAREN codeAddOpenParen expression RGTPAREN codeDeleteOpenParen codeAskFactor','factor',6,'p_factor','Yaotecatl.py',340),
  ('factor -> factoraux codeAskFactor','factor',2,'p_factor','Yaotecatl.py',341),
  ('expression -> exp','expression',1,'p_expression','Yaotecatl.py',344),
  ('expression -> exp expressionaux codeAddOperator exp codeAskExpression','expression',5,'p_expression','Yaotecatl.py',345),
  ('expressionaux -> AND','expressionaux',1,'p_expressionaux','Yaotecatl.py',347),
  ('expressionaux -> DOUBEQUAL','expressionaux',1,'p_expressionaux','Yaotecatl.py',348),
  ('expressionaux -> NOT','expressionaux',1,'p_expressionaux','Yaotecatl.py',349),
  ('expressionaux -> OR','expressionaux',1,'p_expressionaux','Yaotecatl.py',350),
  ('expressionaux -> LESSTHANEQUAL','expressionaux',1,'p_expressionaux','Yaotecatl.py',351),
  ('expressionaux -> GREATTHANEQUAL','expressionaux',1,'p_expressionaux','Yaotecatl.py',352),
  ('expressionaux -> GREATTHAN','expressionaux',1,'p_expressionaux','Yaotecatl.py',353),
  ('expressionaux -> LESSTHAN','expressionaux',1,'p_expressionaux','Yaotecatl.py',354),
  ('loop -> WHILE codeWhileCondition LFTPAREN expression RGTPAREN codeGOTOF block codeGOTOWhile','loop',8,'p_loop','Yaotecatl.py',359),
  ('write -> PRINT LFTPAREN constant RGTPAREN SEMICOLON','write',5,'p_write','Yaotecatl.py',362),
  ('parameter -> type codeCheckType ID codeAddParameters','parameter',4,'p_parameter','Yaotecatl.py',395),
  ('parameter -> type codeCheckType ID codeAddParameters COMMA parameter','parameter',6,'p_parameter','Yaotecatl.py',396),
  ('parameter -> empty','parameter',1,'p_parameter','Yaotecatl.py',397),
  ('term -> factor MULTIPLICATION codeAddOperator term','term',4,'p_term','Yaotecatl.py',400),
  ('term -> factor DIVISION codeAddOperator term','term',4,'p_term','Yaotecatl.py',401),
  ('term -> factor codeAskTerm','term',2,'p_term','Yaotecatl.py',402),
  ('statement -> assignment','statement',1,'p_statement','Yaotecatl.py',407),
  ('statement -> condition','statement',1,'p_statement','Yaotecatl.py',408),
  ('statement -> loop','statement',1,'p_statement','Yaotecatl.py',409),
  ('statement -> write','statement',1,'p_statement','Yaotecatl.py',410),
  ('statement -> read','statement',1,'p_statement','Yaotecatl.py',411),
  ('statement -> call SEMICOLON','statement',2,'p_statement','Yaotecatl.py',412),
  ('type -> INT','type',1,'p_type','Yaotecatl.py',415),
  ('type -> FLOAT','type',1,'p_type','Yaotecatl.py',416),
  ('type -> CHAR','type',1,'p_type','Yaotecatl.py',417),
  ('type -> BOOL','type',1,'p_type','Yaotecatl.py',418),
  ('type -> STRING','type',1,'p_type','Yaotecatl.py',419),
  ('main -> codeLocationMain PRIOMH codeScope block','main',4,'p_main','Yaotecatl.py',424),
  ('function -> FUNCTION codeScope functionaux ID codeNameOfFunct LFTPAREN parameter RGTPAREN codeAddFunctQuad blockreturn codeScope','function',11,'p_function','Yaotecatl.py',428),
  ('functionaux -> VOID codeTypeVoid codeCheckType','functionaux',3,'p_functionaux','Yaotecatl.py',470),
  ('functionaux -> codeFuncIndicator type codeCheckType','functionaux',3,'p_functionaux','Yaotecatl.py',471),
  ('vars -> type codeCheckType varsaux','vars',3,'p_vars','Yaotecatl.py',474),
  ('varsaux2 -> COMMA varsaux','varsaux2',2,'p_varsaux2','Yaotecatl.py',477),
  ('varsaux2 -> SEMICOLON','varsaux2',1,'p_varsaux2','Yaotecatl.py',478),
  ('varsaux -> ID codeAddVar EQUAL expression varsaux2','varsaux',5,'p_varsaux','Yaotecatl.py',481),
  ('varsaux -> ID codeAddVarArreglo LFTBRACSQR INT RGTBRACSQR EQUAL arrayvals varsaux2','varsaux',8,'p_varsaux','Yaotecatl.py',482),
  ('callaux -> codeMovePointer COMMA exp codeAddArguments callaux','callaux',5,'p_callaux','Yaotecatl.py',567),
  ('callaux -> empty','callaux',1,'p_callaux','Yaotecatl.py',568),
  ('call -> ID codeVerifyFunct LFTPAREN codeAddOpenParen codeEraQuad exp codeAddArguments callaux codeDeleteOpenParen RGTPAREN codeVerifyNull codeGOSUB codeTempReturn','call',13,'p_call','Yaotecatl.py',571),
  ('read -> READ LFTPAREN readaux RGTPAREN SEMICOLON','read',5,'p_read','Yaotecatl.py',578),
  ('readaux -> ID','readaux',1,'p_readaux','Yaotecatl.py',601),
  ('readaux -> array','readaux',1,'p_readaux','Yaotecatl.py',602),
  ('empty -> <empty>','empty',0,'p_empty','Yaotecatl.py',607),
  ('codeMinusSign -> <empty>','codeMinusSign',0,'p_codeMinusSign','Yaotecatl.py',625),
  ('codeGotoElseIf -> <empty>','codeGotoElseIf',0,'p_codeGotoElseIf','Yaotecatl.py',632),
  ('codeAddValueArray -> empty','codeAddValueArray',1,'p_codeAddValueArray','Yaotecatl.py',639),
  ('codeTempReturn -> empty','codeTempReturn',1,'p_codeTempReturn','Yaotecatl.py',648),
  ('codeIsCalll -> empty','codeIsCalll',1,'p_codeIsCalll','Yaotecatl.py',667),
  ('codeGOSUB -> empty','codeGOSUB',1,'p_codeGOSUB','Yaotecatl.py',673),
  ('codeVerifyNull -> empty','codeVerifyNull',1,'p_codeVerifyNull','Yaotecatl.py',681),
  ('codeVerifyNull2 -> empty','codeVerifyNull2',1,'p_codeVerifyNull2','Yaotecatl.py',690),
  ('codeMovePointer -> empty','codeMovePointer',1,'p_codeMovePointer','Yaotecatl.py',699),
  ('codeAddArguments -> empty','codeAddArguments',1,'p_codeAddArguments','Yaotecatl.py',706),
  ('codeEraQuad -> empty','codeEraQuad',1,'p_codeEraQuad','Yaotecatl.py',729),
  ('codeVerifyFunct -> empty','codeVerifyFunct',1,'p_codeVerifyFunct','Yaotecatl.py',741),
  ('codeReturnQuad -> <empty>','codeReturnQuad',0,'p_codeReturnQuad','Yaotecatl.py',762),
  ('codeAddFunctQuad -> <empty>','codeAddFunctQuad',0,'p_codeAddFunctQuad','Yaotecatl.py',775),
  ('codeLocationMain -> <empty>','codeLocationMain',0,'p_codeLocationMain','Yaotecatl.py',789),
  ('codeGOTOMain -> <empty>','codeGOTOMain',0,'p_codeGOTOMain','Yaotecatl.py',794),
  ('codeElse -> <empty>','codeElse',0,'p_codeElse','Yaotecatl.py',802),
  ('codeEndIf -> <empty>','codeEndIf',0,'p_codeEndIf','Yaotecatl.py',808),
  ('codeNextIf -> <empty>','codeNextIf',0,'p_codeNextIf','Yaotecatl.py',816),
  ('codeGOTOF -> <empty>','codeGOTOF',0,'p_codeGOTOF','Yaotecatl.py',822),
  ('codeGOTOWhile -> <empty>','codeGOTOWhile',0,'p_codeGOTOWhile','Yaotecatl.py',837),
  ('codeWhileCondition -> <empty>','codeWhileCondition',0,'p_codeWhileCondition','Yaotecatl.py',844),
  ('codeScope -> <empty>','codeScope',0,'p_codeScope','Yaotecatl.py',850),
  ('codeCheckType -> <empty>','codeCheckType',0,'p_codeCheckType','Yaotecatl.py',861),
  ('codeAddVar -> <empty>','codeAddVar',0,'p_codeAddVar','Yaotecatl.py',884),
  ('codeAddVarArreglo -> <empty>','codeAddVarArreglo',0,'p_codeAddVarArreglo','Yaotecatl.py',893),
  ('codeAddParameters -> <empty>','codeAddParameters',0,'p_codeAddParameters','Yaotecatl.py',903),
  ('codeNameOfFunct -> <empty>','codeNameOfFunct',0,'p_codeNameOfFunct','Yaotecatl.py',917),
  ('codeTypeVoid -> <empty>','codeTypeVoid',0,'p_codeTypeVoid','Yaotecatl.py',925),
  ('codeFuncIndicator -> <empty>','codeFuncIndicator',0,'p_codeFuncIndicator','Yaotecatl.py',932),
  ('codeDeleteOpenParen -> empty','codeDeleteOpenParen',1,'p_codeDeleteOpenParen','Yaotecatl.py',939),
  ('codeAddOpenParen -> empty','codeAddOpenParen',1,'p_codeAddOpenParen','Yaotecatl.py',948),
  ('codeAddConstBool -> empty','codeAddConstBool',1,'p_codeAddConstBool','Yaotecatl.py',955),
  ('codeAddConstString -> empty','codeAddConstString',1,'p_codeAddConstString','Yaotecatl.py',962),
  ('codeAddConstNumber -> empty','codeAddConstNumber',1,'p_codeAddConstNumber','Yaotecatl.py',969),
  ('codeAddOperator -> empty','codeAddOperator',1,'p_codeAddOperator','Yaotecatl.py',999),
  ('codeAskTerm -> empty','codeAskTerm',1,'p_codeAskTerm','Yaotecatl.py',1007),
  ('codeAskFactor -> empty','codeAskFactor',1,'p_codeAskFactor','Yaotecatl.py',1036),
  ('codeAskExpression -> empty','codeAskExpression',1,'p_codeAskExpression','Yaotecatl.py',1065),
]
