class Solution {
    public int lengthOfLongestSubstring(String s) {
        // ArrayList<String> longestSubstring = new ArrayList<String>(); 
        
        int longestSubstring = 0;
        
        HashSet<Character> doesCharExist = new HashSet<>(); 
        int left = 0;
        int right = 0;
        
        while( right != s.length() ) {
            if( doesCharExist.contains(s.charAt(right)) ) 
            {
                doesCharExist.remove(s.charAt(left));
                left++;          
            } else {
                doesCharExist.add(s.charAt(right));
                right++;              
            }
            longestSubstring = Math.max(longestSubstring, right - left );    

        }
        
        // longestSubstring = Math.max(longestSubstring, currentSubstring);
        
        return longestSubstring;
    }
}
