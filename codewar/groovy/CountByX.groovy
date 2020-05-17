
import org.junit.Test

class Kata {
   static countBy(x, n) {
    // code here
    def aux = []
    for (i in 1..n){
        aux <<  (x * i)
    } 
    return (aux)

    
   }
    

    static void main(String[] args) {
    assert Kata.countBy(1, 5) == [1, 2, 3, 4, 5]
    assert Kata.countBy(2, 5) == [2, 4, 6, 8, 10]
    assert Kata.countBy(3, 5) == [3, 6, 9, 12, 15]
    assert Kata.countBy(50, 5) == [50, 100, 150, 200, 250]
    assert Kata.countBy(100, 5) == [100, 200, 300, 400, 500]

    }
}





