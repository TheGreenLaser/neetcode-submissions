class Solution {
    public int longestConsecutive(int[] nums) {
        if(nums.length == 0) return 0;
        int[] uniqueNums = Arrays.stream(nums)
                                    .distinct()
                                    .toArray();

        Arrays.sort(uniqueNums);

        for(Integer i : uniqueNums){
            System.out.println(i);
        }
        
        int largest = 0;
        int current = 0;

        for(int i = 1; i < uniqueNums.length; i++){
            if(uniqueNums[i] == uniqueNums[i-1] + 1){
                current++;
            }
            else{
                largest = Math.max(largest, current + 1);
                current = 0;
            }
        }

        return Math.max(largest, current + 1);
    }
}
