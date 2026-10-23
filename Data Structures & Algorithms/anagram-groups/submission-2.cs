public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        Dictionary<string,List<string>> dic = new Dictionary<string,List<string>>();
        int ind = 0;
        for(int i = 0; i<strs.Length; i++){
            int[] alphs = new int[26];
            foreach(var x in strs[i]){
                ind = char.ToUpper(x) - 'A';
                alphs[ind]++;
            }
            var key = string.Join('#',alphs);
            if(dic.ContainsKey(key)){
                dic[key].Add(strs[i]);
            }else{
                dic[key] = new List<string>();
                dic[key].Add(strs[i]);
            }

        }
        List<List<string>> res = new List<List<string>>();
        foreach(var i in dic.Keys){
            res.Add(dic[i]);
        }
        return res;
    }
}
