class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, ArrayList<String>> res = new HashMap<String, ArrayList<String>>();
        for(int i=0; i < strs.length; i++){
            int[] check = new int[26];
            for(int j=0; j < strs[i].length(); j++) {
                char character = strs[i].charAt(j);
                check[character - 'a']++;
            }
            String key = Arrays.toString(check); //“eat” - 100001..1
            // System.out.println(key);
            if(res.containsKey(key)) 
                res.get(key).add(strs[i]);
            else {
                ArrayList<String> newArray = new ArrayList<String>();
                newArray.add(strs[i]);
                res.put(key, newArray);
            }
        }
        return new ArrayList<>(res.values());

    }
}