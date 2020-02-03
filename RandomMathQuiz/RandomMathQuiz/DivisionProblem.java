package RandomMathQuiz;

public class DivisionProblem {
	private int x,y,answer;
	
	/**
	 * @description 
	 */
	public DivisionProblem() {
	 x = (int)(10 + 40*Math.random());
	 y = (int)(30 * Math.random());
	 answer = (int)(x / y);
	}
	
	/**
	 * @return String - Return a question
	 */
	public String getProblem() {
	  return "Compute the division of: " + x + " - " + y + " in integer: ";
	}
	/**
	 * 
	 * @return Integer - Answer to question
	 */
	public int getAnswer() {
	  return answer;
	}
}
