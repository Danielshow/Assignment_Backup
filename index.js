function one(result=null, def_value=1){
  if (!result) {
    return def_value;
  }
  return solve(result, def_value)
}

function solve(result, value){
  var num = result[0]
  var operator = result[1]
  var sec_num = value

  switch(operator){
    case 'plus':
      return num + sec_num
    case 'subtract':
      return num - sec_num
    case 'multiply':
      return num * sec_num
    case 'divide':
      return num/sec_num
    default:
      return null;
  }
}
function plus(num){
  return [num, 'plus']
}


console.log(one(plus(one())))


