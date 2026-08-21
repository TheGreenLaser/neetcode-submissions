class Solution {
    public int[] productExceptSelf(int[] nums) {
        //prefix: 1,  2,  8, 48
        //suffix: 48, 48, 24, 6

        //  48,           24,                        12,                  8
        //suffix(1)  suffix(2) * prefix (0).  suffix(3) * prefix(1).  prefix(2)

        int[] prefix = Arrays.copyOf(nums, nums.length);
        int[] suffix = Arrays.copyOf(nums, nums.length);

        int[] result = new int[nums.length];

        for(int i = 1; i < nums.length; i++){
            prefix[i] *= prefix[i-1];
            suffix[nums.length - i - 1] *= suffix[nums.length - i];
        }

        for(int i = 1; i < result.length - 1; i++){
            result[i] = suffix[i + 1] * prefix[i - 1];
        }

        result[0] = suffix[1];
        result[nums.length - 1] = prefix[nums.length - 2];

        return result;
    }
}  
