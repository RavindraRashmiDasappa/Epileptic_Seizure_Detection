function CheckInputs() 
{
var isvalid = true
var X1 = document.form1.X95.value;
var X2 = document.form1.X101.value;
var X3 = document.form1.X106.value;
var X4 = document.form1.X111.value;
var X5 = document.form1.X116.value;
var X6 = document.form1.X121.value;
var X7 = document.form1.X127.value;
var X8 = document.form1.X144.value;
var X9 = document.form1.X153.value;
var X10 = document.form1.X156.value;
var X11 = document.form1.X160.value;
var X12 = document.form1.X161.value;
var X13 = document.form1.X169.value;
var X14 = document.form1.X171.value;
var X15 = document.form1.X177.value;

var decimal=  /^-?(0|[1-9]\d*)?(\.\d+)?(?<=\d)$/;
if(!X1.match(decimal))
{
isvalid = false
console.log("true")
}
if(!X2.match(decimal))
{
isvalid = false
console.log("true")
}
if(!X3.match(decimal))
{
isvalid = false
console.log("true")
}
if(!X4.match(decimal))
{
isvalid = false
console.log("true")
}
if(!X5.match(decimal))
{
isvalid = false
console.log("true")
}
if(!X6.match(decimal))
{
isvalid = false
console.log("true")
}
if(!X7.match(decimal))
{
isvalid = false
console.log("true")
}
if(!X8.match(decimal))
{
isvalid = false
console.log("true")
}
if(!X9.match(decimal))
{
isvalid = false
console.log("true")
}
if(!X10.match(decimal))
{
isvalid = false
console.log("true")
}
if(!X11.match(decimal))
{
isvalid = false
console.log("true")
}
if(!X12.match(decimal))
{
isvalid = false
console.log("true")
}
if(!X13.match(decimal))
{
isvalid = false
console.log("true")
}
if(!X14.match(decimal))
{
isvalid = false
console.log("true")
}
if(!X15.match(decimal))
{
isvalid = false
console.log("true")
}
if(!isvalid)
{
alert('Enter only Integers/Floats...!')

}
return isvalid
}
