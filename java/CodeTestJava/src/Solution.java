import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.stream.Collectors;

class Solution {
    public int solution(int[] priorities, int location) {
    	ArrayList<Integer> prioritiesArray = (ArrayList<Integer>) Arrays.stream(priorities).boxed().collect(Collectors.toList());        
    	
    	int answer = 0;
        return answer;
    }
    public ArrayList<Integer> _solution(ArrayList<Integer> priorities) {
    	int max = Collections.max(priorities);

    	return priorities;
    }
    public static void main(String[] args) {
		int[] priorities = {2, 1, 3, 2};
		int location = 2;
    	Solution s = new Solution();
		System.out.println(s.solution(priorities, location));
	}
}