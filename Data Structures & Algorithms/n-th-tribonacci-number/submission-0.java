class Solution {
    public int tribonacci(int n) {
        if(n==1)
        {
            return n;
        }
        
        int n1 = 0,n2 = 1,n3 = 1;
        for(int i = 1; i<=n;i++)
        {
            int n4 = n1+n2+n3;
            n1=n2;
            n2=n3;
            n3=n4;
        }

        return n1;
    }
}