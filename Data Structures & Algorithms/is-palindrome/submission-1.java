class Solution {
    public boolean isPalindrome(String s) {
        s = s.trim();
        s = s.replaceAll("\\s+","");
        int l = 0;
        int r = s.length() -1 ;
        char[] ch = s.toCharArray();
        while(l<r)
        {
            while(l<r && !Character.isLetterOrDigit(ch[l]))
            {
                l++;
            }
            while(l<r && !Character.isLetterOrDigit(ch[r]))
            {
                r--;
            }
            if((Character.toLowerCase(ch[r])) != Character.toLowerCase(ch[l]))
            {
                return false;
            }
            l++;
            r--;
        }

        return true;


    }
}
