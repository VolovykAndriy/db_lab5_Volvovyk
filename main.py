import psycopg2
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


username = 'AAVOLOVYK'
password = '111'
database = 'lab_3'
host = 'localhost'
port = '5432'

query_1 = '''
SELECT * FROM PlatformGamesCountSlice;
'''
query_2 = '''
SELECT * FROM PublisherGlobalSalesSlice;
'''

query_3 = '''
SELECT * FROM YearlyTotalSalesSlice;
'''

create_view_1 = '''
CREATE OR REPLACE VIEW PlatformGamesCountSlice AS
SELECT
  Platform.Platform_Name,
  COUNT(Game.game_id) AS Games_Count
FROM
  Platform
JOIN
  Game ON Platform.platform_id = Game.platform_id
GROUP BY
  Platform.Platform_Name;

'''

create_view_2 = '''
CREATE OR REPLACE VIEW PublisherGlobalSalesSlice AS
SELECT
  p.Publisher_Name,
  SUM(gs.sales) AS Total_Global_Sales
FROM
  Publisher p
JOIN
  Game g ON p.publisher_id = g.publisher_id
JOIN
  global_sales gs ON g.gs_id = gs.gs_id
GROUP BY
  p.Publisher_Name
ORDER BY
  Total_Global_Sales DESC;

'''

create_view_3 = '''
CREATE OR REPLACE VIEW YearlyTotalSalesSlice AS
SELECT
  year_of_update,
  SUM(sales) AS total_sales
FROM global_sales
GROUP BY year_of_update
ORDER BY year_of_update;
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
    cur = conn.cursor()

    cur.execute(create_view_1)
    cur.execute(create_view_2)
    cur.execute(create_view_3)

    cur.execute(query_1)
    platform = []
    games_count = []

    for row in cur:
        platform.append(row[0])
        games_count.append(row[1])

    cur.execute(query_2)
    publisher_name = []
    total_global_sales = []

    for row in cur:
        publisher_name.append(row[0])
        total_global_sales.append(row[1])

    cur.execute(query_3)
    year = []
    total_sales_per_year = []

    for row in cur:
        year.append(row[0])
        total_sales_per_year.append(round(row[1], 2))
        print(row)


x_range = range(len(platform))

figure, (bar_ax, pie_ax, graph_ax) = plt.subplots(1, 3)
bar = bar_ax.bar(x_range, games_count, label='Total')
bar_ax.bar_label(bar, label_type='center')  # потрібен новий matplotlib
bar_ax.set_xticks(x_range)
bar_ax.set_xticklabels(platform)
bar_ax.set_xlabel('Платформа')
bar_ax.set_ylabel('Кількість ігр')
bar_ax.set_title('Кількість виданих ігор на кожну платформу')

pie_ax.pie(total_global_sales, labels=publisher_name, autopct='%1.1f%%')
pie_ax.set_title('Кількість продажів у світі за кожним видавництвом')

mark_color = 'blue'
graph_ax.plot(year, total_sales_per_year, color=mark_color, marker='o')

for qnt, price in zip(year, total_sales_per_year):
    graph_ax.annotate(price, xy=(qnt, price), color=mark_color, xytext=(7, 2), textcoords='offset points')

graph_ax.set_xlabel('Рік')
graph_ax.set_ylabel('Кількість')
graph_ax.set_title('Кількість проданих копій кожного року')

mng = plt.get_current_fig_manager()
mng.resize(1920, 1080)

plt.show()