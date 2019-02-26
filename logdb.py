#!/usr/bin/env python2
import psycopg2


def set_db(query):
    """Return all posts from the 'database', most recent first."""
    try:
        db = psycopg2.connect("dbname=news")
        c = db.cursor()
        c.execute(query)
        val = c.fetchall()
        db.close()
        return val
    except psycopg2.Error as e:
        print("Unable to connect to the database")
        print(e.pgerror)
        print(e.diag.message_detail)
        sys.exit(1)


if __name__ == '__main__':
    q1 = """  select aubook.name, sum(num) as tot from
    (select articles.title as title, num from articles,
    (select articles.slug as slug,
    count(log.path) as num from log,articles
    where log.path  like '%' ||articles.slug || '%'
    and log.status not like '%404%'
    group by articles.slug order by num desc) as top_three
    where articles.slug = top_three.slug order by num desc) as rank
    join (select title, name
  from articles, authors
  where articles.author = authors.id) as           
  aubook on rank.title = aubook.title group by aubook.name 
  order by tot desc;"""
    q2 = """select articles.title, num from articles,
    (select articles.slug as slug, count(log.path) as num from log,articles
    where log.path  like '%' ||articles.slug || '%' and log.status not like '%404%'
    group by articles.slug order by num desc limit 3) as top_three
    where articles.slug = top_three.slug order by num desc;"""
    q3 = """select * from (select to_char(time,'MonthDD,YYYY') as date,ROUND((
  SUM(CASE WHEN status LIKE '%404%' THEN 1 ELSE 0 END) * 100.0 / COUNT(status)
  ),1) as percent_total
  from log GROUP BY date) as result where percent_total > 1;"""
    rows = set_db(q1)
    print "\nMost Popular Authors:\n"
    for row in rows:
        print("{0} - {1} views".format(row[0], int(row[1])))
    rows = set_db(q2)
    print "\nTop 3 Most Popular Books:\n"
    for row in rows:
        print("{0} - {1} views".format(row[0], int(row[1])))
    rows = set_db(q3)
    print "\nAbnormal Day(s):\n"
    for row in rows:
        print(' '.join(row[0].split()) + ' - {0}% errors'.format(row[1]))














