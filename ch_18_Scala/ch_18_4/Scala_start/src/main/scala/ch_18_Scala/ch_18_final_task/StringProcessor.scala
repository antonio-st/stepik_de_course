package ch_18_final_task

  object StringProcessor {
    def processStrings(strings: List[String]): List[String] = {
      // заменим цикл и объявление переменных на filter для иттерации по списку и выявлении слов с кол-вом символом более 3
      // результатом работы filter является новый список с отфильтрованными значениями
      val funcRes: List[String] = strings.filter { x =>
        x.length > 3
      }
      // map применит функцию toUpperCase() к каждому элементу коллекции, результат  - новая коллекция
      // в функциональном стиле в функции выводится последнее выражение, return не используется
      funcRes.map(x => x.toUpperCase())
    }

    def main(args: Array[String]): Unit = {
      val strings = List("apple", "cat", "banana", "dog", "elephant")
      val processedStrings = processStrings(strings)
      println(s"Processed strings: $processedStrings")
    }
  }



