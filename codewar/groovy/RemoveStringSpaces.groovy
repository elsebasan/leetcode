
import org.junit.Test

class Kata {
  static String noSpace(String x) {
      return (x.findAll{ it != " "}).join('')

  }
}
    
    

static void main(String[] args) {

    assert "8j8mBliB8gimjB8B8jlB" == Kata.noSpace("8 j 8   mBliB8g  imjB8B8  jl  B")
    assert "88Bifk8hB8BB8BBBB888chl8BhBfd" == Kata.noSpace("8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd")
    assert "8aaaaaddddr" == Kata.noSpace("8aaaaa dddd r     ")
    assert "jfBmgklf8hg88lbe8" == Kata.noSpace("jfBm  gk lf8hg  88lbe8 ")
    assert "8jaam" == Kata.noSpace("8j aam")


}





