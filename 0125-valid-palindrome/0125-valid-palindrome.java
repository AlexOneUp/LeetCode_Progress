class Solution {
    public boolean isPalindrome(String s) {
        String lowerCased = s.toLowerCase();
        String noSpecialChar = lowerCased.replaceAll("([^a-z0-9])", "");
        
        int stringLength = noSpecialChar.length();
        
        //Two Pointer Approach
        int j = stringLength - 1;
        int i = 0;
        while (i < j) {
            if(noSpecialChar.charAt(i) != noSpecialChar.charAt(j) ) {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
}

//Two Pointer Approach :
//___________________________________________________________________
// lowercase input, then regex lowercased input, then 2 ptr approach for each char in regex replaced string. If unmatching chars, then return false.
