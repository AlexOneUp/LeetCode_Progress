class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        
        HashMap<String, List<String>> map = new HashMap<>();
        
        for(String subStr : strs) {
            char[] subStrArray = subStr.toCharArray();
            Arrays.sort(subStrArray);
            String key = new String(subStrArray);
            
            //Lines 12 => 15 work together
            if (!map.containsKey(key)) {
                map.put(key, new ArrayList<>());
            }
            map.get(key).add(subStr);
            //Lines 12 => 15 work together 
        }
        
        return new ArrayList<>(map.values());
    }
}

// use hashmap takes Str for key, List of Str arrays for val : returns array list for the maps values. Compares the SubStrings to a array of chars TO BE SORTED in list from substrings. New String takes sorted array represents the key for the map. See if map does not contain key, otherwise put key into the map with an arraylist as value. Get() the map with String array subStr as key, AND add() the subString as the new value