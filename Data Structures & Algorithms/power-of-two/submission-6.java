class Solution {
    public boolean isPowerOfTwo(int n) {
        if(n<=0)
        {
            return false;
        }
        int x = n;
        while(x%2==0)
        {
                x=x/2;
        }
        if(x==1)
        {
            return true;
        }
        else{
            return false;
        }

    }
}