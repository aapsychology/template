# import pymysql
#
# conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='ippool')
# cursor = conn.cursor()
# cursor.execute("insert proxy_ip(ip, port, speed, proxy_type) VALUES('{0}', '{1}', {2}, 'HTTP')".format(
#                     1, 2 ,3 ))
# conn.commit()
# cursor.close()
# conn.close()
#
# # 获取最新自增ID
# new_id = cursor.lastrowid