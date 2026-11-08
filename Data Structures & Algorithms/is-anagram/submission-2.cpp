class Solution {
public:
    bool isAnagram(string s, string t) {
        // fast fail if strings are different lengths
        if (s.length() != t.length()) {
            return false;
        }
        
        // count occurrence of characters in both strings
        unordered_map<char, int> first;
        unordered_map<char, int> second;

        for (char c : s) {
            if (!first.contains(c)) {
                first[c] = 1;
            } else {
                first[c] += 1;
            }
        }

        for (char c : t) {
            if (!second.contains(c)) {
                second[c] = 1;
            } else {
                second[c] += 1;
            }
        }

        // fast fail if number of entries in maps are different
        if (first.size() != second.size()) {
            return false;
        }
       
        // loop through one of the maps and check num of occurrences in each
        int matching = 0;

        for ( auto entry : first ) {
            if (second.contains(entry.first) && second[entry.first] == entry.second) {
                matching++;
            }
        }

        if ( matching == first.size() ) {
            return true;
        } else {
            return false;
        }
    }
};
