console.log( (![]+[])[+[]]  +(![]+[])[+!+[]]  +([![]]+[][[]])[+!+[]+[+[]]]   +(![]+[])[!+[]+!+[]] );
// 1
// (![]+[])[+[]] = ("false" +[])[0] = "false"[0] = 'f'

//2 
// (![]+[])[+!+[]] = ("false")[+!0] = ("false")[+true] = ("false")[1] = 'a'

// 3
// ([![]]+[][[]]) [+!+[]+[+[]]] = ([false] + undefined) [+!+[]+[0]] = 
// ("falseundefined") [1 +[] + [0]] = ("falseundefined") ['1' + '0'] = ("falseundefined") ['10'] = 'i'

// 4
// (![]+[])[!+[]+!+[]] = ("false")[true +!0] = ("false")[1 +true] = ("false")[1 + 1] = ("false")[2] = 'l' 
