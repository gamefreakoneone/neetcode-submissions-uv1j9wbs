class Solution {
public:

    string encode(vector<string>& strs) {
        if(strs.empty()){
            return {};
        }
        string answer = "";
        for(int i = 0; i < strs.size() ; i++){
            int length = strs[i].size();
            answer+= to_string(length)+"#"+strs[i];
        }
        return answer;
    }

    vector<string> decode(string s) {
        if(s.size()==0){
            return {};
        }
        vector<string> result;
        int i = 0 , j =0;
        while(i < s.size()){
            int j= i;
            while( s[j] != '#'){
                j++;
            }
            int length = stoi(s.substr( i , j- i));
            i = j+1;
            j = i + length;
            result.push_back(s.substr(i, length));
            i = j;
        }
        return result;
    }
};
