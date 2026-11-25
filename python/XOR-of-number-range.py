class Solution {
    public int findXOR(int l, int r) {
        // code here
        int start = (l/4)*4;
        int end = (r/4)*4;
        int xor = 0;
        for (int i=start;i<l;i++){
            xor^=i;
        }
        for (int i=end;i< r+1 ; i++){
            xor^=i;
        }
        return xor;
    }
}