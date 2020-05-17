import org.junit.Test
import java.lang.Math

class Solution {

  static def areaOrPerimter(int l, int w) {
    // your code here
    return  ( l == w) ?  l*l :  2*(l+w)

  }

    static void main(String[] args) {
    assert Solution.areaOrPerimter(4, 4) == 16
    assert Solution.areaOrPerimter(6, 10) == 32
    assert Solution.areaOrPerimter(5, 4) == 18
    assert Solution.areaOrPerimter(72, 100) == 344

    }

}





