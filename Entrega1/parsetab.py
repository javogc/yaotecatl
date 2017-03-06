
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'LFTBRAC RGTBRAC LFTPAREN RGTPAREN LFTBRACSQR RGTBRACSQR AND DOUBEQUAL NOT OR SEMICOLON EQUAL LESSTHANEQUAL GREATTHANEQUAL GREATTHAN LESSTHAN PLUS MINUS MULTIPLICATION DIVISION ID COMMA FUNCTION INT FALSE STRING READ VOID FLOAT PRIOMH CHAR PRINT WHILE PROGRAM BOOL ELSEIF RETURN ELSE TRUE IFprogram : PROGRAM ID LFTBRAC auxprogram main RGTBRACauxprogram : vars auxprogram \n    | function auxprogram \n    | emptyarray : ID LFTBRACSQR exp RGTBRACSQRarrayvalues : LFTBRACSQR arrayvaluesaux RGTBRACSQR arrayvaluesaux : cteN arrayvaluesaux2\n    | cteS arrayvaluesaux2 arrayvaluesaux2 : COMMA arrayvaluesaux\n    | emptyassignment : assignmentaux EQUAL expression SEMICOLON \n    | assignmentaux EQUAL call assignmentaux : ID \n    | arrayblockreturn : LFTBRAC blockreturnaux RGTBRAC \n    | LFTBRAC blockreturnaux RETURN exp SEMICOLON RGTBRAC blockreturnaux : statement blockreturnaux \n    | empty block : LFTBRAC blockaux RGTBRACblockaux : statement blockaux \n    | empty condition : IF conditionaux \n    | IF conditionaux ELSE block conditionaux : LFTPAREN expression RGTPAREN block ELSEIF conditionaux \n    | LFTPAREN expression RGTPAREN block constant : ID \n    | array \n    | cteN\n    | cteS\n    | TRUE \n    | FALSE cteN : FLOAT \n    | INTcteS : STRINGexp : term expaux  expaux : PLUS exp expaux \n    | MINUS exp expaux \n    | empty factor : LFTPAREN expression RGTPAREN\n    | factoraux  factoraux : constant  \n    | MINUS constant\n    | PLUS constantexpression : exp \n    | exp expressionaux exp expressionaux : AND \n    | DOUBEQUAL \n    | NOT \n    | OR \n    | LESSTHANEQUAL \n    | GREATTHANEQUAL \n    | GREATTHAN \n    | LESSTHAN loop : WHILE LFTPAREN expression RGTPAREN block write : PRINT LFTPAREN constant RGTPAREN SEMICOLON parameter : type ID \n    | type ID COMMA parameter \n    | empty  term : factor termaux  termaux : MULTIPLICATION term termaux \n    | DIVISION term termaux \n    | empty  statement : assignment \n    | condition \n    | vars \n    | loop \n    | write \n    | read \n    | call  type : INT \n    | FLOAT \n    | CHAR \n    | BOOL \n    | STRING  main : PRIOMH block  function : FUNCTION functionaux ID LFTPAREN parameter RGTPAREN blockreturn  functionaux : VOID \n    | type  vars : type varsaux     varsaux : ID EQUAL expression SEMICOLON\n    | ID EQUAL call \n    | ID EQUAL expression COMMA varsaux \n    | ID LFTBRACSQR INT RGTBRACSQR EQUAL arrayvalues SEMICOLON\n    | ID LFTBRACSQR INT RGTBRACSQR EQUAL arrayvalues COMMA varsaux call : ID LFTPAREN exp RGTPAREN SEMICOLON \n    | ID LFTPAREN exp callaux RGTPAREN SEMICOLON  callaux : COMMA exp callaux\n    | empty read : READ LFTPAREN ID RGTPAREN SEMICOLON empty : '
    
