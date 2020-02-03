package RandomMathQuiz;

/**
 * @description This class create Addition problems
 * @author danielshotonwa
 *
 */
public class AdditionProblem {
	private int x,y,answer;
	
	/**
	 * @description 
	 */
	public AdditionProblem() {
	 x = (int)(10 + 40*Math.random());
	 y = (int)(30 * Math.random());
	 answer = x + y;
	}
	
	/**
	 * @return String - Return a question
	 */
	public String getProblem() {
	  return "Compute the sum: " + x + " + " + y + ": ";
	}
	/**
	 * 
	 * @return Integer - Answer to question
	 */
	public int getAnswer() {
	  return answer;
	}
}
