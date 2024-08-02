/**
 * Tutorial: https://www.youtube.com/watch?v=9FAWP0DcpTo
 * 
 * Substring search is a method used to find a string of characters called a substring in another string known as text.
 * Brute force algorithm uses a straightforward method for finding the occurrence of a substring in a given large string or text.
 * This algorithm is mainly used in text processing and pattern matching.
 * This algorithm checks each substring within the large string for a match for the desired substring.
 * 
 * 
 * Brute Force Substring Search
 * 
 * This algorithm checks every possible position in the text to see if the substring matches.
 * Time Complexity: O(n * m)
 * - n: Length of the text
 * - m: Length of the pattern
 */


function bruteForceSearch(text, pattern){
    n = text.length; // Length of the text
    m = pattern.length; // Length of the pattern

    // Iterate through each position in the text where the pattern could start
    for (let i = 0; i <= n-m; i++) {
        let j = 0;

        // Check if the pattern matches the text starting from position i
        while (j < m && text[i+j] === pattern[j]) {
            j++;
        }

        // If we reached the end of the pattern, we found a match
        if(j===m){
            return i; // Return the starting index of the match
        }
    }
    return -1; // No match found
}


const text = "Brute Force Test";
const pattern = "Test";
const result = bruteForceSearch(text, pattern);
console.log(result); // Output: 6 (the index of the match)