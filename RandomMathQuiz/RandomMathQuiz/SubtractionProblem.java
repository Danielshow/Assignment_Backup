package RandomMathQuiz;

public class SubtractionProblem {
	private int x,y,answer;
	
	/**
	 * @description 
	 */
	public SubtractionProblem() {
	 x = (int)(10 + 40*Math.random());
	 y = (int)(30 * Math.random());
	 answer = x - y;
	}
	
	/**
	 * @return String - Return a question
	 */
	public String getProblem() {
	  return "Compute the difference: " + x + " - " + y + ": ";
	}
	/**
	 * 
	 * @return Integer - Answer to question
	 */
	public int getAnswer() {
	  return answer;
	}
}
