class Solution {
    public List<List<Integer>> threeSum(int[] nums){

        Arrays.sort(nums);

        List<List<Integer>> result = new ArrayList<List<Integer>>();

        for(int i = 0; i < nums.length; i++){
            if(i > 0 && nums[i] == nums[i-1]){
                continue;
            }

            int p1 = i+1;
            int p2 = nums.length - 1;

            int target = nums[i] * -1;

            while(p1 < p2){
                if(nums[p1] + nums[p2] == target){
                    List<Integer> list = new ArrayList<Integer>();
                    list.add(nums[p1]);
                    list.add(nums[p2]);
                    list.add(nums[i]);
                    result.add(list);
                    p1++;
                    p2--;
                    while(p2 > p1 && nums[p2] == nums[p2 + 1]){
                        p2--;
                    }
                    while(p1 < p2 && nums[p1] == nums[p1 - 1]){
                        p1++;
                    }
                }
                if(nums[p1] +nums[p2] > target){
                    p2--;
                    while(p2 > p1 && nums[p2] == nums[p2 + 1]){
                        p2--;
                    }
                }
                if(nums[p1] +nums[p2] < target){
                    p1++;
                    while(p1 < p2 && nums[p1] == nums[p1 - 1]){
                        p1++;
                    }
                }
            }
        }


        return result;
    }
}
