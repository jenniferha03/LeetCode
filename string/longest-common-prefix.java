class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) return "";

        String shortestWord = strs[0];

        for (int i = 1; i < strs.length; i++) {
            if (strs[i].length() < shortestWord.length()) {
                shortestWord = strs[i];
            }
        }

        // shortestWord = "flow"

        for (int i = 0; i < shortestWord.length(); i++) { // shortestWord.charAt(2) = "o"
            for (String s : strs) { // s = "flight"
                if (shortestWord.charAt(i) != s.charAt(i)) { // s.charAt(2) = "i"
                    return shortestWord.substring(0, i);
                }
            }
        }

        return shortestWord;
    }
}