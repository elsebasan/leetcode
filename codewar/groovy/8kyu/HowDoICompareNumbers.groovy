
import org.junit.Test

class Kata {
  static whatIs(int x) {
    System.out.println(x)
    System.out.println(x.equals(1764))
    
    int y = 42*42
    
    System.out.println(y)
    System.out.println(y.equals(1746))

    if (x.equals(42)){
        return "everything"
    }
    else if (x.equals(1764)) {
        return  "everything squared"
    }
    else{ 
        return "nothing"
    }
  }
    
}
    

    static void main(String[] args) {
    Kata.whatIs(42 * 42) 
    /*
    assert Kata.whatIs(0) == "nothing"
    assert Kata.whatIs(123) == "nothing"
    assert Kata.whatIs(-1) == "nothing"
    assert Kata.whatIs(42) == "everything"
    assert Kata.whatIs(42 * 42) == "everything squared"
*/

    }





