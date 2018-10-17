#! /usr/bin/env python

import psycopg2

DB = "news"
QUERY_ARTICLES = """select title,COUNT(*) AS views 
from articles 
JOIN log 
ON log.path LIKE concat('/article/%', articles.slug) 
GROUP BY articles.title 
ORDER BY views DESC 
LIMIT 3;"""

QUERY_AUTHOR = """select authors.name,COUNT(*) AS views 
from authors 
JOIN articles 
ON authors.id = articles.author 
JOIN log 
ON log.path like concat('/article/%', articles.slug)
group by authors.name 
order by views DESC
LIMIT 3;"""

QUERY_DAYS_ERROR = """SELECT total.day,
ROUND(((errors.error_requests*1.0) / total.requests), 3) AS percent 
FROM (SELECT date_trunc('day', time) "day", count(*) AS error_requests
FROM log          
WHERE status LIKE '404%'
GROUP BY day) AS errors
JOIN (SELECT date_trunc('day', time) "day", count(*) AS requests
FROM log
GROUP BY day) AS total
ON total.day = errors.day
WHERE (ROUND(((errors.error_requests*1.0) / total.requests), 3) > 0.01)
ORDER BY percent DESC;"""

def get_query_result(query):
    database = psycopg2.connect(database=DB)
    cursor = database.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    database.close()
    return results

def print_query_results(results):
    for item in results:
        print(str(item[0]) + ' ------ ' + str(item[1]))

if __name__ == '__main__':
    print("\nThe 3 most popular articles of all time are:\n")
    print_query_results(get_query_result(QUERY_ARTICLES))
    print("\nThe 3 most popular article authors of all time are:\n")
    print_query_results(get_query_result(QUERY_AUTHOR))
    print("\nDays with more than 1% of request that lead to an error:\n")
    print_query_results(get_query_result(QUERY_DAYS_ERROR))
