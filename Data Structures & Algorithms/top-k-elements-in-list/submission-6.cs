public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {
        Dictionary<int,int> dic = new Dictionary<int,int>();

        foreach(var num in nums){
            if(!dic.ContainsKey(num)){
                dic[num] = 1;
            }else{
                dic[num] = dic[num] + 1;
            }
        }

        int[] list = dic.OrderByDescending(x=>x.Value).Select(x=>x.Key).Take(k).ToArray();
        return list;
    }
}
