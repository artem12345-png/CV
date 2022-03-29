import MySQLdb
import graphviz
import math
import numpy as np

dot = graphviz.Digraph(format='svg')


def get_graph(pattern: str, time_from, time_to, max_thikness: int = 10, border=0.9) -> graphviz:
    """
        :param pattern: Слово, которое мы хотим найти в сообщениях
        :param time_from: от какого времени (указывать в формате год-месяц-день)
        :param time_to: по какое время мы хотим найти (указывать в формате год-месяц-день)
        :param max_thikness: параметр задает на сколько групп надо разбить уже отфильтрованные данные
        :param border: порог фильтрации данных, если вы укажите 0,9 то получите 10% с конца (то есть последние 10% наибольших данных)
        :return: возвращает итоговый граф, объект класса graphviz.Digraph()
        """

    with MySQLdb.connect() as db:
        cur = db.cursor()

        query = f"""
                    SELECT u1.NAME, u1.LAST_NAME, m.AUTHOR_ID, r.USER_ID,u.NAME, u.LAST_NAME, count(m.ID) as cnt 
                    FROM otelit.b_im_message m 
                    INNER JOIN otelit.b_im_relation r ON m.CHAT_ID = r.CHAT_ID
                    INNER JOIN otelit.b_user u ON u.ID = r.USER_ID
                    INNER JOIN otelit.b_user u1 ON u1.ID = m.AUTHOR_ID
                    WHERE m.AUTHOR_ID != r.USER_ID and 
                    m.MESSAGE like "%{pattern}%" and
                    r.user_id not in (1372, 32, 141, 1589) and 
                    m.AUTHOR_ID not in (1372, 32, 141, 1589) and
                    m.DATE_CREATE between "{time_from}" and "{time_to}" 
                    GROUP BY m.AUTHOR_ID, r.USER_ID;
                """
        dot = graphviz.Digraph()
        cur.execute(query)
        res = cur.fetchall()

        main_dict = {(item[2], item[3]): item[6] for item in res}
        users = {item[2]: str(item[0]) + " " + str(item[1]) for item in res}
        for item in res:
            if item[2] not in users:
                users[item[2]] = item[0] + " " + item[1]
            elif item[3] not in users:
                users[item[3]] = item[4] + " " + item[5]
        # print(main_dict)
        # print("-"*1000)
        # print(users)

        threshold = np.quantile([x for x in main_dict.values()], border)

        d_filtered = {k: v for k, v in main_dict.items() if v >= threshold}

        np.quantile([x for x in d_filtered.values()], [0, 0.2, 0.4, 0.6, 0.8])

        qt = np.quantile([x for x in d_filtered.values()], [i / max_thikness for i in range(max_thikness)])

        def thikness(v, qt):
            return np.sum(qt <= v)

        for k, v in d_filtered.items():
            dot.edge(str(users[k[0]]), str(users[k[1]]), penwidth=str(thikness(v, qt)))

        # print()
        # print(max(d_filtered.values()))
        # print(len(d_filtered))
        # print(threshold)
        dot.render(filename='main')
        return dot.source

