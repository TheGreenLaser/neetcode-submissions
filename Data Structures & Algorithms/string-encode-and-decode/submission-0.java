class Solution {

    public String encode(List<String> strs) {
        String ret = "";

        for(String s : strs){
            int length = s.length();
            ret += Integer.toString(length) + "#";
            ret += s;
        }

        return ret;
    }

    public List<String> decode(String str) {
        List<String> temp = new ArrayList<String>();

        int i = 0;
        String num = "";
        
        while(i < str.length()){
            String c = str.substring(i, i+1);
            i++;
            if(c.equals("#")){
                int curLen = Integer.parseInt(num);
                String c2 = str.substring(i, i + curLen);
                temp.add(c2);
                i += curLen;
                num = "";
            }
            else{
                num += c;
            }   
        }

        return temp;
    }
}
