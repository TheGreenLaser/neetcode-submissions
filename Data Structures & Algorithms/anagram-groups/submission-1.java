class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        //0. create hashmap(String, List<String>)
        //1. go through every string, make int[] frequency array, add to hashmap as String
        //1. big O (10^4 * 10^2)
        //2. convert hashmap to list<list<string>>

        HashMap<String, List<String>> map = new HashMap<String, List<String>>();
        List<List<String>> result = new ArrayList<List<String>>();

        for(String str : strs){
            char[] chars = str.toCharArray();
            Integer[] freq = new Integer[26];
            for(char c : chars){
                int position = c - 'a';
                if(freq[position] != null) freq[position] += 1;
                else freq[position] = 1;
            }

            String freqStr = Arrays.toString(freq);

            if(map.containsKey(freqStr)){
                List list = map.get(freqStr);
                list.add(str);
                map.put(freqStr, list);
            }
            else{
                List<String> list = new ArrayList<String>();
                list.add(str);
                map.put(freqStr, list);
            }
        }

        for(List<String> l : map.values()){
            result.add(l);
        }
        return result;
    }
}
