
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'LFTBRAC RGTBRAC LFTPAREN RGTPAREN LFTBRACSQR RGTBRACSQR AND DOUBEQUAL NOT OR SEMICOLON EQUAL LESSTHANEQUAL GREATTHANEQUAL GREATTHAN LESSTHAN PLUS MINUS MULTIPLICATION DIVISION ID COMMA FUNCTION CHAR INT FALSE STRING READ VOID FLOAT PRIOMH WRITE PRINT WHILE PROGRAM BOOL ELSEIF RETURN ARRAY ELSE TRUE IFprogram : PROGRAM ID LFTBRAC auxprogram main RGTBRACauxprogram : vars auxprogram \n    | function auxprogram \n    | emptyarray : ID LFTBRACSQR exp RGTBRACSQRarrayvalues : LFTBRACSQR arrayvaluesaux RGTBRACSQR arrayvaluesaux : cteN arrayvaluesaux2\n    | cteS arrayvaluesaux2 arrayvaluesaux2 : COMMA arrayvaluesaux\n    | emptyassignment : assignmentaux EQUAL expression SEMICOLON \n    | assignmentaux EQUAL call assignmentaux : ID \n    | arrayblockreturn : LFTBRAC blockreturnaux RGTBRAC \n    | LFTBRAC blockreturnaux RETURN exp SEMICOLON RGTBRAC blockreturnaux : statement blockreturnaux \n    | empty block : LFTBRAC blockaux RGTBRACblockaux : statement blockaux \n    | empty condition : IF conditionaux \n    | IF conditionaux ELSE block conditionaux : LFTPAREN expression RGTPAREN block ELSEIF conditionaux \n    | LFTPAREN expression RGTPAREN block constant : ID \n    | array \n    | cteN\n    | cteS\n    | TRUE \n    | FALSE cteN : FLOAT \n    | INTcteS : STRINGexp : term \n    | term expaux  expaux : PLUS exp expaux \n    | MINUS exp expaux \n    | empty factor : factoraux constant \n    | LFTPAREN expression RGTPAREN factoraux : PLUS \n    | MINUS \n    | emptyexpression : exp \n    | exp expressionaux exp expressionaux : AND \n    | DOUBEQUAL \n    | NOT \n    | OR \n    | LESSTHANEQUAL \n    | GREATTHANEQUAL \n    | GREATTHAN \n    | LESSTHAN loop : WHILE LFTPAREN expression RGTPAREN block write : PRINT LFTPAREN constant RGTPAREN SEMICOLON parameter : type ID \n    | type ID COMMA parameter \n    | empty  term : factor termaux  termaux : MULTIPLICATION term termaux \n    | DIVISION term termaux \n    | empty  statement : assignment \n    | condition \n    | vars \n    | loop \n    | write \n    | read \n    | call  type : INT \n    | FLOAT \n    | CHAR \n    | BOOL \n    | STRING  main : PRIOMH block  function : FUNCTION functionaux ID LFTPAREN functionaux2 RGTPAREN blockreturn  functionaux : VOID \n    | type  functionaux2 : parameter \n    | empty  vars : type varsaux     varsaux : ID EQUAL expression SEMICOLON\n    | ID EQUAL call \n    | ID EQUAL expression COMMA varsaux \n    | ID LFTBRACSQR INT RGTBRACSQR EQUAL arrayvalues SEMICOLON\n    | ID LFTBRACSQR INT RGTBRACSQR EQUAL arrayvalues COMMA varsaux call : ID LFTPAREN exp RGTPAREN SEMICOLON \n    | ID LFTPAREN exp callaux RGTPAREN SEMICOLON  callaux : COMMA exp callaux\n    | empty read : READ LFTPAREN ID RGTPAREN SEMICOLON empty :'
    
