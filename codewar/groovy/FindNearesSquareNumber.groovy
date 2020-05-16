import org.junit.Test
import java.lang.Math

class Kata {

  static def nearestSq(def n) {
    // your code here
    return Math.pow(Math.round(Math.sqrt(n)),2)

  }

    static void main(String[] args) {

        assert Kata.nearestSq(1) == 1
        assert Kata.nearestSq(2) == 1
        assert Kata.nearestSq(10) == 9
        assert Kata.nearestSq(111) == 121
        assert Kata.nearestSq(9999) == 10000

    }

}





