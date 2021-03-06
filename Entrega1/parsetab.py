
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'LFTBRAC RGTBRAC LFTPAREN RGTPAREN LFTBRACSQR RGTBRACSQR AND DOUBEQUAL NOT OR SEMICOLON EQUAL LESSTHANEQUAL GREATTHANEQUAL GREATTHAN LESSTHAN PLUS MINUS MULTIPLICATION DIVISION ID COMMA FUNCTION INT FALSE STRING READ VOID FLOAT PRIOMH CHAR PRINT WHILE PROGRAM BOOL ELSEIF RETURN ELSE TRUE IFprogram : PROGRAM ID LFTBRAC auxprogram main RGTBRACauxprogram : vars auxprogram \n    | function auxprogram \n    | emptyarray : ID LFTBRACSQR exp RGTBRACSQRarrayvalues : LFTBRACSQR arrayvaluesaux RGTBRACSQR arrayvaluesaux : constant  \n    | constant COMMA arrayvaluesaux assignment : assignmentaux EQUAL expression SEMICOLON assignmentaux : ID \n    | arrayblockreturn : LFTBRAC blockneutral RGTBRAC \n    | LFTBRAC blockneutral RETURN exp SEMICOLON RGTBRAC blockneutral : statement blockneutral \n    | vars blockneutral\n    | empty block : LFTBRAC blockneutral RGTBRACcondition : IF conditionaux \n    | IF conditionaux ELSE block conditionaux : LFTPAREN expression RGTPAREN block conditionaux2 conditionaux2 : ELSEIF conditionaux \n    | empty constant : ID \n    | array \n    | cteN\n    | cteS\n    | TRUE \n    | FALSE\n    | call2 cteN : FLOAT \n    | INTcteS : STRINGexp : term expaux  expaux : PLUS exp expaux \n    | MINUS exp expaux \n    | empty factor : LFTPAREN expression RGTPAREN\n    | constant\n    | MINUS constant\n    | PLUS constant expression : exp \n    | exp expressionaux exp expressionaux : AND \n    | DOUBEQUAL \n    | NOT \n    | OR \n    | LESSTHANEQUAL \n    | GREATTHANEQUAL \n    | GREATTHAN \n    | LESSTHAN loop : WHILE LFTPAREN expression RGTPAREN block write : PRINT LFTPAREN constant RGTPAREN SEMICOLON parameter : type ID \n    | type ID COMMA parameter \n    | empty  term : factor termaux  termaux : MULTIPLICATION term termaux \n    | DIVISION term termaux \n    | empty  statement : assignment \n    | condition \n    | loop \n    | write \n    | read \n    | call  type : INT \n    | FLOAT \n    | CHAR \n    | BOOL \n    | STRING  main : PRIOMH block  function : FUNCTION functionaux ID LFTPAREN parameter RGTPAREN blockreturn  functionaux : VOID \n    | type  vars : type varsaux     varsaux : ID EQUAL expression SEMICOLON\n    | ID EQUAL expression COMMA varsaux \n    | ID LFTBRACSQR INT RGTBRACSQR EQUAL arrayvalues SEMICOLON\n    | ID LFTBRACSQR INT RGTBRACSQR EQUAL arrayvalues COMMA varsaux call : ID LFTPAREN exp callaux RGTPAREN SEMICOLON  callaux : COMMA exp callaux\n    | empty call2 : ID LFTPAREN exp callaux RGTPAREN  read : READ LFTPAREN readaux RGTPAREN SEMICOLON readaux : ID\n    | array empty : '
    
