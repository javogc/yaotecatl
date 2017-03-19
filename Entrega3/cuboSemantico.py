cube = {
    "int": {
      "int": { "+":"int", "-":"int",  "*":"int", "/":"int", ">":"bool",   ">=":"bool",  "<=":"bool", "<":"bool",  "=":"int", "==": "bool", "!=":"bool", "&&":"Error", "||":"Error",}, 
      "float": { "+":"float",   "-":"float",  "*":"float",  "/":"float",  ">":"bool",  ">=":"bool", "<=":"bool", "<":"bool",  "=":"int",  "==": "bool","!=":"bool", "&&":"Error",  "||":"Error",},  
      "string": {  "+":"Error",  "-":"Error",  "*":"Error",  "/":"Error", ">":"Error",  ">=":"Error", "<=":"Error","<":"Error", "=":"Error", "==": "Error","!=":"Error","&&":"Error",  "||":"Error",}, 
      "bool": {"+":"Error", "-":"Error",  "*":"Error",  "/":"Error",  ">":"Error",  ">=":"Error", "<=":"Error", "<":"Error", "=":"Error",  "==": "Error", "!=":"Error", "&&":"Error",  "||":"Error", },},
    
    "float":{
      "int": { "+":"float",   "-":"float",   "*":"float",   "/":"float",   ">":"bool",   ">=":"bool",  "<=":"bool",  "<":"bool",   "=":"float",  "==": "bool",   "!=":"bool","&&":"Error",  "||":"Error",   }, 
      "float": { "+":"float",  "-":"float",  "*":"float",  "/":"float",  ">":"bool",  ">=":"bool", "<=":"bool", "<":"bool", "=":"float",   "==": "bool","!=":"bool",   "&&":"Error",   "||":"Error", },  
      "string": { "+":"Error",  "-":"Error",  "*":"Error",  "/":"Error",  ">":"Error",  ">=":"Error", "<=":"Error", "<":"Error",  "=":"Error", "==": "Error",  "!=":"Error", "&&":"Error",   "||":"Error",   }, 
      "bool": {   "+":"Error",   "-":"Error",   "*":"Error",   "/":"Error",   ">":"Error",   ">=":"Error",  "<=":"Error",  "<":"Error",   "=":"Error", "==": "Error",  "!=":"Error", "&&":"Error",  "||":"Error", },},

    "string":{
      "int": {"+":"Error",   "-":"Error",   "*":"Error", "/":"Error",  ">":"Error",  ">=":"Error", "<=":"Error", "<":"Error",  "=":"Error",  "==": "Error", "!=":"Error", "&&":"Error",  "||":"Error", }, 
      "float": { "+":"Error",  "-":"Error", "*":"Error",   "/":"Error",   ">":"Error",   ">=":"Error",  "<=":"Error",  "<":"Error",   "=":"Error",   "==": "Error","!=":"Error", "&&":"Error", "||":"Error",},  
      "string": { "+":"string",   "-":"Error",   "*":"Error",   "/":"Error",   ">":"Error",   ">=":"Error",  "<=":"Error",  "<":"Error",   "=":"string", "==": "bool","!=":"bool", "&&":"Error",  "||":"Error", }, 
      "bool": { "+":"Error",  "-":"Error",  "*":"Error",  "/":"Error",  ">":"Error",  ">=":"Error", "<=":"Error", "<":"Error",  "=":"Error",  "==": "Error", "!=":"Error", "&&":"Error",  "||":"Error",},},
      
    "bool":{ 
      "int": {  "+":"Error",   "-":"Error",   "*":"Error",   "/":"Error",  ">":"Error",  ">=":"Error", "<=":"Error", "<":"Error",  "=":"Error", "==": "Error",  "!=":"Error", "&&":"Error",  "||":"Error", }, 
      "float": { "+":"Error", "-":"Error", "*":"Error",  "/":"Error",  ">":"Error",  ">=":"Error", "<=":"Error", "<":"Error",  "=":"Error",  "==": "Error", "!=":"Error",  "&&":"Error",  "||":"Error",  }, 
      "string": { "+":"Error",  "-":"Error",  "*":"Error",  "/":"Error",  ">":"Error",  ">=":"Error", "<=":"Error", "<":"Error",  "=":"Error",  "==":"Error","!=":"Error", "&&":"Error", "||":"Error",}, 
      "bool": {"+":"Error", "-":"Error", "*":"Error", "/":"Error", ">":"Error", ">=":"Error", "<=":"Error","<":"Error", "=":"bool", "==":"bool","!=":"bool","&&":"bool", "||":"bool",},},
      
    }

def checkSemanticCube(op1, op2, operator):
    return cube[op1][op2][operator]