_lr_action_items = {'RGTPAREN':([31,50,54,55,62,63,64,75,78,79,91,92,93,94,95,96,97,98,99,100,101,102,106,108,109,110,113,115,117,118,119,120,121,122,125,133,135,136,139,140,141,142,145,146,155,166,],[-93,-35,-45,-93,107,-80,-59,-36,-39,119,-60,-63,-29,-40,-34,-33,-30,-32,-31,-27,-28,-26,-57,128,129,130,132,137,-93,-93,-41,-46,-93,-93,-93,154,-91,-5,-37,-38,-62,-61,-58,-59,-93,-90,]),'RETURN':([23,32,37,38,39,43,46,48,53,69,74,103,111,123,126,131,138,147,148,149,150,151,152,153,156,160,162,165,173,175,],[-82,-66,-68,-69,-70,-64,-65,-67,-84,-19,-22,-83,-12,-85,-93,-11,-23,-93,163,-18,-92,-55,-56,-88,-25,-86,-17,-89,-87,-24,]),'READ':([23,26,32,37,38,39,40,43,46,48,53,69,74,103,111,123,126,131,138,147,150,151,152,153,156,160,165,173,175,],[-82,33,-66,-68,-69,-70,33,-64,-65,-67,-84,-19,-22,-83,-12,-85,33,-11,-23,33,-92,-55,-56,-88,-25,-86,-89,-87,-24,]),'VOID':([5,],[16,]),'EQUAL':([22,36,44,45,105,136,],[29,-14,70,-13,124,-5,]),'CHAR':([4,5,6,11,23,26,31,32,37,38,39,40,43,46,48,53,69,74,103,111,123,125,126,127,131,138,147,150,151,152,153,156,160,164,165,173,175,178,],[7,7,7,7,-82,7,7,-66,-68,-69,-70,7,-64,-65,-67,-84,-19,-22,-83,-12,-85,7,7,-77,-11,-23,7,-92,-55,-56,-88,-25,-86,-15,-89,-87,-24,-16,]),'MULTIPLICATION':([55,91,92,93,94,95,96,97,98,99,100,101,102,119,121,122,136,141,142,],[90,-60,-63,-29,-40,-34,-33,-30,-32,-31,-27,-28,-26,-41,90,90,-5,-62,-61,]),'WHILE':([23,26,32,37,38,39,40,43,46,48,53,69,74,103,111,123,126,131,138,147,150,151,152,153,156,160,165,173,175,],[-82,34,-66,-68,-69,-70,34,-64,-65,-67,-84,-19,-22,-83,-12,-85,34,-11,-23,34,-92,-55,-56,-88,-25,-86,-89,-87,-24,]),'PROGRAM':([0,],[2,]),'PRINT':([23,26,32,37,38,39,40,43,46,48,53,69,74,103,111,123,126,131,138,147,150,151,152,153,156,160,165,173,175,],[-82,35,-66,-68,-69,-70,35,-64,-65,-67,-84,-19,-22,-83,-12,-85,35,-11,-23,35,-92,-55,-56,-88,-25,-86,-89,-87,-24,]),'RGTBRACSQR':([50,55,60,75,78,91,92,93,94,95,96,97,98,99,100,101,102,114,117,118,119,121,122,136,139,140,141,142,157,158,159,169,170,171,176,],[-35,-93,105,-36,-39,-60,-63,-29,-40,-34,-33,-30,-32,-31,-27,-28,-26,136,-93,-93,-41,-93,-93,-5,-37,-38,-62,-61,-93,-93,172,-10,-8,-7,-9,]),'TRUE':([29,49,51,52,56,59,66,67,70,71,72,73,76,77,80,81,82,83,84,85,86,87,88,89,90,134,163,],[-93,-42,-93,-43,97,-44,-93,97,-93,-93,-93,-93,-93,-93,-47,-93,-52,-53,-51,-54,-49,-48,-50,-93,-93,-93,-93,]),'MINUS':([29,50,51,55,66,70,71,72,73,75,76,77,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,117,118,119,121,122,134,136,139,140,141,142,163,],[52,77,52,-93,52,52,52,52,52,-36,52,52,-39,-47,52,-52,-53,-51,-54,-49,-48,-50,52,52,-60,-63,-29,-40,-34,-33,-30,-32,-31,-27,-28,-26,77,77,-41,-93,-93,52,-5,-37,-38,-62,-61,52,]),'SEMICOLON':([50,54,55,57,75,78,91,92,93,94,95,96,97,98,99,100,101,102,112,117,118,119,120,121,122,128,130,132,136,139,140,141,142,144,154,172,174,],[-35,-45,-93,103,-36,-39,-60,-63,-29,-40,-34,-33,-30,-32,-31,-27,-28,-26,131,-93,-93,-41,-46,-93,-93,150,152,153,-5,-37,-38,-62,-61,160,165,-6,177,]),'GREATTHAN':([50,54,55,75,78,91,92,93,94,95,96,97,98,99,100,101,102,117,118,119,121,122,136,139,140,141,142,],[-35,83,-93,-36,-39,-60,-63,-29,-40,-34,-33,-30,-32,-31,-27,-28,-26,-93,-93,-41,-93,-93,-5,-37,-38,-62,-61,]),'LESSTHANEQUAL':([50,54,55,75,78,91,92,93,94,95,96,97,98,99,100,101,102,117,118,119,121,122,136,139,140,141,142,],[-35,84,-93,-36,-39,-60,-63,-29,-40,-34,-33,-30,-32,-31,-27,-28,-26,-93,-93,-41,-93,-93,-5,-37,-38,-62,-61,]),'LFTBRACSQR':([22,45,102,124,],[30,72,72,143,]),'PLUS':([29,50,51,55,66,70,71,72,73,75,76,77,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,117,118,119,121,122,134,136,139,140,141,142,163,],[49,76,49,-93,49,49,49,49,49,-36,49,49,-39,-47,49,-52,-53,-51,-54,-49,-48,-50,49,49,-60,-63,-29,-40,-34,-33,-30,-32,-31,-27,-28,-26,76,76,-41,-93,-93,49,-5,-37,-38,-62,-61,49,]),'COMMA':([50,54,55,57,75,78,91,92,93,94,95,96,97,98,99,100,101,102,106,113,117,118,119,120,121,122,136,139,140,141,142,144,155,157,158,172,],[-35,-45,-93,104,-36,-39,-60,-63,-29,-40,-34,-33,-30,-32,-31,-27,-28,-26,125,134,-93,-93,-41,-46,-93,-93,-5,-37,-38,-62,-61,161,134,168,168,-6,]),'$end':([1,28,],[0,-1,]),'FUNCTION':([4,6,11,23,53,103,123,127,153,160,164,165,173,178,],[5,5,5,-82,-84,-83,-85,-77,-88,-86,-15,-89,-87,-16,]),'DIVISION':([55,91,92,93,94,95,96,97,98,99,100,101,102,119,121,122,136,141,142,],[89,-60,-63,-29,-40,-34,-33,-30,-32,-31,-27,-28,-26,-41,89,89,-5,-62,-61,]),'STRING':([4,5,6,11,23,26,29,31,32,37,38,39,40,43,46,48,49,51,52,53,56,59,66,67,69,70,71,72,73,74,76,77,80,81,82,83,84,85,86,87,88,89,90,103,111,123,125,126,127,131,134,138,143,147,150,151,152,153,156,160,163,164,165,168,173,175,178,],[12,12,12,12,-82,12,-93,12,-66,-68,-69,-70,12,-64,-65,-67,-42,-93,-43,-84,95,-44,-93,95,-19,-93,-93,-93,-93,-22,-93,-93,-47,-93,-52,-53,-51,-54,-49,-48,-50,-93,-93,-83,-12,-85,12,12,-77,-11,-93,-23,95,12,-92,-55,-56,-88,-25,-86,-93,-15,-89,95,-87,-24,-16,]),'RGTBRAC':([21,23,26,27,32,37,38,39,40,41,42,43,46,48,53,68,69,74,103,111,123,126,131,138,147,148,149,150,151,152,153,156,160,162,165,173,175,177,],[28,-82,-93,-76,-66,-68,-69,-70,-93,-21,69,-64,-65,-67,-84,-20,-19,-22,-83,-12,-85,-93,-11,-23,-93,164,-18,-92,-55,-56,-88,-25,-86,-17,-89,-87,-24,178,]),'LFTPAREN':([25,29,33,34,35,45,47,51,58,66,70,71,72,73,76,77,80,81,82,83,84,85,86,87,88,89,90,134,163,167,],[31,51,65,66,67,71,73,51,71,51,51,51,51,51,51,51,-47,51,-52,-53,-51,-54,-49,-48,-50,51,51,51,51,73,]),'ELSE':([69,74,156,175,],[-19,116,-25,-24,]),'ELSEIF':([69,156,],[-19,167,]),'GREATTHANEQUAL':([50,54,55,75,78,91,92,93,94,95,96,97,98,99,100,101,102,117,118,119,121,122,136,139,140,141,142,],[-35,82,-93,-36,-39,-60,-63,-29,-40,-34,-33,-30,-32,-31,-27,-28,-26,-93,-93,-41,-93,-93,-5,-37,-38,-62,-61,]),'DOUBEQUAL':([50,54,55,75,78,91,92,93,94,95,96,97,98,99,100,101,102,117,118,119,121,122,136,139,140,141,142,],[-35,87,-93,-36,-39,-60,-63,-29,-40,-34,-33,-30,-32,-31,-27,-28,-26,-93,-93,-41,-93,-93,-5,-37,-38,-62,-61,]),'ID':([2,7,9,12,13,14,15,16,17,18,23,26,29,32,37,38,39,40,43,46,48,49,51,52,53,56,59,61,65,66,67,69,70,71,72,73,74,76,77,80,81,82,83,84,85,86,87,88,89,90,103,104,111,123,126,131,134,138,147,150,151,152,153,156,160,161,163,165,173,175,],[3,-73,22,-75,-71,-72,-74,-78,25,-79,-82,45,58,-66,-68,-69,-70,45,-64,-65,-67,-42,-93,-43,-84,102,-44,106,108,-93,102,-19,58,-93,-93,-93,-22,-93,-93,-47,-93,-52,-53,-51,-54,-49,-48,-50,-93,-93,-83,22,-12,-85,45,-11,-93,-23,45,-92,-55,-56,-88,-25,-86,22,-93,-89,-87,-24,]),'IF':([23,26,32,37,38,39,40,43,46,48,53,69,74,103,111,123,126,131,138,147,150,151,152,153,156,160,165,173,175,],[-82,47,-66,-68,-69,-70,47,-64,-65,-67,-84,-19,-22,-83,-12,-85,47,-11,-23,47,-92,-55,-56,-88,-25,-86,-89,-87,-24,]),'AND':([50,54,55,75,78,91,92,93,94,95,96,97,98,99,100,101,102,117,118,119,121,122,136,139,140,141,142,],[-35,80,-93,-36,-39,-60,-63,-29,-40,-34,-33,-30,-32,-31,-27,-28,-26,-93,-93,-41,-93,-93,-5,-37,-38,-62,-61,]),'FALSE':([29,49,51,52,56,59,66,67,70,71,72,73,76,77,80,81,82,83,84,85,86,87,88,89,90,134,163,],[-93,-42,-93,-43,99,-44,-93,99,-93,-93,-93,-93,-93,-93,-47,-93,-52,-53,-51,-54,-49,-48,-50,-93,-93,-93,-93,]),'LFTBRAC':([3,20,107,116,129,137,],[4,26,126,26,26,26,]),'INT':([4,5,6,11,23,26,29,30,31,32,37,38,39,40,43,46,48,49,51,52,53,56,59,66,67,69,70,71,72,73,74,76,77,80,81,82,83,84,85,86,87,88,89,90,103,111,123,125,126,127,131,134,138,143,147,150,151,152,153,156,160,163,164,165,168,173,175,178,],[13,13,13,13,-82,13,-93,60,13,-66,-68,-69,-70,13,-64,-65,-67,-42,-93,-43,-84,96,-44,-93,96,-19,-93,-93,-93,-93,-22,-93,-93,-47,-93,-52,-53,-51,-54,-49,-48,-50,-93,-93,-83,-12,-85,13,13,-77,-11,-93,-23,96,13,-92,-55,-56,-88,-25,-86,-93,-15,-89,96,-87,-24,-16,]),'FLOAT':([4,5,6,11,23,26,29,31,32,37,38,39,40,43,46,48,49,51,52,53,56,59,66,67,69,70,71,72,73,74,76,77,80,81,82,83,84,85,86,87,88,89,90,103,111,123,125,126,127,131,134,138,143,147,150,151,152,153,156,160,163,164,165,168,173,175,178,],[14,14,14,14,-82,14,-93,14,-66,-68,-69,-70,14,-64,-65,-67,-42,-93,-43,-84,98,-44,-93,98,-19,-93,-93,-93,-93,-22,-93,-93,-47,-93,-52,-53,-51,-54,-49,-48,-50,-93,-93,-83,-12,-85,14,14,-77,-11,-93,-23,98,14,-92,-55,-56,-88,-25,-86,-93,-15,-89,98,-87,-24,-16,]),'LESSTHAN':([50,54,55,75,78,91,92,93,94,95,96,97,98,99,100,101,102,117,118,119,121,122,136,139,140,141,142,],[-35,85,-93,-36,-39,-60,-63,-29,-40,-34,-33,-30,-32,-31,-27,-28,-26,-93,-93,-41,-93,-93,-5,-37,-38,-62,-61,]),'PRIOMH':([4,6,8,10,11,19,23,24,53,103,123,127,153,160,164,165,173,178,],[-93,-93,20,-4,-93,-2,-82,-3,-84,-83,-85,-77,-88,-86,-15,-89,-87,-16,]),'BOOL':([4,5,6,11,23,26,31,32,37,38,39,40,43,46,48,53,69,74,103,111,123,125,126,127,131,138,147,150,151,152,153,156,160,164,165,173,175,178,],[15,15,15,15,-82,15,15,-66,-68,-69,-70,15,-64,-65,-67,-84,-19,-22,-83,-12,-85,15,15,-77,-11,-23,15,-92,-55,-56,-88,-25,-86,-15,-89,-87,-24,-16,]),'NOT':([50,54,55,75,78,91,92,93,94,95,96,97,98,99,100,101,102,117,118,119,121,122,136,139,140,141,142,],[-35,86,-93,-36,-39,-60,-63,-29,-40,-34,-33,-30,-32,-31,-27,-28,-26,-93,-93,-41,-93,-93,-5,-37,-38,-62,-61,]),'OR':([50,54,55,75,78,91,92,93,94,95,96,97,98,99,100,101,102,117,118,119,121,122,136,139,140,141,142,],[-35,88,-93,-36,-39,-60,-63,-29,-40,-34,-33,-30,-32,-31,-27,-28,-26,-93,-93,-41,-93,-93,-5,-37,-38,-62,-61,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'cteS':([56,67,143,168,],[93,93,157,157,]),'constant':([56,67,],[94,110,]),'vars':([4,6,11,26,40,126,147,],[6,6,6,32,32,32,32,]),'expaux':([50,117,118,],[75,139,140,]),'factoraux':([29,51,66,70,71,72,73,76,77,81,89,90,134,163,],[56,56,56,56,56,56,56,56,56,56,56,56,56,56,]),'array':([26,40,56,67,126,147,],[36,36,100,100,36,36,]),'termaux':([55,121,122,],[91,141,142,]),'cteN':([56,67,143,168,],[101,101,158,158,]),'arrayvaluesaux':([143,168,],[159,176,]),'auxprogram':([4,6,11,],[8,19,24,]),'functionaux':([5,],[17,]),'write':([26,40,126,147,],[37,37,37,37,]),'program':([0,],[1,]),'call':([26,29,40,70,126,147,],[39,53,39,111,39,39,]),'statement':([26,40,126,147,],[40,40,147,147,]),'factor':([29,51,66,70,71,72,73,76,77,81,89,90,134,163,],[55,55,55,55,55,55,55,55,55,55,55,55,55,55,]),'arrayvalues':([124,],[144,]),'main':([8,],[21,]),'type':([4,5,6,11,26,31,40,125,126,147,],[9,18,9,9,9,61,9,61,9,9,]),'empty':([4,6,11,26,29,31,40,50,51,55,66,70,71,72,73,76,77,81,89,90,113,117,118,121,122,125,126,134,147,155,157,158,163,],[10,10,10,41,59,64,41,78,59,92,59,59,59,59,59,59,59,59,59,59,135,78,78,92,92,146,149,59,149,135,169,169,59,]),'blockaux':([26,40,],[42,68,]),'function':([4,6,11,],[11,11,11,]),'expressionaux':([54,],[81,]),'read':([26,40,126,147,],[38,38,38,38,]),'assignment':([26,40,126,147,],[43,43,43,43,]),'blockreturnaux':([126,147,],[148,162,]),'callaux':([113,155,],[133,166,]),'arrayvaluesaux2':([157,158,],[170,171,]),'assignmentaux':([26,40,126,147,],[44,44,44,44,]),'functionaux2':([31,],[62,]),'condition':([26,40,126,147,],[46,46,46,46,]),'term':([29,51,66,70,71,72,73,76,77,81,89,90,134,163,],[50,50,50,50,50,50,50,50,50,50,121,122,50,50,]),'parameter':([31,125,],[63,145,]),'blockreturn':([107,],[127,]),'block':([20,116,129,137,],[27,138,151,156,]),'exp':([29,51,66,70,71,72,73,76,77,81,134,163,],[54,54,54,54,113,114,54,117,118,120,155,174,]),'conditionaux':([47,167,],[74,175,]),'expression':([29,51,66,70,73,],[57,79,109,112,115,]),'loop':([26,40,126,147,],[48,48,48,48,]),'varsaux':([9,104,161,],[23,123,173,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID LFTBRAC auxprogram main RGTBRAC','program',6,'p_program','Yaotecatl.py',88),
  ('auxprogram -> vars auxprogram','auxprogram',2,'p_auxprogram','Yaotecatl.py',90),
  ('auxprogram -> function auxprogram','auxprogram',2,'p_auxprogram','Yaotecatl.py',91),
  ('auxprogram -> empty','auxprogram',1,'p_auxprogram','Yaotecatl.py',92),
  ('array -> ID LFTBRACSQR exp RGTBRACSQR','array',4,'p_array','Yaotecatl.py',95),
  ('arrayvalues -> LFTBRACSQR arrayvaluesaux RGTBRACSQR','arrayvalues',3,'p_arrayvalues','Yaotecatl.py',98),
  ('arrayvaluesaux -> cteN arrayvaluesaux2','arrayvaluesaux',2,'p_arrayvaluesaux','Yaotecatl.py',100),
  ('arrayvaluesaux -> cteS arrayvaluesaux2','arrayvaluesaux',2,'p_arrayvaluesaux','Yaotecatl.py',101),
  ('arrayvaluesaux2 -> COMMA arrayvaluesaux','arrayvaluesaux2',2,'p_arrayvaluesaux2','Yaotecatl.py',103),
  ('arrayvaluesaux2 -> empty','arrayvaluesaux2',1,'p_arrayvaluesaux2','Yaotecatl.py',104),
  ('assignment -> assignmentaux EQUAL expression SEMICOLON','assignment',4,'p_assignment','Yaotecatl.py',107),
  ('assignment -> assignmentaux EQUAL call','assignment',3,'p_assignment','Yaotecatl.py',108),
  ('assignmentaux -> ID','assignmentaux',1,'p_assignmentaux','Yaotecatl.py',110),
  ('assignmentaux -> array','assignmentaux',1,'p_assignmentaux','Yaotecatl.py',111),
  ('blockreturn -> LFTBRAC blockreturnaux RGTBRAC','blockreturn',3,'p_blockreturn','Yaotecatl.py',114),
  ('blockreturn -> LFTBRAC blockreturnaux RETURN exp SEMICOLON RGTBRAC','blockreturn',6,'p_blockreturn','Yaotecatl.py',115),
  ('blockreturnaux -> statement blockreturnaux','blockreturnaux',2,'p_blockreturnaux','Yaotecatl.py',117),
  ('blockreturnaux -> empty','blockreturnaux',1,'p_blockreturnaux','Yaotecatl.py',118),
  ('block -> LFTBRAC blockaux RGTBRAC','block',3,'p_block','Yaotecatl.py',121),
  ('blockaux -> statement blockaux','blockaux',2,'p_blockaux','Yaotecatl.py',123),
  ('blockaux -> empty','blockaux',1,'p_blockaux','Yaotecatl.py',124),
  ('condition -> IF conditionaux','condition',2,'p_condition','Yaotecatl.py',127),
  ('condition -> IF conditionaux ELSE block','condition',4,'p_condition','Yaotecatl.py',128),
  ('conditionaux -> LFTPAREN expression RGTPAREN block ELSEIF conditionaux','conditionaux',6,'p_conditionaux','Yaotecatl.py',130),
  ('conditionaux -> LFTPAREN expression RGTPAREN block','conditionaux',4,'p_conditionaux','Yaotecatl.py',131),
  ('constant -> ID','constant',1,'p_constant','Yaotecatl.py',134),
  ('constant -> array','constant',1,'p_constant','Yaotecatl.py',135),
  ('constant -> cteN','constant',1,'p_constant','Yaotecatl.py',136),
  ('constant -> cteS','constant',1,'p_constant','Yaotecatl.py',137),
  ('constant -> TRUE','constant',1,'p_constant','Yaotecatl.py',138),
  ('constant -> FALSE','constant',1,'p_constant','Yaotecatl.py',139),
  ('cteN -> FLOAT','cteN',1,'p_cteN','Yaotecatl.py',142),
  ('cteN -> INT','cteN',1,'p_cteN','Yaotecatl.py',143),
  ('cteS -> STRING','cteS',1,'p_cteS','Yaotecatl.py',146),
  ('exp -> term','exp',1,'p_exp','Yaotecatl.py',149),
  ('exp -> term expaux','exp',2,'p_exp','Yaotecatl.py',150),
  ('expaux -> PLUS exp expaux','expaux',3,'p_expaux','Yaotecatl.py',152),
  ('expaux -> MINUS exp expaux','expaux',3,'p_expaux','Yaotecatl.py',153),
  ('expaux -> empty','expaux',1,'p_expaux','Yaotecatl.py',154),
  ('factor -> factoraux constant','factor',2,'p_factor','Yaotecatl.py',157),
  ('factor -> LFTPAREN expression RGTPAREN','factor',3,'p_factor','Yaotecatl.py',158),
  ('factoraux -> PLUS','factoraux',1,'p_factoraux','Yaotecatl.py',160),
  ('factoraux -> MINUS','factoraux',1,'p_factoraux','Yaotecatl.py',161),
  ('factoraux -> empty','factoraux',1,'p_factoraux','Yaotecatl.py',162),
  ('expression -> exp','expression',1,'p_expression','Yaotecatl.py',165),
  ('expression -> exp expressionaux exp','expression',3,'p_expression','Yaotecatl.py',166),
  ('expressionaux -> AND','expressionaux',1,'p_expressionaux','Yaotecatl.py',168),
  ('expressionaux -> DOUBEQUAL','expressionaux',1,'p_expressionaux','Yaotecatl.py',169),
  ('expressionaux -> NOT','expressionaux',1,'p_expressionaux','Yaotecatl.py',170),
  ('expressionaux -> OR','expressionaux',1,'p_expressionaux','Yaotecatl.py',171),
  ('expressionaux -> LESSTHANEQUAL','expressionaux',1,'p_expressionaux','Yaotecatl.py',172),
  ('expressionaux -> GREATTHANEQUAL','expressionaux',1,'p_expressionaux','Yaotecatl.py',173),
  ('expressionaux -> GREATTHAN','expressionaux',1,'p_expressionaux','Yaotecatl.py',174),
  ('expressionaux -> LESSTHAN','expressionaux',1,'p_expressionaux','Yaotecatl.py',175),
  ('loop -> WHILE LFTPAREN expression RGTPAREN block','loop',5,'p_loop','Yaotecatl.py',178),
  ('write -> PRINT LFTPAREN constant RGTPAREN SEMICOLON','write',5,'p_write','Yaotecatl.py',181),
  ('parameter -> type ID','parameter',2,'p_parameter','Yaotecatl.py',184),
  ('parameter -> type ID COMMA parameter','parameter',4,'p_parameter','Yaotecatl.py',185),
  ('parameter -> empty','parameter',1,'p_parameter','Yaotecatl.py',186),
  ('term -> factor termaux','term',2,'p_term','Yaotecatl.py',189),
  ('termaux -> MULTIPLICATION term termaux','termaux',3,'p_termaux','Yaotecatl.py',191),
  ('termaux -> DIVISION term termaux','termaux',3,'p_termaux','Yaotecatl.py',192),
  ('termaux -> empty','termaux',1,'p_termaux','Yaotecatl.py',193),
  ('statement -> assignment','statement',1,'p_statement','Yaotecatl.py',196),
  ('statement -> condition','statement',1,'p_statement','Yaotecatl.py',197),
  ('statement -> vars','statement',1,'p_statement','Yaotecatl.py',198),
  ('statement -> loop','statement',1,'p_statement','Yaotecatl.py',199),
  ('statement -> write','statement',1,'p_statement','Yaotecatl.py',200),
  ('statement -> read','statement',1,'p_statement','Yaotecatl.py',201),
  ('statement -> call','statement',1,'p_statement','Yaotecatl.py',202),
  ('type -> INT','type',1,'p_type','Yaotecatl.py',205),
  ('type -> FLOAT','type',1,'p_type','Yaotecatl.py',206),
  ('type -> CHAR','type',1,'p_type','Yaotecatl.py',207),
  ('type -> BOOL','type',1,'p_type','Yaotecatl.py',208),
  ('type -> STRING','type',1,'p_type','Yaotecatl.py',209),
  ('main -> PRIOMH block','main',2,'p_main','Yaotecatl.py',212),
  ('function -> FUNCTION functionaux ID LFTPAREN functionaux2 RGTPAREN blockreturn','function',7,'p_function','Yaotecatl.py',215),
  ('functionaux -> VOID','functionaux',1,'p_functionaux','Yaotecatl.py',217),
  ('functionaux -> type','functionaux',1,'p_functionaux','Yaotecatl.py',218),
  ('functionaux2 -> parameter','functionaux2',1,'p_functionaux2','Yaotecatl.py',220),
  ('functionaux2 -> empty','functionaux2',1,'p_functionaux2','Yaotecatl.py',221),
  ('vars -> type varsaux','vars',2,'p_vars','Yaotecatl.py',224),
  ('varsaux -> ID EQUAL expression SEMICOLON','varsaux',4,'p_varsaux','Yaotecatl.py',226),
  ('varsaux -> ID EQUAL call','varsaux',3,'p_varsaux','Yaotecatl.py',227),
  ('varsaux -> ID EQUAL expression COMMA varsaux','varsaux',5,'p_varsaux','Yaotecatl.py',228),
  ('varsaux -> ID LFTBRACSQR INT RGTBRACSQR EQUAL arrayvalues SEMICOLON','varsaux',7,'p_varsaux','Yaotecatl.py',229),
  ('varsaux -> ID LFTBRACSQR INT RGTBRACSQR EQUAL arrayvalues COMMA varsaux','varsaux',8,'p_varsaux','Yaotecatl.py',230),
  ('call -> ID LFTPAREN exp RGTPAREN SEMICOLON','call',5,'p_call','Yaotecatl.py',236),
  ('call -> ID LFTPAREN exp callaux RGTPAREN SEMICOLON','call',6,'p_call','Yaotecatl.py',237),
  ('callaux -> COMMA exp callaux','callaux',3,'p_callaux','Yaotecatl.py',239),
  ('callaux -> empty','callaux',1,'p_callaux','Yaotecatl.py',240),
  ('read -> READ LFTPAREN ID RGTPAREN SEMICOLON','read',5,'p_read','Yaotecatl.py',244),
  ('empty -> <empty>','empty',0,'p_empty','Yaotecatl.py',247),
]
