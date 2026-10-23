public class Solution {
    public bool hasDuplicate(int[] nums) {
        HashSet<int> l = new HashSet<int>();
        foreach(var i in nums){
            if(l.Contains(i)){
                return true;
            }
            l.Add(i);
        }
        return false;
    }
}