_lr_action_items = {'RGTPAREN':([31,49,50,51,52,53,55,57,59,62,63,64,65,66,70,71,82,83,84,87,88,89,90,93,106,108,109,110,113,115,117,118,119,120,121,122,125,133,135,136,139,140,141,142,145,154,165,],[-90,-41,-29,-40,-27,-28,-30,-90,-34,-90,-31,-33,-32,-44,107,-58,-42,-26,-43,-59,-62,119,-35,-38,-56,128,129,130,132,137,-90,-90,-39,-90,-90,-45,-90,153,-88,-5,-61,-60,-36,-37,-57,-90,-87,]),'RETURN':([24,32,37,38,39,43,46,48,58,76,81,103,111,123,126,131,138,146,147,148,149,150,151,152,155,159,161,164,172,174,],[-79,-65,-67,-68,-69,-63,-64,-66,-81,-19,-22,-80,-12,-82,-90,-11,-23,-90,162,-18,-89,-54,-55,-85,-25,-83,-17,-86,-84,-24,]),'READ':([24,26,32,37,38,39,40,43,46,48,58,76,81,103,111,123,126,131,138,146,149,150,151,152,155,159,164,172,174,],[-79,33,-65,-67,-68,-69,33,-63,-64,-66,-81,-19,-22,-80,-12,-82,33,-11,-23,33,-89,-54,-55,-85,-25,-83,-86,-84,-24,]),'VOID':([5,],[18,]),'EQUAL':([23,36,44,45,105,136,],[29,-14,77,-13,124,-5,]),'CHAR':([4,5,6,10,24,26,31,32,37,38,39,40,43,46,48,58,76,81,103,111,123,125,126,127,131,138,146,149,150,151,152,155,159,163,164,172,174,177,],[7,7,7,7,-79,7,7,-65,-67,-68,-69,7,-63,-64,-66,-81,-19,-22,-80,-12,-82,7,7,-76,-11,-23,7,-89,-54,-55,-85,-25,-83,-15,-86,-84,-24,-16,]),'MULTIPLICATION':([49,50,51,52,53,55,57,59,61,63,64,65,82,83,84,87,88,117,118,119,136,139,140,],[-41,-29,-40,-27,-28,-30,86,-34,-26,-31,-33,-32,-42,-26,-43,-59,-62,86,86,-39,-5,-61,-60,]),'WHILE':([24,26,32,37,38,39,40,43,46,48,58,76,81,103,111,123,126,131,138,146,149,150,151,152,155,159,164,172,174,],[-79,34,-65,-67,-68,-69,34,-63,-64,-66,-81,-19,-22,-80,-12,-82,34,-11,-23,34,-89,-54,-55,-85,-25,-83,-86,-84,-24,]),'PROGRAM':([0,],[2,]),'PRINT':([24,26,32,37,38,39,40,43,46,48,58,76,81,103,111,123,126,131,138,146,149,150,151,152,155,159,164,172,174,],[-79,35,-65,-67,-68,-69,35,-63,-64,-66,-81,-19,-22,-80,-12,-82,35,-11,-23,35,-89,-54,-55,-85,-25,-83,-86,-84,-24,]),'RGTBRACSQR':([49,50,51,52,53,55,57,59,62,63,64,65,68,82,83,84,87,88,90,93,114,117,118,119,120,121,136,139,140,141,142,156,157,158,168,169,170,175,],[-41,-29,-40,-27,-28,-30,-90,-34,-90,-31,-33,-32,105,-42,-26,-43,-59,-62,-35,-38,136,-90,-90,-39,-90,-90,-5,-61,-60,-36,-37,-90,-90,171,-10,-8,-7,-9,]),'TRUE':([29,54,56,60,73,74,77,78,79,80,85,86,91,92,94,95,96,97,98,99,100,101,102,134,162,],[55,55,55,55,55,55,55,55,55,55,55,55,55,55,-46,55,-51,-52,-50,-53,-48,-47,-49,55,55,]),'MINUS':([29,49,50,51,52,53,55,57,59,60,61,62,63,64,65,73,77,78,79,80,82,83,84,85,86,87,88,90,91,92,93,94,95,96,97,98,99,100,101,102,117,118,119,120,121,134,136,139,140,141,142,162,],[54,-41,-29,-40,-27,-28,-30,-90,-34,54,-26,92,-31,-33,-32,54,54,54,54,54,-42,-26,-43,54,54,-59,-62,-35,54,54,-38,-46,54,-51,-52,-50,-53,-48,-47,-49,-90,-90,-39,92,92,54,-5,-61,-60,-36,-37,54,]),'SEMICOLON':([49,50,51,52,53,55,57,59,61,62,63,64,65,66,67,82,83,84,87,88,90,93,112,117,118,119,120,121,122,128,130,132,136,139,140,141,142,144,153,171,173,],[-41,-29,-40,-27,-28,-30,-90,-34,-26,-90,-31,-33,-32,-44,103,-42,-26,-43,-59,-62,-35,-38,131,-90,-90,-39,-90,-90,-45,149,151,152,-5,-61,-60,-36,-37,159,164,-6,176,]),'GREATTHAN':([49,50,51,52,53,55,57,59,61,62,63,64,65,66,82,83,84,87,88,90,93,117,118,119,120,121,136,139,140,141,142,],[-41,-29,-40,-27,-28,-30,-90,-34,-26,-90,-31,-33,-32,97,-42,-26,-43,-59,-62,-35,-38,-90,-90,-39,-90,-90,-5,-61,-60,-36,-37,]),'LESSTHANEQUAL':([49,50,51,52,53,55,57,59,61,62,63,64,65,66,82,83,84,87,88,90,93,117,118,119,120,121,136,139,140,141,142,],[-41,-29,-40,-27,-28,-30,-90,-34,-26,-90,-31,-33,-32,98,-42,-26,-43,-59,-62,-35,-38,-90,-90,-39,-90,-90,-5,-61,-60,-36,-37,]),'LFTBRACSQR':([23,45,61,83,124,],[30,79,79,79,143,]),'PLUS':([29,49,50,51,52,53,55,57,59,60,61,62,63,64,65,73,77,78,79,80,82,83,84,85,86,87,88,90,91,92,93,94,95,96,97,98,99,100,101,102,117,118,119,120,121,134,136,139,140,141,142,162,],[56,-41,-29,-40,-27,-28,-30,-90,-34,56,-26,91,-31,-33,-32,56,56,56,56,56,-42,-26,-43,56,56,-59,-62,-35,56,56,-38,-46,56,-51,-52,-50,-53,-48,-47,-49,-90,-90,-39,91,91,56,-5,-61,-60,-36,-37,56,]),'COMMA':([49,50,51,52,53,55,57,59,61,62,63,64,65,66,67,82,83,84,87,88,90,93,106,113,117,118,119,120,121,122,136,139,140,141,142,144,154,156,157,171,],[-41,-29,-40,-27,-28,-30,-90,-34,-26,-90,-31,-33,-32,-44,104,-42,-26,-43,-59,-62,-35,-38,125,134,-90,-90,-39,-90,-90,-45,-5,-61,-60,-36,-37,160,134,167,167,-6,]),'$end':([1,28,],[0,-1,]),'FUNCTION':([4,6,10,24,58,103,123,127,152,159,163,164,172,177,],[5,5,5,-79,-81,-80,-82,-76,-85,-83,-15,-86,-84,-16,]),'DIVISION':([49,50,51,52,53,55,57,59,61,63,64,65,82,83,84,87,88,117,118,119,136,139,140,],[-41,-29,-40,-27,-28,-30,85,-34,-26,-31,-33,-32,-42,-26,-43,-59,-62,85,85,-39,-5,-61,-60,]),'STRING':([4,5,6,10,24,26,29,31,32,37,38,39,40,43,46,48,54,56,58,60,73,74,76,77,78,79,80,81,85,86,91,92,94,95,96,97,98,99,100,101,102,103,111,123,125,126,127,131,134,138,143,146,149,150,151,152,155,159,162,163,164,167,172,174,177,],[11,11,11,11,-79,11,59,11,-65,-67,-68,-69,11,-63,-64,-66,59,59,-81,59,59,59,-19,59,59,59,59,-22,59,59,59,59,-46,59,-51,-52,-50,-53,-48,-47,-49,-80,-12,-82,11,11,-76,-11,59,-23,59,11,-89,-54,-55,-85,-25,-83,59,-15,-86,59,-84,-24,-16,]),'RGTBRAC':([21,24,26,27,32,37,38,39,40,41,42,43,46,48,58,75,76,81,103,111,123,126,131,138,146,147,148,149,150,151,152,155,159,161,164,172,174,176,],[28,-79,-90,-75,-65,-67,-68,-69,-90,-21,76,-63,-64,-66,-81,-20,-19,-22,-80,-12,-82,-90,-11,-23,-90,163,-18,-89,-54,-55,-85,-25,-83,-17,-86,-84,-24,177,]),'LFTPAREN':([25,29,33,34,35,45,47,60,61,73,77,78,79,80,85,86,91,92,94,95,96,97,98,99,100,101,102,134,162,166,],[31,60,72,73,74,78,80,60,78,60,60,60,60,60,60,60,60,60,-46,60,-51,-52,-50,-53,-48,-47,-49,60,60,80,]),'ELSE':([76,81,155,174,],[-19,116,-25,-24,]),'ELSEIF':([76,155,],[-19,166,]),'GREATTHANEQUAL':([49,50,51,52,53,55,57,59,61,62,63,64,65,66,82,83,84,87,88,90,93,117,118,119,120,121,136,139,140,141,142,],[-41,-29,-40,-27,-28,-30,-90,-34,-26,-90,-31,-33,-32,96,-42,-26,-43,-59,-62,-35,-38,-90,-90,-39,-90,-90,-5,-61,-60,-36,-37,]),'DOUBEQUAL':([49,50,51,52,53,55,57,59,61,62,63,64,65,66,82,83,84,87,88,90,93,117,118,119,120,121,136,139,140,141,142,],[-41,-29,-40,-27,-28,-30,-90,-34,-26,-90,-31,-33,-32,101,-42,-26,-43,-59,-62,-35,-38,-90,-90,-39,-90,-90,-5,-61,-60,-36,-37,]),'ID':([2,7,11,12,13,14,15,16,17,18,24,26,29,32,37,38,39,40,43,46,48,54,56,58,60,69,72,73,74,76,77,78,79,80,81,85,86,91,92,94,95,96,97,98,99,100,101,102,103,104,111,123,126,131,134,138,146,149,150,151,152,155,159,160,162,164,172,174,],[3,-72,-74,-70,23,-71,-73,25,-78,-77,-79,45,61,-65,-67,-68,-69,45,-63,-64,-66,83,83,-81,83,106,108,83,83,-19,61,83,83,83,-22,83,83,83,83,-46,83,-51,-52,-50,-53,-48,-47,-49,-80,23,-12,-82,45,-11,83,-23,45,-89,-54,-55,-85,-25,-83,23,83,-86,-84,-24,]),'IF':([24,26,32,37,38,39,40,43,46,48,58,76,81,103,111,123,126,131,138,146,149,150,151,152,155,159,164,172,174,],[-79,47,-65,-67,-68,-69,47,-63,-64,-66,-81,-19,-22,-80,-12,-82,47,-11,-23,47,-89,-54,-55,-85,-25,-83,-86,-84,-24,]),'AND':([49,50,51,52,53,55,57,59,61,62,63,64,65,66,82,83,84,87,88,90,93,117,118,119,120,121,136,139,140,141,142,],[-41,-29,-40,-27,-28,-30,-90,-34,-26,-90,-31,-33,-32,94,-42,-26,-43,-59,-62,-35,-38,-90,-90,-39,-90,-90,-5,-61,-60,-36,-37,]),'FALSE':([29,54,56,60,73,74,77,78,79,80,85,86,91,92,94,95,96,97,98,99,100,101,102,134,162,],[63,63,63,63,63,63,63,63,63,63,63,63,63,63,-46,63,-51,-52,-50,-53,-48,-47,-49,63,63,]),'LFTBRAC':([3,20,107,116,129,137,],[4,26,126,26,26,26,]),'INT':([4,5,6,10,24,26,29,30,31,32,37,38,39,40,43,46,48,54,56,58,60,73,74,76,77,78,79,80,81,85,86,91,92,94,95,96,97,98,99,100,101,102,103,111,123,125,126,127,131,134,138,143,146,149,150,151,152,155,159,162,163,164,167,172,174,177,],[12,12,12,12,-79,12,64,68,12,-65,-67,-68,-69,12,-63,-64,-66,64,64,-81,64,64,64,-19,64,64,64,64,-22,64,64,64,64,-46,64,-51,-52,-50,-53,-48,-47,-49,-80,-12,-82,12,12,-76,-11,64,-23,64,12,-89,-54,-55,-85,-25,-83,64,-15,-86,64,-84,-24,-16,]),'FLOAT':([4,5,6,10,24,26,29,31,32,37,38,39,40,43,46,48,54,56,58,60,73,74,76,77,78,79,80,81,85,86,91,92,94,95,96,97,98,99,100,101,102,103,111,123,125,126,127,131,134,138,143,146,149,150,151,152,155,159,162,163,164,167,172,174,177,],[14,14,14,14,-79,14,65,14,-65,-67,-68,-69,14,-63,-64,-66,65,65,-81,65,65,65,-19,65,65,65,65,-22,65,65,65,65,-46,65,-51,-52,-50,-53,-48,-47,-49,-80,-12,-82,14,14,-76,-11,65,-23,65,14,-89,-54,-55,-85,-25,-83,65,-15,-86,65,-84,-24,-16,]),'LESSTHAN':([49,50,51,52,53,55,57,59,61,62,63,64,65,66,82,83,84,87,88,90,93,117,118,119,120,121,136,139,140,141,142,],[-41,-29,-40,-27,-28,-30,-90,-34,-26,-90,-31,-33,-32,99,-42,-26,-43,-59,-62,-35,-38,-90,-90,-39,-90,-90,-5,-61,-60,-36,-37,]),'PRIOMH':([4,6,8,9,10,19,22,24,58,103,123,127,152,159,163,164,172,177,],[-90,-90,20,-4,-90,-2,-3,-79,-81,-80,-82,-76,-85,-83,-15,-86,-84,-16,]),'BOOL':([4,5,6,10,24,26,31,32,37,38,39,40,43,46,48,58,76,81,103,111,123,125,126,127,131,138,146,149,150,151,152,155,159,163,164,172,174,177,],[15,15,15,15,-79,15,15,-65,-67,-68,-69,15,-63,-64,-66,-81,-19,-22,-80,-12,-82,15,15,-76,-11,-23,15,-89,-54,-55,-85,-25,-83,-15,-86,-84,-24,-16,]),'NOT':([49,50,51,52,53,55,57,59,61,62,63,64,65,66,82,83,84,87,88,90,93,117,118,119,120,121,136,139,140,141,142,],[-41,-29,-40,-27,-28,-30,-90,-34,-26,-90,-31,-33,-32,100,-42,-26,-43,-59,-62,-35,-38,-90,-90,-39,-90,-90,-5,-61,-60,-36,-37,]),'OR':([49,50,51,52,53,55,57,59,61,62,63,64,65,66,82,83,84,87,88,90,93,117,118,119,120,121,136,139,140,141,142,],[-41,-29,-40,-27,-28,-30,-90,-34,-26,-90,-31,-33,-32,102,-42,-26,-43,-59,-62,-35,-38,-90,-90,-39,-90,-90,-5,-61,-60,-36,-37,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'cteS':([29,54,56,60,73,74,77,78,79,80,85,86,91,92,95,134,143,162,167,],[50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,156,50,156,]),'constant':([29,54,56,60,73,74,77,78,79,80,85,86,91,92,95,134,162,],[49,82,84,49,49,110,49,49,49,49,49,49,49,49,49,49,49,]),'vars':([4,6,10,26,40,126,146,],[6,6,6,32,32,32,32,]),'expaux':([62,120,121,],[90,141,142,]),'factoraux':([29,60,73,77,78,79,80,85,86,91,92,95,134,162,],[51,51,51,51,51,51,51,51,51,51,51,51,51,51,]),'array':([26,29,40,54,56,60,73,74,77,78,79,80,85,86,91,92,95,126,134,146,162,],[36,52,36,52,52,52,52,52,52,52,52,52,52,52,52,52,52,36,52,36,52,]),'termaux':([57,117,118,],[87,139,140,]),'cteN':([29,54,56,60,73,74,77,78,79,80,85,86,91,92,95,134,143,162,167,],[53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,157,53,157,]),'arrayvaluesaux':([143,167,],[158,175,]),'auxprogram':([4,6,10,],[8,19,22,]),'functionaux':([5,],[16,]),'write':([26,40,126,146,],[37,37,37,37,]),'program':([0,],[1,]),'call':([26,29,40,77,126,146,],[39,58,39,111,39,39,]),'statement':([26,40,126,146,],[40,40,146,146,]),'factor':([29,60,73,77,78,79,80,85,86,91,92,95,134,162,],[57,57,57,57,57,57,57,57,57,57,57,57,57,57,]),'arrayvalues':([124,],[144,]),'main':([8,],[21,]),'type':([4,5,6,10,26,31,40,125,126,146,],[13,17,13,13,13,69,13,69,13,13,]),'empty':([4,6,10,26,31,40,57,62,113,117,118,120,121,125,126,146,154,156,157,],[9,9,9,41,71,41,88,93,135,88,88,93,93,71,148,148,135,168,168,]),'blockaux':([26,40,],[42,75,]),'function':([4,6,10,],[10,10,10,]),'expressionaux':([66,],[95,]),'read':([26,40,126,146,],[38,38,38,38,]),'assignment':([26,40,126,146,],[43,43,43,43,]),'blockreturnaux':([126,146,],[147,161,]),'callaux':([113,154,],[133,165,]),'arrayvaluesaux2':([156,157,],[169,170,]),'assignmentaux':([26,40,126,146,],[44,44,44,44,]),'condition':([26,40,126,146,],[46,46,46,46,]),'term':([29,60,73,77,78,79,80,85,86,91,92,95,134,162,],[62,62,62,62,62,62,62,117,118,62,62,62,62,62,]),'parameter':([31,125,],[70,145,]),'blockreturn':([107,],[127,]),'block':([20,116,129,137,],[27,138,150,155,]),'exp':([29,60,73,77,78,79,80,91,92,95,134,162,],[66,66,66,66,113,114,66,120,121,122,154,173,]),'conditionaux':([47,166,],[81,174,]),'expression':([29,60,73,77,80,],[67,89,109,112,115,]),'loop':([26,40,126,146,],[48,48,48,48,]),'varsaux':([13,104,160,],[24,123,172,]),}

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
  ('arrayvaluesaux -> cteN arrayvaluesaux2','arrayvaluesaux',2,'p_arrayvaluesaux','Yaotecatl.py',98),
  ('arrayvaluesaux -> cteS arrayvaluesaux2','arrayvaluesaux',2,'p_arrayvaluesaux','Yaotecatl.py',99),
  ('arrayvaluesaux2 -> COMMA arrayvaluesaux','arrayvaluesaux2',2,'p_arrayvaluesaux2','Yaotecatl.py',101),
  ('arrayvaluesaux2 -> empty','arrayvaluesaux2',1,'p_arrayvaluesaux2','Yaotecatl.py',102),
  ('assignment -> assignmentaux EQUAL expression SEMICOLON','assignment',4,'p_assignment','Yaotecatl.py',105),
  ('assignment -> assignmentaux EQUAL call','assignment',3,'p_assignment','Yaotecatl.py',106),
  ('assignmentaux -> ID','assignmentaux',1,'p_assignmentaux','Yaotecatl.py',108),
  ('assignmentaux -> array','assignmentaux',1,'p_assignmentaux','Yaotecatl.py',109),
  ('blockreturn -> LFTBRAC blockreturnaux RGTBRAC','blockreturn',3,'p_blockreturn','Yaotecatl.py',112),
  ('blockreturn -> LFTBRAC blockreturnaux RETURN exp SEMICOLON RGTBRAC','blockreturn',6,'p_blockreturn','Yaotecatl.py',113),
  ('blockreturnaux -> statement blockreturnaux','blockreturnaux',2,'p_blockreturnaux','Yaotecatl.py',115),
  ('blockreturnaux -> empty','blockreturnaux',1,'p_blockreturnaux','Yaotecatl.py',116),
  ('block -> LFTBRAC blockaux RGTBRAC','block',3,'p_block','Yaotecatl.py',119),
  ('blockaux -> statement blockaux','blockaux',2,'p_blockaux','Yaotecatl.py',121),
  ('blockaux -> empty','blockaux',1,'p_blockaux','Yaotecatl.py',122),
  ('condition -> IF conditionaux','condition',2,'p_condition','Yaotecatl.py',125),
  ('condition -> IF conditionaux ELSE block','condition',4,'p_condition','Yaotecatl.py',126),
  ('conditionaux -> LFTPAREN expression RGTPAREN block ELSEIF conditionaux','conditionaux',6,'p_conditionaux','Yaotecatl.py',128),
  ('conditionaux -> LFTPAREN expression RGTPAREN block','conditionaux',4,'p_conditionaux','Yaotecatl.py',129),
  ('constant -> ID','constant',1,'p_constant','Yaotecatl.py',132),
  ('constant -> array','constant',1,'p_constant','Yaotecatl.py',133),
  ('constant -> cteN','constant',1,'p_constant','Yaotecatl.py',134),
  ('constant -> cteS','constant',1,'p_constant','Yaotecatl.py',135),
  ('constant -> TRUE','constant',1,'p_constant','Yaotecatl.py',136),
  ('constant -> FALSE','constant',1,'p_constant','Yaotecatl.py',137),
  ('cteN -> FLOAT','cteN',1,'p_cteN','Yaotecatl.py',140),
  ('cteN -> INT','cteN',1,'p_cteN','Yaotecatl.py',141),
  ('cteS -> STRING','cteS',1,'p_cteS','Yaotecatl.py',144),
  ('exp -> term expaux','exp',2,'p_exp','Yaotecatl.py',147),
  ('expaux -> PLUS exp expaux','expaux',3,'p_expaux','Yaotecatl.py',149),
  ('expaux -> MINUS exp expaux','expaux',3,'p_expaux','Yaotecatl.py',150),
  ('expaux -> empty','expaux',1,'p_expaux','Yaotecatl.py',151),
  ('factor -> LFTPAREN expression RGTPAREN','factor',3,'p_factor','Yaotecatl.py',154),
  ('factor -> factoraux','factor',1,'p_factor','Yaotecatl.py',155),
  ('factoraux -> constant','factoraux',1,'p_factoraux','Yaotecatl.py',157),
  ('factoraux -> MINUS constant','factoraux',2,'p_factoraux','Yaotecatl.py',158),
  ('factoraux -> PLUS constant','factoraux',2,'p_factoraux','Yaotecatl.py',159),
  ('expression -> exp','expression',1,'p_expression','Yaotecatl.py',162),
  ('expression -> exp expressionaux exp','expression',3,'p_expression','Yaotecatl.py',163),
  ('expressionaux -> AND','expressionaux',1,'p_expressionaux','Yaotecatl.py',165),
  ('expressionaux -> DOUBEQUAL','expressionaux',1,'p_expressionaux','Yaotecatl.py',166),
  ('expressionaux -> NOT','expressionaux',1,'p_expressionaux','Yaotecatl.py',167),
  ('expressionaux -> OR','expressionaux',1,'p_expressionaux','Yaotecatl.py',168),
  ('expressionaux -> LESSTHANEQUAL','expressionaux',1,'p_expressionaux','Yaotecatl.py',169),
  ('expressionaux -> GREATTHANEQUAL','expressionaux',1,'p_expressionaux','Yaotecatl.py',170),
  ('expressionaux -> GREATTHAN','expressionaux',1,'p_expressionaux','Yaotecatl.py',171),
  ('expressionaux -> LESSTHAN','expressionaux',1,'p_expressionaux','Yaotecatl.py',172),
  ('loop -> WHILE LFTPAREN expression RGTPAREN block','loop',5,'p_loop','Yaotecatl.py',175),
  ('write -> PRINT LFTPAREN constant RGTPAREN SEMICOLON','write',5,'p_write','Yaotecatl.py',178),
  ('parameter -> type ID','parameter',2,'p_parameter','Yaotecatl.py',181),
  ('parameter -> type ID COMMA parameter','parameter',4,'p_parameter','Yaotecatl.py',182),
  ('parameter -> empty','parameter',1,'p_parameter','Yaotecatl.py',183),
  ('term -> factor termaux','term',2,'p_term','Yaotecatl.py',186),
  ('termaux -> MULTIPLICATION term termaux','termaux',3,'p_termaux','Yaotecatl.py',188),
  ('termaux -> DIVISION term termaux','termaux',3,'p_termaux','Yaotecatl.py',189),
  ('termaux -> empty','termaux',1,'p_termaux','Yaotecatl.py',190),
  ('statement -> assignment','statement',1,'p_statement','Yaotecatl.py',193),
  ('statement -> condition','statement',1,'p_statement','Yaotecatl.py',194),
  ('statement -> vars','statement',1,'p_statement','Yaotecatl.py',195),
  ('statement -> loop','statement',1,'p_statement','Yaotecatl.py',196),
  ('statement -> write','statement',1,'p_statement','Yaotecatl.py',197),
  ('statement -> read','statement',1,'p_statement','Yaotecatl.py',198),
  ('statement -> call','statement',1,'p_statement','Yaotecatl.py',199),
  ('type -> INT','type',1,'p_type','Yaotecatl.py',202),
  ('type -> FLOAT','type',1,'p_type','Yaotecatl.py',203),
  ('type -> CHAR','type',1,'p_type','Yaotecatl.py',204),
  ('type -> BOOL','type',1,'p_type','Yaotecatl.py',205),
  ('type -> STRING','type',1,'p_type','Yaotecatl.py',206),
  ('main -> PRIOMH block','main',2,'p_main','Yaotecatl.py',209),
  ('function -> FUNCTION functionaux ID LFTPAREN parameter RGTPAREN blockreturn','function',7,'p_function','Yaotecatl.py',212),
  ('functionaux -> VOID','functionaux',1,'p_functionaux','Yaotecatl.py',214),
  ('functionaux -> type','functionaux',1,'p_functionaux','Yaotecatl.py',215),
  ('vars -> type varsaux','vars',2,'p_vars','Yaotecatl.py',219),
  ('varsaux -> ID EQUAL expression SEMICOLON','varsaux',4,'p_varsaux','Yaotecatl.py',221),
  ('varsaux -> ID EQUAL call','varsaux',3,'p_varsaux','Yaotecatl.py',222),
  ('varsaux -> ID EQUAL expression COMMA varsaux','varsaux',5,'p_varsaux','Yaotecatl.py',223),
  ('varsaux -> ID LFTBRACSQR INT RGTBRACSQR EQUAL arrayvalues SEMICOLON','varsaux',7,'p_varsaux','Yaotecatl.py',224),
  ('varsaux -> ID LFTBRACSQR INT RGTBRACSQR EQUAL arrayvalues COMMA varsaux','varsaux',8,'p_varsaux','Yaotecatl.py',225),
  ('call -> ID LFTPAREN exp RGTPAREN SEMICOLON','call',5,'p_call','Yaotecatl.py',231),
  ('call -> ID LFTPAREN exp callaux RGTPAREN SEMICOLON','call',6,'p_call','Yaotecatl.py',232),
  ('callaux -> COMMA exp callaux','callaux',3,'p_callaux','Yaotecatl.py',234),
  ('callaux -> empty','callaux',1,'p_callaux','Yaotecatl.py',235),
  ('read -> READ LFTPAREN ID RGTPAREN SEMICOLON','read',5,'p_read','Yaotecatl.py',239),
  ('empty -> <empty>','empty',0,'p_empty','Yaotecatl.py',242),
]
