package RandomMathQuiz;


public class MathQuiz {
  public static void main(String[] args) {
	  TextIO.put("Hi, What is your name? ");
	  String name = TextIO.getln();
	  
	  TextIO.putln("Hello, " + name);
	  
	  TextIO.putln("This is a Math quiz, A question will be displayed, type in the correct answer. Cant you get to 100points");
	  
	  int score = 0;
	  
	  while (score != 100) {
		  int rand = (int)(Math.random() * 10);
		  if (rand < 5) {
			  AdditionProblem question = new AdditionProblem();
			  TextIO.put(question.getProblem());
			  for (int i = 0; i < 2; i++) {
				  int result = TextIO.getInt();
				  if (result == question.getAnswer() && i == 0) {
					  score += 10;
					  break;
				  } else if (result == question.getAnswer()) {
					  score += 5;
				  } else {
					  TextIO.putln("Enter the result again: ");
				  }
			  }
		  } else if(rand > 5 && rand < 7) {
			  SubtractionProblem question = new SubtractionProblem();
			  TextIO.put(question.getProblem());
			  int result = TextIO.getInt();
			  for (int i = 0; i < 2; i++) {
				  if (result == question.getAnswer() && i == 0) {
					  score += 10;
					  break;
				  } else if (result == question.getAnswer()) {
					  score += 5;
				  }
			  }
		  } else {
			  DivisionProblem question = new DivisionProblem();
			  TextIO.put(question.getProblem());
			  int result = TextIO.getInt();
			  for (int i = 0; i < 2; i++) {
				  if (result == question.getAnswer() && i == 0) {
					  score += 10;
					  break;
				  } else if (result == question.getAnswer()) {
					  score += 5;
				  }
			  }
			  
		  }
	  }
  }
}
