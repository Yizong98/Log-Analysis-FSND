#! /usr/bin/env python2
import psycopg2


def set_db(query):
    """Return all posts from the 'database', most recent first."""
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute(query)
    val = c.fetchall()
    db.close()
    return val


if __name__ == '__main__':
    q1 = """ select aubook.name, sum(num) as tot from
    (select articles.title, num from articles,
    (select articles.slug as slug,
    count(log.path) as num from log,articles
    where log.path  like '%' ||articles.slug || '%'
    group by articles.slug order by num desc) as top_three
    where articles.slug = top_three.slug order by num desc) as rank,
    (select title, name
  from articles, authors
  where articles.author = authors.id)
  as aubook group by aubook.name order by tot;"""
    q2 = """select articles.title, num from articles,
    (select articles.slug as slug, count(log.path) as num from log,articles
    where log.path  like '%' ||articles.slug || '%'
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
