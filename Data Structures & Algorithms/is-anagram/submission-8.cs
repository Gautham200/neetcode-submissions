public class Solution {
    public bool IsAnagram(string s, string t) {

        if(s.Length != t.Length){
            return false;
        }
        Dictionary<char,int> sd = new Dictionary<char, int>();
        Dictionary<char, int> td = new Dictionary<char, int>();

        foreach(char i in s){
            if(sd.ContainsKey(i)){
                sd[i] = sd[i]+1;
            }else{
                sd[i] = 1;
            }
        }

        foreach(char i in t){
            if(td.ContainsKey(i)){
                td[i] = td[i]+1;
            }else{
                td[i] = 1;
            }
        }

        foreach(var i in td.Keys){
            if(!(sd.ContainsKey(i) && sd[i]==td[i])){
                return false;
            }
        }
        return true;

    }
}
