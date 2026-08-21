class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        List<Integer>[] freqList = new List[nums.length+1];

        int[] result = new int[k];
        int cind = 0;

        for(Integer n : nums){
            if(map.containsKey(n)){
                map.put(n, map.get(n) + 1);
            }
            else{
                map.put(n, 1);
            }
        }

        //map stores number, frequency
        //freqList stores frequency, numbers

        for(Integer number: map.keySet()){
            int freq = map.get(number);
            if(freqList[freq] != null) freqList[freq].add(number);
            else{
                List<Integer> list = new ArrayList<Integer>();
                list.add(number);
                freqList[freq] = list;
            }
        }

        for (int i = freqList.length - 1; i > 0 && cind < k; i--) {
            if (freqList[i] == null) continue;

            for (int number : freqList[i]) {
                if (cind >= k) break;
                result[cind++] = number;
            }
        }

        return result;
    }
}
