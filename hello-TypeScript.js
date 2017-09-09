console.log("Hello World");
// : String - type annotation. Tells TS its a sting type
function hello(string) {
    console.log("Hello " + string);
}
// Works caus its type string
hello("John");
// Won't work cause expected type is String
//hello(1); 
