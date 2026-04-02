class Solution {
public:
    bool isValid(string s) {
        if(s.length()==0){
            return true;
        }
        queue<char> values;
        stack<char> open;
        for(int i = 0; i < s.size(); i++){
            values.push(s[i]);
        }

        while(!values.empty()){
            char curr = values.front();
            values.pop();
            if(curr=='(' || curr == '[' || curr == '{'){
                open.push(curr);
            }else if(open.empty()){
                    return false;
                }
            else{
                char curr_top = open.top();
                if(curr_top=='(' && curr==')'){
                    open.pop();
                } else if(curr_top=='[' && curr==']'){
                    open.pop();
                }else if(curr_top=='{' && curr=='}'){
                    open.pop();
                }else                
                {
                    return false;
                }
            }
        }
        if(open.empty()){
            return true;
        }
        return false;
    }
};
