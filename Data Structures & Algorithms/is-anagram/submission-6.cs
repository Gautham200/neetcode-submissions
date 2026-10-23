public class Solution {
    public bool IsAnagram(string s, string t) {
        Dictionary<char,int> dic1 = new Dictionary<char,int>();
        Dictionary<char,int> dic2 = new Dictionary<char,int>();
        if(s.Length != t.Length){
            return false;
        }
        for(int i = 0; i<s.Length; i++){
            if(dic1.ContainsKey(s[i])){
                dic1[s[i]]++;
            }else{
                dic1[s[i]] = 1;
            }
            if(dic2.ContainsKey(t[i])){
                dic2[t[i]]++;
            }else{
                dic2[t[i]] = 1;
            }
        }
        foreach(var i in dic1.Keys){
            if(!dic2.ContainsKey(i) || dic1[i]!=dic2[i]){
                return false;
            }
        }
        foreach(var i in dic2.Keys){
            if(!dic1.ContainsKey(i) || dic1[i]!=dic2[i]){
                return false;
            }
        }
        
        return true;
    }
}
