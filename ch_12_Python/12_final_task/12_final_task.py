import pandas as pd


def read_sales_data(file_path):
    "читает sales.csv построчно, каждую строку разбивает по , на словари, отдавая list словарей"

    # читаем файл построчно в переменную download
    with open(file_path, "r", encoding='utf-8') as f:
        download = f.readlines()
    result = []
    # иттеративно проходим по строкам файла(со второй строки), записываем словари по каждому аттрибуту в словарь,
    # предварительно разделя строку по ","
    dict1, dict2, dict3, dict4 = {}, {}, {}, {}
    for i in range(1, len(download)):
        dict1["product_name"] = download[i].split(",")[0]
        dict2["quantity"] = download[i].split(",")[1]
        dict3["price"] = download[i].split(",")[2]
        dict4["date"] = download[i].split(",")[3]
        result.append([dict1, dict2, dict3, dict4])
        dict1, dict2, dict3, dict4 = {}, {}, {}, {}
    return result


# def total_sales_per_product(sales_data):
#     """Принимает список продаж и возвращает словарь,
#     где ключ - название продукта, а значение - общая сумма продаж этого продукта"""
#     sum_apple, sum_pears, sum_plums, sum_cookies, sum_candies = 0, 0, 0, 0, 0
#     dict_sum = {}
#     for i in range(0, len(sales_data)):
#         p_name = sales_data[i][0].get("product_name")
#         p_price = sales_data[i][2].get("price")
#         p_quant = sales_data[i][1].get("quantity")
#         if p_name == "яблоки":
#             sum_apple += int(p_price) * int(p_quant)
#         elif p_name == "груши":
#             sum_pears += int(p_price) * int(p_quant)
#         elif p_name == "сливы":
#             sum_plums += int(p_price) * int(p_quant)
#         elif p_name == "печенье":
#             sum_cookies += int(p_price) * int(p_quant)
#         elif p_name == "конфеты Рот-Фронт":
#             sum_candies += int(p_price) * int(p_quant)
#
#     dict_sum["яблоки"] = sum_apple
#     dict_sum["груши"] = sum_pears
#     dict_sum["сливы"] = sum_plums
#     dict_sum["печенье"] = sum_cookies
#     dict_sum["конфеты Рот-Фронт"] = sum_candies
#     return dict_sum


def total_sales_per_product(sales_data):
    """Принимает список продаж и возвращает словарь, где ключ - дата,
    а значение общая сумма продаж за эту дату."""

    # преобразуем в список списков каждый день продаж, предварительно подсчитывая сумму продаж
    sum_to_date = []
    for i in range(0, len(sales_data)):
        p_name = sales_data[i][0].get("product_name").split("\n")[0]
        p_price = sales_data[i][2].get("price")
        p_quant = sales_data[i][1].get("quantity")
        sum_to_date.append([p_name, int(p_price) * int(p_quant)])

    # создаем df из полученного выше списка
    df = pd.DataFrame(sum_to_date, columns=["product_name", "sum_sales"])

    # группируем по дате
    sum_to_date_df = df.groupby('product_name', as_index=False) \
        .agg({'sum_sales': 'sum'}) \
        .sort_values("sum_sales")
    print(sum_to_date_df)

    # иттеративно проходя по каждой строке df записываем данные в словарь
    dict_sum_on_date = {}
    for i in range(len(sum_to_date_df)):
        dict_sum_on_date[sum_to_date_df.loc[i]["product_name"]] = int(sum_to_date_df.loc[i]["sum_sales"])

    return dict_sum_on_date


def sales_over_time(sales_data):
    """Принимает список продаж и возвращает словарь, где ключ - дата,
    а значение общая сумма продаж за эту дату."""

    # преобразуем в список списков каждый день продаж, предварительно подсчитывая сумму продаж
    sum_to_date = []
    for i in range(0, len(sales_data)):
        p_price = sales_data[i][2].get("price")
        p_quant = sales_data[i][1].get("quantity")
        date_p = sales_data[i][3].get("date").split("\n")[0]
        sum_to_date.append([date_p, int(p_price) * int(p_quant)])

    # создаем df из полученного выше списка
    df = pd.DataFrame(sum_to_date, columns=["date", "sum_sales"])

    # группируем по дате
    sum_to_date_df = df.groupby('date', as_index=False) \
        .agg({'sum_sales': 'sum'}) \
        .sort_values("date")

    # иттеративно проходя по каждой строке df записываем данные в словарь
    dict_sum_on_date = {}
    for i in range(len(sum_to_date_df)):
        dict_sum_on_date[sum_to_date_df.loc[i]["date"]] = int(sum_to_date_df.loc[i]["sum_sales"])

    return dict_sum_on_date


sales_data = read_sales_data("sales.csv")
print(sales_data)
print(total_sales_per_product(sales_data))
print(sales_over_time(sales_data))
