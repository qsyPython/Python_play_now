/**
 * 模块化公共类:
 */ 
function sayHello(name) {
  console.log(`Hello ${name}!`)// log内部参数传参,不用字符串，而是用``方式相当于format str
}

function sayGoodbye(name) {
  console.log(`Hello ${name}!`)
}

module.exports.sayHello = sayHello
module.exports.sayGoodbye = sayGoodbye