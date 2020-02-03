import java.util.Arrays;

/**
 * @description Benchmarking array.sort and selection sort
 * - Using 1000 - Selection sort: 4ms Array Sort: 1ms
 * - Using 10000 - Selection sort: 63ms Array Sort: 3ms
 * - Using 100000 - Selection sort: 5680ms Array Sort: 28ms
 * - Using 1000000 - Array sort: 112ms
 * @author danielshotonwa
 *
 */
public class SortingBenchmark {
	public static void main(String[] args) {
		int arraySize = 1000000;
		int[] firstArray = new int[arraySize];
		int[] secondArray = new int[arraySize];
		
		for (int i = 0; i < arraySize; i++) {
			int num = (int)(Integer.MAX_VALUE * Math.random());
			firstArray[i] = num;
			secondArray[i] = num;
		}
		long startTimefirstArray = System.currentTimeMillis();
		selectionSort(firstArray);
		long runTimeFirstArray = System.currentTimeMillis() - startTimefirstArray;
		
		long startTimeSecondArray = System.currentTimeMillis();
		Arrays.sort(secondArray);
		long runTimeSecondArray = System.currentTimeMillis() - startTimeSecondArray;
		
		System.out.println("Run time using selection sort: " + runTimeFirstArray);
		System.out.println("Run time using Array sort: " + runTimeSecondArray);
	}
	/**
	 * @description Sort an array using selection sort
	 * @param A - An unsorted array
	 * @return A - sorted using selection sort
	 */
	static void selectionSort(int[] A) {
		for (int lastPlace = A.length-1; lastPlace > 0; lastPlace--) {
			int maxLoc = 0;
			for (int j = 1; j <= lastPlace; j++) { 
				if (A[j] > A[maxLoc]) {
					maxLoc = j;
				} 
			}
		   int temp = A[maxLoc];
		   A[maxLoc] = A[lastPlace];
		   A[lastPlace] = temp;
		}
	}
}
