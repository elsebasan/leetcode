
import org.junit.Test

class check {
   static chromosomeCheck(String sperm) {
    // code here
    "Congratulations! You're going to have a ${sperm.contains('Y') ? 'son' : 'daughter' }." 

    
   }
    

    static void main(String[] args) {
    assert check.chromosomeCheck("XY") == "Congratulations! You're going to have a son."
    assert check.chromosomeCheck("XX") == "Congratulations! You're going to have a daughter."

    }
}