_lr_action_items = {'RGTPAREN':([31,49,50,51,52,54,55,56,58,60,61,62,63,64,65,69,70,82,85,86,87,88,90,93,106,108,109,110,111,112,114,116,118,119,120,121,122,123,124,127,134,136,137,140,141,142,143,144,147,153,155,163,],[-87,-38,-26,-24,-25,-29,-27,-87,-32,-23,-87,-28,-31,-30,-41,107,-55,-39,-56,-59,-40,120,-33,-36,-53,130,-86,-85,131,132,-87,138,-87,-87,-37,-87,-87,-87,-42,-87,152,-82,-5,-58,-57,155,-34,-35,-54,-87,-83,-81,]),'RETURN':([24,32,37,38,39,40,41,42,45,48,71,75,80,81,103,125,128,133,139,148,149,150,151,154,158,162,164,165,169,171,],[-75,-87,-63,-64,-65,-87,-16,-60,-61,-62,-15,-14,-18,-17,-76,-77,-87,-9,-19,160,-84,-51,-52,-87,-78,-80,-20,-22,-79,-21,]),'READ':([24,26,32,37,38,39,40,42,45,48,80,81,103,125,128,133,139,149,150,151,154,158,162,164,165,169,171,],[-75,33,33,-63,-64,-65,33,-60,-61,-62,-18,-17,-76,-77,33,-9,-19,-84,-51,-52,-87,-78,-80,-20,-22,-79,-21,]),'VOID':([5,],[18,]),'EQUAL':([23,36,43,44,105,137,],[29,-11,76,-10,126,-5,]),'CHAR':([4,5,6,10,24,26,31,32,37,38,39,40,42,45,48,80,81,103,125,127,128,129,133,139,149,150,151,154,158,161,162,164,165,169,171,174,],[7,7,7,7,-75,7,7,7,-63,-64,-65,7,-60,-61,-62,-18,-17,-76,-77,7,7,-72,-9,-19,-84,-51,-52,-87,-78,-12,-80,-20,-22,-79,-21,-13,]),'MULTIPLICATION':([49,50,51,52,54,55,56,58,60,62,63,64,82,85,86,87,118,119,120,137,140,141,155,],[-38,-26,-24,-25,-29,-27,84,-32,-23,-28,-31,-30,-39,-56,-59,-40,84,84,-37,-5,-58,-57,-83,]),'WHILE':([24,26,32,37,38,39,40,42,45,48,80,81,103,125,128,133,139,149,150,151,154,158,162,164,165,169,171,],[-75,34,34,-63,-64,-65,34,-60,-61,-62,-18,-17,-76,-77,34,-9,-19,-84,-51,-52,-87,-78,-80,-20,-22,-79,-21,]),'PROGRAM':([0,],[2,]),'PRINT':([24,26,32,37,38,39,40,42,45,48,80,81,103,125,128,133,139,149,150,151,154,158,162,164,165,169,171,],[-75,35,35,-63,-64,-65,35,-60,-61,-62,-18,-17,-76,-77,35,-9,-19,-84,-51,-52,-87,-78,-80,-20,-22,-79,-21,]),'RGTBRACSQR':([49,50,51,52,54,55,56,58,60,61,62,63,64,67,82,85,86,87,90,93,115,118,119,120,122,123,137,140,141,143,144,155,156,157,172,],[-38,-26,-24,-25,-29,-27,-87,-32,-23,-87,-28,-31,-30,105,-39,-56,-59,-40,-33,-36,137,-87,-87,-37,-87,-87,-5,-58,-57,-34,-35,-83,-7,168,-8,]),'TRUE':([29,53,57,59,73,74,76,77,78,79,83,84,89,91,92,94,95,96,97,98,99,100,101,102,135,145,160,167,],[55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,-43,55,-48,-49,-47,-50,-45,-44,-46,55,55,55,55,]),'MINUS':([29,49,50,51,52,54,55,56,58,59,60,61,62,63,64,73,76,77,78,79,82,83,84,85,86,87,89,90,91,92,93,94,95,96,97,98,99,100,101,102,118,119,120,122,123,135,137,140,141,143,144,155,160,],[53,-38,-26,-24,-25,-29,-27,-87,-32,53,-23,92,-28,-31,-30,53,53,53,53,53,-39,53,53,-56,-59,-40,53,-33,53,53,-36,-43,53,-48,-49,-47,-50,-45,-44,-46,-87,-87,-37,92,92,53,-5,-58,-57,-34,-35,-83,53,]),'SEMICOLON':([49,50,51,52,54,55,56,58,60,61,62,63,64,65,66,82,85,86,87,90,93,113,118,119,120,122,123,124,130,132,137,140,141,143,144,146,152,155,168,170,],[-38,-26,-24,-25,-29,-27,-87,-32,-23,-87,-28,-31,-30,-41,103,-39,-56,-59,-40,-33,-36,133,-87,-87,-37,-87,-87,-42,149,151,-5,-58,-57,-34,-35,158,162,-83,-6,173,]),'GREATTHAN':([49,50,51,52,54,55,56,58,60,61,62,63,64,65,82,85,86,87,90,93,118,119,120,122,123,137,140,141,143,144,155,],[-38,-26,-24,-25,-29,-27,-87,-32,-23,-87,-28,-31,-30,97,-39,-56,-59,-40,-33,-36,-87,-87,-37,-87,-87,-5,-58,-57,-34,-35,-83,]),'LESSTHANEQUAL':([49,50,51,52,54,55,56,58,60,61,62,63,64,65,82,85,86,87,90,93,118,119,120,122,123,137,140,141,143,144,155,],[-38,-26,-24,-25,-29,-27,-87,-32,-23,-87,-28,-31,-30,98,-39,-56,-59,-40,-33,-36,-87,-87,-37,-87,-87,-5,-58,-57,-34,-35,-83,]),'LFTBRACSQR':([23,44,60,110,126,],[30,78,78,78,145,]),'PLUS':([29,49,50,51,52,54,55,56,58,59,60,61,62,63,64,73,76,77,78,79,82,83,84,85,86,87,89,90,91,92,93,94,95,96,97,98,99,100,101,102,118,119,120,122,123,135,137,140,141,143,144,155,160,],[57,-38,-26,-24,-25,-29,-27,-87,-32,57,-23,91,-28,-31,-30,57,57,57,57,57,-39,57,57,-56,-59,-40,57,-33,57,57,-36,-43,57,-48,-49,-47,-50,-45,-44,-46,-87,-87,-37,91,91,57,-5,-58,-57,-34,-35,-83,57,]),'COMMA':([49,50,51,52,54,55,56,58,60,61,62,63,64,65,66,82,85,86,87,90,93,106,114,118,119,120,121,122,123,124,137,140,141,143,144,146,153,155,156,168,],[-38,-26,-24,-25,-29,-27,-87,-32,-23,-87,-28,-31,-30,-41,104,-39,-56,-59,-40,-33,-36,127,135,-87,-87,-37,135,-87,-87,-42,-5,-58,-57,-34,-35,159,135,-83,167,-6,]),'$end':([1,28,],[0,-1,]),'FUNCTION':([4,6,10,24,103,125,129,158,161,169,174,],[5,5,5,-75,-76,-77,-72,-78,-12,-79,-13,]),'DIVISION':([49,50,51,52,54,55,56,58,60,62,63,64,82,85,86,87,118,119,120,137,140,141,155,],[-38,-26,-24,-25,-29,-27,83,-32,-23,-28,-31,-30,-39,-56,-59,-40,83,83,-37,-5,-58,-57,-83,]),'STRING':([4,5,6,10,24,26,29,31,32,37,38,39,40,42,45,48,53,57,59,73,74,76,77,78,79,80,81,83,84,89,91,92,94,95,96,97,98,99,100,101,102,103,125,127,128,129,133,135,139,145,149,150,151,154,158,160,161,162,164,165,167,169,171,174,],[11,11,11,11,-75,11,58,11,11,-63,-64,-65,11,-60,-61,-62,58,58,58,58,58,58,58,58,58,-18,-17,58,58,58,58,58,-43,58,-48,-49,-47,-50,-45,-44,-46,-76,-77,11,11,-72,-9,58,-19,58,-84,-51,-52,-87,-78,58,-12,-80,-20,-22,58,-79,-21,-13,]),'RGTBRAC':([21,24,26,27,32,37,38,39,40,41,42,45,47,48,71,75,80,81,103,125,128,133,139,148,149,150,151,154,158,162,164,165,169,171,173,],[28,-75,-87,-71,-87,-63,-64,-65,-87,-16,-60,-61,81,-62,-15,-14,-18,-17,-76,-77,-87,-9,-19,161,-84,-51,-52,-87,-78,-80,-20,-22,-79,-21,174,]),'LFTPAREN':([25,29,33,34,35,44,46,59,60,73,76,77,78,79,83,84,89,91,92,94,95,96,97,98,99,100,101,102,135,160,166,],[31,59,72,73,74,77,79,59,89,59,59,59,59,59,59,59,59,59,59,-43,59,-48,-49,-47,-50,-45,-44,-46,59,59,79,]),'ELSE':([80,81,154,164,165,171,],[117,-17,-87,-20,-22,-21,]),'ELSEIF':([81,154,],[-17,166,]),'GREATTHANEQUAL':([49,50,51,52,54,55,56,58,60,61,62,63,64,65,82,85,86,87,90,93,118,119,120,122,123,137,140,141,143,144,155,],[-38,-26,-24,-25,-29,-27,-87,-32,-23,-87,-28,-31,-30,96,-39,-56,-59,-40,-33,-36,-87,-87,-37,-87,-87,-5,-58,-57,-34,-35,-83,]),'DOUBEQUAL':([49,50,51,52,54,55,56,58,60,61,62,63,64,65,82,85,86,87,90,93,118,119,120,122,123,137,140,141,143,144,155,],[-38,-26,-24,-25,-29,-27,-87,-32,-23,-87,-28,-31,-30,101,-39,-56,-59,-40,-33,-36,-87,-87,-37,-87,-87,-5,-58,-57,-34,-35,-83,]),'ID':([2,7,11,12,13,14,15,16,17,18,24,26,29,32,37,38,39,40,42,45,48,53,57,59,68,72,73,74,76,77,78,79,80,81,83,84,89,91,92,94,95,96,97,98,99,100,101,102,103,104,125,128,133,135,139,145,149,150,151,154,158,159,160,162,164,165,167,169,171,],[3,-68,-70,-66,23,-67,-69,25,-74,-73,-75,44,60,44,-63,-64,-65,44,-60,-61,-62,60,60,60,106,110,60,60,60,60,60,60,-18,-17,60,60,60,60,60,-43,60,-48,-49,-47,-50,-45,-44,-46,-76,23,-77,44,-9,60,-19,60,-84,-51,-52,-87,-78,23,60,-80,-20,-22,60,-79,-21,]),'IF':([24,26,32,37,38,39,40,42,45,48,80,81,103,125,128,133,139,149,150,151,154,158,162,164,165,169,171,],[-75,46,46,-63,-64,-65,46,-60,-61,-62,-18,-17,-76,-77,46,-9,-19,-84,-51,-52,-87,-78,-80,-20,-22,-79,-21,]),'AND':([49,50,51,52,54,55,56,58,60,61,62,63,64,65,82,85,86,87,90,93,118,119,120,122,123,137,140,141,143,144,155,],[-38,-26,-24,-25,-29,-27,-87,-32,-23,-87,-28,-31,-30,94,-39,-56,-59,-40,-33,-36,-87,-87,-37,-87,-87,-5,-58,-57,-34,-35,-83,]),'FALSE':([29,53,57,59,73,74,76,77,78,79,83,84,89,91,92,94,95,96,97,98,99,100,101,102,135,145,160,167,],[62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,-43,62,-48,-49,-47,-50,-45,-44,-46,62,62,62,62,]),'LFTBRAC':([3,20,107,117,131,138,],[4,26,128,26,26,26,]),'INT':([4,5,6,10,24,26,29,30,31,32,37,38,39,40,42,45,48,53,57,59,73,74,76,77,78,79,80,81,83,84,89,91,92,94,95,96,97,98,99,100,101,102,103,125,127,128,129,133,135,139,145,149,150,151,154,158,160,161,162,164,165,167,169,171,174,],[12,12,12,12,-75,12,63,67,12,12,-63,-64,-65,12,-60,-61,-62,63,63,63,63,63,63,63,63,63,-18,-17,63,63,63,63,63,-43,63,-48,-49,-47,-50,-45,-44,-46,-76,-77,12,12,-72,-9,63,-19,63,-84,-51,-52,-87,-78,63,-12,-80,-20,-22,63,-79,-21,-13,]),'FLOAT':([4,5,6,10,24,26,29,31,32,37,38,39,40,42,45,48,53,57,59,73,74,76,77,78,79,80,81,83,84,89,91,92,94,95,96,97,98,99,100,101,102,103,125,127,128,129,133,135,139,145,149,150,151,154,158,160,161,162,164,165,167,169,171,174,],[14,14,14,14,-75,14,64,14,14,-63,-64,-65,14,-60,-61,-62,64,64,64,64,64,64,64,64,64,-18,-17,64,64,64,64,64,-43,64,-48,-49,-47,-50,-45,-44,-46,-76,-77,14,14,-72,-9,64,-19,64,-84,-51,-52,-87,-78,64,-12,-80,-20,-22,64,-79,-21,-13,]),'LESSTHAN':([49,50,51,52,54,55,56,58,60,61,62,63,64,65,82,85,86,87,90,93,118,119,120,122,123,137,140,141,143,144,155,],[-38,-26,-24,-25,-29,-27,-87,-32,-23,-87,-28,-31,-30,99,-39,-56,-59,-40,-33,-36,-87,-87,-37,-87,-87,-5,-58,-57,-34,-35,-83,]),'PRIOMH':([4,6,8,9,10,19,22,24,103,125,129,158,161,169,174,],[-87,-87,20,-4,-87,-2,-3,-75,-76,-77,-72,-78,-12,-79,-13,]),'BOOL':([4,5,6,10,24,26,31,32,37,38,39,40,42,45,48,80,81,103,125,127,128,129,133,139,149,150,151,154,158,161,162,164,165,169,171,174,],[15,15,15,15,-75,15,15,15,-63,-64,-65,15,-60,-61,-62,-18,-17,-76,-77,15,15,-72,-9,-19,-84,-51,-52,-87,-78,-12,-80,-20,-22,-79,-21,-13,]),'NOT':([49,50,51,52,54,55,56,58,60,61,62,63,64,65,82,85,86,87,90,93,118,119,120,122,123,137,140,141,143,144,155,],[-38,-26,-24,-25,-29,-27,-87,-32,-23,-87,-28,-31,-30,100,-39,-56,-59,-40,-33,-36,-87,-87,-37,-87,-87,-5,-58,-57,-34,-35,-83,]),'OR':([49,50,51,52,54,55,56,58,60,61,62,63,64,65,82,85,86,87,90,93,118,119,120,122,123,137,140,141,143,144,155,],[-38,-26,-24,-25,-29,-27,-87,-32,-23,-87,-28,-31,-30,102,-39,-56,-59,-40,-33,-36,-87,-87,-37,-87,-87,-5,-58,-57,-34,-35,-83,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'cteS':([29,53,57,59,73,74,76,77,78,79,83,84,89,91,92,95,135,145,160,167,],[50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,]),'constant':([29,53,57,59,73,74,76,77,78,79,83,84,89,91,92,95,135,145,160,167,],[49,82,87,49,49,112,49,49,49,49,49,49,49,49,49,49,49,156,49,156,]),'vars':([4,6,10,26,32,40,128,],[6,6,6,32,32,32,32,]),'expaux':([61,122,123,],[90,143,144,]),'array':([26,29,32,40,53,57,59,72,73,74,76,77,78,79,83,84,89,91,92,95,128,135,145,160,167,],[36,51,36,36,51,51,51,109,51,51,51,51,51,51,51,51,51,51,51,51,36,51,51,51,51,]),'termaux':([56,118,119,],[85,140,141,]),'cteN':([29,53,57,59,73,74,76,77,78,79,83,84,89,91,92,95,135,145,160,167,],[52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,]),'arrayvaluesaux':([145,167,],[157,172,]),'auxprogram':([4,6,10,],[8,19,22,]),'conditionaux2':([154,],[164,]),'call2':([29,53,57,59,73,74,76,77,78,79,83,84,89,91,92,95,135,145,160,167,],[54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,]),'functionaux':([5,],[16,]),'write':([26,32,40,128,],[37,37,37,37,]),'program':([0,],[1,]),'call':([26,32,40,128,],[39,39,39,39,]),'statement':([26,32,40,128,],[40,40,40,40,]),'factor':([29,59,73,76,77,78,79,83,84,89,91,92,95,135,160,],[56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,]),'arrayvalues':([126,],[146,]),'main':([8,],[21,]),'type':([4,5,6,10,26,31,32,40,127,128,],[13,17,13,13,13,68,13,13,68,13,]),'empty':([4,6,10,26,31,32,40,56,61,114,118,119,121,122,123,127,128,153,154,],[9,9,9,41,70,41,41,86,93,136,86,86,136,93,93,70,41,136,165,]),'function':([4,6,10,],[10,10,10,]),'expressionaux':([65,],[95,]),'read':([26,32,40,128,],[38,38,38,38,]),'assignment':([26,32,40,128,],[42,42,42,42,]),'callaux':([114,121,153,],[134,142,163,]),'readaux':([72,],[108,]),'assignmentaux':([26,32,40,128,],[43,43,43,43,]),'condition':([26,32,40,128,],[45,45,45,45,]),'term':([29,59,73,76,77,78,79,83,84,89,91,92,95,135,160,],[61,61,61,61,61,61,61,118,119,61,61,61,61,61,61,]),'parameter':([31,127,],[69,147,]),'blockneutral':([26,32,40,128,],[47,71,75,148,]),'blockreturn':([107,],[129,]),'block':([20,117,131,138,],[27,139,150,154,]),'exp':([29,59,73,76,77,78,79,89,91,92,95,135,160,],[65,65,65,65,114,115,65,121,122,123,124,153,170,]),'conditionaux':([46,166,],[80,171,]),'expression':([29,59,73,76,79,],[66,88,111,113,116,]),'loop':([26,32,40,128,],[48,48,48,48,]),'varsaux':([13,104,159,],[24,125,169,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID LFTBRAC auxprogram main RGTBRAC','program',6,'p_program','Yaotecatl.py',86),
  ('auxprogram -> vars auxprogram','auxprogram',2,'p_auxprogram','Yaotecatl.py',88),
  ('auxprogram -> function auxprogram','auxprogram',2,'p_auxprogram','Yaotecatl.py',89),
  ('auxprogram -> empty','auxprogram',1,'p_auxprogram','Yaotecatl.py',90),
  ('array -> ID LFTBRACSQR exp RGTBRACSQR','array',4,'p_array','Yaotecatl.py',93),
  ('arrayvalues -> LFTBRACSQR arrayvaluesaux RGTBRACSQR','arrayvalues',3,'p_arrayvalues','Yaotecatl.py',96),
  ('arrayvaluesaux -> constant','arrayvaluesaux',1,'p_arrayvaluesaux','Yaotecatl.py',98),
  ('arrayvaluesaux -> constant COMMA arrayvaluesaux','arrayvaluesaux',3,'p_arrayvaluesaux','Yaotecatl.py',99),
  ('assignment -> assignmentaux EQUAL expression SEMICOLON','assignment',4,'p_assignment','Yaotecatl.py',102),
  ('assignmentaux -> ID','assignmentaux',1,'p_assignmentaux','Yaotecatl.py',104),
  ('assignmentaux -> array','assignmentaux',1,'p_assignmentaux','Yaotecatl.py',105),
  ('blockreturn -> LFTBRAC blockneutral RGTBRAC','blockreturn',3,'p_blockreturn','Yaotecatl.py',108),
  ('blockreturn -> LFTBRAC blockneutral RETURN exp SEMICOLON RGTBRAC','blockreturn',6,'p_blockreturn','Yaotecatl.py',109),
  ('blockneutral -> statement blockneutral','blockneutral',2,'p_blockneutral','Yaotecatl.py',111),
  ('blockneutral -> vars blockneutral','blockneutral',2,'p_blockneutral','Yaotecatl.py',112),
  ('blockneutral -> empty','blockneutral',1,'p_blockneutral','Yaotecatl.py',113),
  ('block -> LFTBRAC blockneutral RGTBRAC','block',3,'p_block','Yaotecatl.py',116),
  ('condition -> IF conditionaux','condition',2,'p_condition','Yaotecatl.py',119),
  ('condition -> IF conditionaux ELSE block','condition',4,'p_condition','Yaotecatl.py',120),
  ('conditionaux -> LFTPAREN expression RGTPAREN block conditionaux2','conditionaux',5,'p_conditionaux','Yaotecatl.py',122),
  ('conditionaux2 -> ELSEIF conditionaux','conditionaux2',2,'p_conditionaux2','Yaotecatl.py',124),
  ('conditionaux2 -> empty','conditionaux2',1,'p_conditionaux2','Yaotecatl.py',125),
  ('constant -> ID','constant',1,'p_constant','Yaotecatl.py',129),
  ('constant -> array','constant',1,'p_constant','Yaotecatl.py',130),
  ('constant -> cteN','constant',1,'p_constant','Yaotecatl.py',131),
  ('constant -> cteS','constant',1,'p_constant','Yaotecatl.py',132),
  ('constant -> TRUE','constant',1,'p_constant','Yaotecatl.py',133),
  ('constant -> FALSE','constant',1,'p_constant','Yaotecatl.py',134),
  ('constant -> call2','constant',1,'p_constant','Yaotecatl.py',135),
  ('cteN -> FLOAT','cteN',1,'p_cteN','Yaotecatl.py',138),
  ('cteN -> INT','cteN',1,'p_cteN','Yaotecatl.py',139),
  ('cteS -> STRING','cteS',1,'p_cteS','Yaotecatl.py',142),
  ('exp -> term expaux','exp',2,'p_exp','Yaotecatl.py',145),
  ('expaux -> PLUS exp expaux','expaux',3,'p_expaux','Yaotecatl.py',147),
  ('expaux -> MINUS exp expaux','expaux',3,'p_expaux','Yaotecatl.py',148),
  ('expaux -> empty','expaux',1,'p_expaux','Yaotecatl.py',149),
  ('factor -> LFTPAREN expression RGTPAREN','factor',3,'p_factor','Yaotecatl.py',152),
  ('factor -> constant','factor',1,'p_factor','Yaotecatl.py',153),
  ('factor -> MINUS constant','factor',2,'p_factor','Yaotecatl.py',154),
  ('factor -> PLUS constant','factor',2,'p_factor','Yaotecatl.py',155),
  ('expression -> exp','expression',1,'p_expression','Yaotecatl.py',158),
  ('expression -> exp expressionaux exp','expression',3,'p_expression','Yaotecatl.py',159),
  ('expressionaux -> AND','expressionaux',1,'p_expressionaux','Yaotecatl.py',161),
  ('expressionaux -> DOUBEQUAL','expressionaux',1,'p_expressionaux','Yaotecatl.py',162),
  ('expressionaux -> NOT','expressionaux',1,'p_expressionaux','Yaotecatl.py',163),
  ('expressionaux -> OR','expressionaux',1,'p_expressionaux','Yaotecatl.py',164),
  ('expressionaux -> LESSTHANEQUAL','expressionaux',1,'p_expressionaux','Yaotecatl.py',165),
  ('expressionaux -> GREATTHANEQUAL','expressionaux',1,'p_expressionaux','Yaotecatl.py',166),
  ('expressionaux -> GREATTHAN','expressionaux',1,'p_expressionaux','Yaotecatl.py',167),
  ('expressionaux -> LESSTHAN','expressionaux',1,'p_expressionaux','Yaotecatl.py',168),
  ('loop -> WHILE LFTPAREN expression RGTPAREN block','loop',5,'p_loop','Yaotecatl.py',171),
  ('write -> PRINT LFTPAREN constant RGTPAREN SEMICOLON','write',5,'p_write','Yaotecatl.py',174),
  ('parameter -> type ID','parameter',2,'p_parameter','Yaotecatl.py',177),
  ('parameter -> type ID COMMA parameter','parameter',4,'p_parameter','Yaotecatl.py',178),
  ('parameter -> empty','parameter',1,'p_parameter','Yaotecatl.py',179),
  ('term -> factor termaux','term',2,'p_term','Yaotecatl.py',182),
  ('termaux -> MULTIPLICATION term termaux','termaux',3,'p_termaux','Yaotecatl.py',184),
  ('termaux -> DIVISION term termaux','termaux',3,'p_termaux','Yaotecatl.py',185),
  ('termaux -> empty','termaux',1,'p_termaux','Yaotecatl.py',186),
  ('statement -> assignment','statement',1,'p_statement','Yaotecatl.py',189),
  ('statement -> condition','statement',1,'p_statement','Yaotecatl.py',190),
  ('statement -> loop','statement',1,'p_statement','Yaotecatl.py',191),
  ('statement -> write','statement',1,'p_statement','Yaotecatl.py',192),
  ('statement -> read','statement',1,'p_statement','Yaotecatl.py',193),
  ('statement -> call','statement',1,'p_statement','Yaotecatl.py',194),
  ('type -> INT','type',1,'p_type','Yaotecatl.py',197),
  ('type -> FLOAT','type',1,'p_type','Yaotecatl.py',198),
  ('type -> CHAR','type',1,'p_type','Yaotecatl.py',199),
  ('type -> BOOL','type',1,'p_type','Yaotecatl.py',200),
  ('type -> STRING','type',1,'p_type','Yaotecatl.py',201),
  ('main -> PRIOMH block','main',2,'p_main','Yaotecatl.py',204),
  ('function -> FUNCTION functionaux ID LFTPAREN parameter RGTPAREN blockreturn','function',7,'p_function','Yaotecatl.py',207),
  ('functionaux -> VOID','functionaux',1,'p_functionaux','Yaotecatl.py',209),
  ('functionaux -> type','functionaux',1,'p_functionaux','Yaotecatl.py',210),
  ('vars -> type varsaux','vars',2,'p_vars','Yaotecatl.py',213),
  ('varsaux -> ID EQUAL expression SEMICOLON','varsaux',4,'p_varsaux','Yaotecatl.py',215),
  ('varsaux -> ID EQUAL expression COMMA varsaux','varsaux',5,'p_varsaux','Yaotecatl.py',216),
  ('varsaux -> ID LFTBRACSQR INT RGTBRACSQR EQUAL arrayvalues SEMICOLON','varsaux',7,'p_varsaux','Yaotecatl.py',217),
  ('varsaux -> ID LFTBRACSQR INT RGTBRACSQR EQUAL arrayvalues COMMA varsaux','varsaux',8,'p_varsaux','Yaotecatl.py',218),
  ('call -> ID LFTPAREN exp callaux RGTPAREN SEMICOLON','call',6,'p_call','Yaotecatl.py',221),
  ('callaux -> COMMA exp callaux','callaux',3,'p_callaux','Yaotecatl.py',223),
  ('callaux -> empty','callaux',1,'p_callaux','Yaotecatl.py',224),
  ('call2 -> ID LFTPAREN exp callaux RGTPAREN','call2',5,'p_call2','Yaotecatl.py',227),
  ('read -> READ LFTPAREN readaux RGTPAREN SEMICOLON','read',5,'p_read','Yaotecatl.py',230),
  ('readaux -> ID','readaux',1,'p_readaux','Yaotecatl.py',232),
  ('readaux -> array','readaux',1,'p_readaux','Yaotecatl.py',233),
  ('empty -> <empty>','empty',0,'p_empty','Yaotecatl.py',236),
]
