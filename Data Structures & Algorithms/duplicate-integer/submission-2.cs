public class Solution {
    public bool hasDuplicate(int[] nums) {
        HashSet<int> viewed = new HashSet<int>();

        foreach (int i in nums){
            if (viewed.Contains(i)){
                return true;
            }
            viewed.Add(i);
        }
        return false;
    }
}