
package com.javacodegeeks.groovy.date

import org.junit.Test
import static java.util.Calendar.*

class Kata {
   static Boolean isToday(Date date) {
    // code here
      return (date.format('yyyyMMdd') == new Date().format('yyyyMMdd'))
   }
    

  static void main(String[] args) {
    Date yesterday = new Date() - 1
    Date tomorrow = new Date() + 1
    assert Kata.isToday(new Date()) == true
    assert Kata.isToday(tomorrow) == false
    assert Kata.isToday(yesterday) == false
  }
}





