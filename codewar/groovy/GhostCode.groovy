import org.junit.Test
import java.lang.Math

class Kata {

  public static String helloName (String name) {
    // your code here
      // \u000d name="dumb";
    if(name == null || name.equals(""))
      return "Hello world!";
    else
      return "Hello my name is " + name;
  }


    static void main(String[] args) {

        String result = Kata.helloName("Javatlacati");
        println (result)
        assertEquals("Hello my name is Javatlacati is not "+ result,"Hello my name is Javatlacati",result);

    }

}





