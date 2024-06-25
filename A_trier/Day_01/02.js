let str = "14gxqgqsqqbxfpxnbccjc33eightwo";
let firstDigit = str.match(/\d/)[0];
let lastDigit = str.match(/\d/g).pop();

console.log("Premier chiffre: " + firstDigit);
console.log("Dernier chiffre: " + lastDigit);
console.log(typeof firstDigit);
console.log("somme chiffre: ", `${firstDigit}${lastDigit}`);