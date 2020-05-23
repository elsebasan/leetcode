class Kata {
    static def orderedCount(input) {
        // Implement me! :)
        [char] probando = input.slit()
        for (letter : probando)
            print(letter)
    }
}



static void main(String[] args) {
      
    Kata.orderedCount('abracadabra')
//    assert Kata.orderedCount('abracadabra') == [['a', 5], ['b', 2], ['r', 2], ['c', 1], ['d', 1]]
 //   assert Kata.orderedCount('Code Wars') == [['C', 1], ['o', 1], ['d', 1], ['e', 1], [' ', 1], ['W', 1], ['a', 1], ['r', 1], ['s', 1]]
    

}


