public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int,int> d = new Dictionary<int,int>();
        int[] x = new int[2];
        for(int i = 0; i<nums.Length; i++){
            if(d.ContainsKey(target-nums[i])){
                x[0] = d[target-nums[i]];
                x[1] = i;
                return x;
            }
            d[nums[i]] = i;
        }
        return x;
    }
}
