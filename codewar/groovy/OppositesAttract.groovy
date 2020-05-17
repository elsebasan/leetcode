
import org.junit.Test

class Kata {
    static def lovefunc(flower1, flower2) {
        // Implement me! :)
        (flower1 + flower2) % 2 != 0
    }
    
}
    

    static void main(String[] args) {
        assert Kata.lovefunc(1,4) == true
        assert Kata.lovefunc(2,2) == false
        assert Kata.lovefunc(0,1) == true
        assert Kata.lovefunc(0,0) == false

    }





