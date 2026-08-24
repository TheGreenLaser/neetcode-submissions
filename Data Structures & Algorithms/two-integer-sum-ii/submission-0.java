class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int pointer1 = 0;
        int pointer2 = numbers.length -1;

        while(pointer1 < pointer2){
            if(numbers[pointer1] + numbers[pointer2] == target){
                break;
            }
            if(numbers[pointer1] + numbers[pointer2] > target){
                pointer2--;
            }
            if(numbers[pointer1] + numbers[pointer2] < target){
                pointer1++;
            }
        }

        return new int[]{pointer1 + 1, pointer2 + 1};
    }
}
