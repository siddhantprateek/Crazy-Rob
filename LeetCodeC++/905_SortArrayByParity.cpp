class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& A) 
    { 
        int size = sizeof(A)/sizeof(A[0]);
        vector<int> even_arr, odd_arr;

        for(int i = 0; i < size; i++)
        {
            if (A[i] % 2 == 0)
            {
                even_arr.push_back(A[i]);
            }
            else
            {
                odd_arr.push_back(A[i]);
            }
        }
        return(transform(even_arr.begin(),even_arr.end(),odd_arr.begin(),odd_arr.begin(),plus<int>()));
    }
};