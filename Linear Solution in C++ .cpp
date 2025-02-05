#include <iostream>

using namespace std;

int main(int argc, char *argv[]) {

    int ExpectedLine;
    cin>> ExpectedLine;
    if (ExpectedLine == 1){
    	cout << 1 ;
    	return 0;
    }
    else if (ExpectedLine == 2){
    	cout << 1 << " " << 1;
    	return 0;
    }
    else{
	    
	    int lenArr = 0;
	    int counter = 0;
	    
		while (counter <= ExpectedLine){
			lenArr += counter;
			counter++;
		}
		//cout<<lenArr;
		
		int arr[lenArr-1] ;
		
		for (int i = 0; i <= 3; i++) {
	    	arr[i] = 1;
	    	
	    }

		counter = 3;
		int LoopNumber = 3;

		while (LoopNumber <= ExpectedLine){
			arr[counter] = 1;
			int loop = 0;
			while (loop < LoopNumber - 2){
				
				arr[counter] = arr[counter - 2] + arr[counter - 3];
				loop ++;
				counter ++;
			}
			arr[counter] = 1;
			LoopNumber++;
		}
	    for (int i = 0; i <= lenArr; i++) {
	        cout << arr[i] << " ";
	    }
	    
	}
    return 0;
}
