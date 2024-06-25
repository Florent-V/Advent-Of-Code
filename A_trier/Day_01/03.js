let str = "14gxqgqsqqbxfpxnbccjc33eight";
let subStrings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
const dico = {
  one: 1,
  two: 2,
  three: 3,
  four: 4,
  five: 5,
  six: 6,
  seven:7,
  eight: 8,
  nine: 9
}
let regex = new RegExp(subStrings.join("|"), "g");

let matches = str.match(regex);
console.log(dico[matches[0]]);
console.log(dico[matches.pop()]);