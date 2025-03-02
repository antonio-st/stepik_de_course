from pyspark.sql import SparkSession
import time

# Создание сессии Spark
spark = SparkSession.builder \
    .appName("PySpark Example") \
    .getOrCreate()

# Задействуем мощь Spark
data = [("Alice", 29), ("Bob", 34), ("Cathy", 28), ("David", 23)]
df = spark.createDataFrame(data, ["Name", "Age"])
print("Исходные данные:")
df.show()


df_filtered = df.filter(df["Age"] > 30)

print("Фильтрованные данные (возраст > 30):")
df_filtered.show()

print("Оставляем Spark UI доступным для просмотра в течение 3 мин.")
time.sleep(180)

spark.stop()
