function detectWord(s) {
  let result = ""; // empty string to store lowercase letters
  for (let i = 0; i < s.length; i++) { // go through each character
    let char = s[i]; // current character
    if (char === char.toLowerCase() && char !== char.toUpperCase()) {
      result += char; // add lowercase letter to result
    }
  }
  return result; // return the hidden word
}

// Example usage
console.log(detectWord("UcUNFYGSFYFYGtNUH")); // Output: "ct"
