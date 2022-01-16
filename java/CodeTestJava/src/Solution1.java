import java.util.ArrayList;

class Solution1 {
    public int[] solution(int[] progresses, int[] speeds) {
    	ArrayList<Integer> answer = new ArrayList<Integer>();
    	ArrayList<Integer> left = new ArrayList<Integer>();
    	int progress;
    	int speed;
    	Integer cnt = 0;
    	Integer _maxDue = null;
    	Integer maxDue = null;
    	
        for (int i = 0; i < progresses.length+1; i++) {
			if (i==progresses.length) {
				_maxDue = 100;
				}
			else {
				progress = progresses[i];
				speed = speeds[i];
				_maxDue = (100 - progress)/speed + ((((100 - progress)%speed) != 0)?1:0);
				left.add(_maxDue);				
			}
        	
			if (maxDue == null) {
				maxDue = _maxDue;
			}
			if (_maxDue > maxDue) {
				answer.add(cnt);
				cnt = 0;
				maxDue = _maxDue;
			}
			cnt++;
		}
        System.out.println(left);
        System.out.println(answer);
        int[] answerInt = answer.stream().mapToInt(i -> i).toArray();
        return answerInt;
    }
    public static void main(String[] args) {
        int[] progresses = {95, 90, 99, 99, 80, 99};
        int[] speeds =  {1, 1, 1, 1, 1, 1};
        Solution1 sol = new Solution1();
        System.out.println(sol.solution(progresses, speeds));
    }
}