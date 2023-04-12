class Solution {
public:
    string simplifyPath(string path) {
        stack<string> s, s1;
        vector<string> v;
        string t = "", res = "";
        path += "/";

        for (char i: path) {
            if (i == '/') {
                if (t != "" && t != ".") v.push_back(t);
                t = "";
            }
            else t += i;
        }

        for (string i: v) {
            if (i == "..") {
                if (!s.empty()) s.pop();
            }
            else s.push(i);
        }

        // reverse stack
        while (!s.empty()) {
            s1.push(s.top());
            s.pop();
        }

        while (!s1.empty()) {
            res += "/" + s1.top();
            s1.pop();
        }

        if (res == "") res = "/";

        return res;
    }
};
