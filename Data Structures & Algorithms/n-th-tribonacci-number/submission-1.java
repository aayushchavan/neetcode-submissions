class Solution {
    public int tribonacci(int n) {
        if(n==0)
        {
            return 0;
        }
        else if(n==1)
        {
            return 1;
        }

        int n1=0;
        int n2=1;
        int n3=1;
        for(int i = 0;i<n-1;i++)
        {
            int n4=n1+n2+n3;
            n1=n2;
            n2=n3;
            n3=n4;
        }

        return n2;
    }
}