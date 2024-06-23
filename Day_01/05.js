const str = 'xtwone3four';
let subStrings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];
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
let matches = str.match(regex)
console.log(matches);
let firstDigit = dico[matches[0]] ?? matches[0];
          console.log(firstDigit);
          let lastDigit = dico[matches.pop()] ?? matches.pop();
          console.log(lastDigit);