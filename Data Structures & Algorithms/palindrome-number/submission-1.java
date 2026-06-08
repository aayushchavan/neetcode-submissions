class Solution {
    public boolean isPalindrome(int x) {
        int n = x;
        if(n<0){return false;}
        int revNum = 0 ;
        while(n>0)
        {
        int d = n%10;
        revNum = revNum *10 + d;
        n = n/10;
        } 

        if(revNum == x){return true;}
        else{return false;}
    }
    
}