class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        Stack<Integer> stack = new Stack<>();
	    int n = temperatures.length;
        int[] res = new int[n];

        for(int i=0; i < temperatures.length; i++) {
            if (stack.isEmpty()) {
                stack.push(i);
            }
            else {
                while(!stack.isEmpty() && temperatures[i] > temperatures[stack.peek()]) {
                    int currDay = stack.pop();
                    res[currDay]  = i - currDay;
                    
                    }
	            
                stack.push(i);
            }
        }
        return res;
        }
}