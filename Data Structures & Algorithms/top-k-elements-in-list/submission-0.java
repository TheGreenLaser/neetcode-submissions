class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();

        for(Integer n : nums){
            if(map.containsKey(n)){
                map.put(n, map.get(n) + 1);
            }
            else{
                map.put(n, 1);
            }
        }
        
        int remaining = k;
        int[] result = new int[k];
        int curIndex = 0;

        while(remaining > 0){
            remaining--;
            int biggest = -1;
            int biggestKey = 0;
            for(Integer i : map.keySet()){
                if(map.get(i) > biggest){
                    biggestKey = i;
                    biggest = map.get(i);
                }
            }

            result[curIndex] = biggestKey;
            curIndex++;
            map.remove(biggestKey);
        }

        return result;
    }
}
