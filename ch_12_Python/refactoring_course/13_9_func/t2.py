# Напишите функцию convert_temperature(temp: float, from_scale: str, to_scale: str) -> float,
# которая конвертирует температуру между шкалами Цельсия, Фаренгейта и Кельвина.

def convert_temperature(temp: float, from_scale: str, to_scale: str) -> float:
    if from_scale == "C" and to_scale == "F":
        return temp * (9 / 5) + 32
    if from_scale == "C" and to_scale == "K":
        return temp + 273.15
    if from_scale == "F" and to_scale == "C":
        return (temp - 32) / (9 / 5)
    if from_scale == "F" and to_scale == "K":
        return (temp + 459.67) * (5 / 9)
    if from_scale == "K" and to_scale == "C":
        return temp - 273.15
    if from_scale == "K" and to_scale == "F":
        return (temp - 273.15) * (9 / 5)

input_string  = input().split()
temp = int(input_string[0].replace(",",""))
from_scale = input_string[1].replace("\"", "").replace(",","")
to_scale = input_string[2].replace("\"", "")

print(convert_temperature(temp, from_scale, to_scale))