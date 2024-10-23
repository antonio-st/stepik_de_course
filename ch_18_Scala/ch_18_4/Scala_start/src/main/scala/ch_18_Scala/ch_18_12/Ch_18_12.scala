package ch_18_12

object Ch_18_12 extends App {

  def formatString(prefix: String)(body: String)(suffix: String): String = {
    s"$prefix$body$suffix"
  }

  val formatWithBrackets = formatString("[")(_: String)("]")
  println(formatWithBrackets("Hello")) // [Hello]

  val formatWithCurlyBraces = formatString("{")(_: String)("}")
  println(formatWithCurlyBraces("Hello")) // {Hello}

}
