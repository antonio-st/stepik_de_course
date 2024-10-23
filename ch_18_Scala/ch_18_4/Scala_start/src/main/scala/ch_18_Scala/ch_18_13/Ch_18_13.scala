package ch_18_13

object Ch_18_13 extends App {

  case class Person(name: String, age: Int)

  def describe(person: Person): String = person match {
    case Person("Alice", 25) => "This is Alice, 25 years old."
    case Person("Bob", age) => s"This is Bob, age $age."
    case Person(name, age) => s"This is $name, age $age."
  }

  val alice = Person("Alice", 25)
  val bob = Person("Bob", 30)
  val charlie = Person("Charlie", 35)

  println(describe(alice))    // This is Alice, 25 years old.
  println(describe(bob))      // This is Bob, age 30.
  println(describe(charlie))  // This is Charlie, age 35.


  trait Speaker {
    def speak(): String
  }

  trait Greeter {
    def greet(): String = "Hello"
  }

  class Personlity(name: String) extends Speaker with Greeter {
    def speak(): String = s"My name is $name"
  }

  val person = new Personlity("Alice")

  println(person.speak())
  println(person.greet())

}
