'''
做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用**生成激活码**（或者优惠券），
使用 Python 如何生成 200 个激活码（或者优惠券）？
将 生成的 200 个激活码（或者优惠券）保存到 **MySQL** 关系型数据库中。 
将生成的 200 个激活码（或者优惠券）保存到 **Redis** 非关系型数据库中。 
'''

import random
import pymysql
import redis

#生成200个随机字符串,XXXX-XXXX-XXXX-XXXX
'''
a-z:97-122
A-Z:65-90
0-9:48-57
'''
class randomChar(object):
	"""docstring for randomChar"""
	def randomString(self):
		list = []
		for i in range(48,58):
			list.append(i)
		for i in range(65,91):
			list.append(i)
		for i in range(97,123):
			list.append(i)
		ranS = ''
		for j in range(4):
			for i in range(4):
				index = random.choice(list)
				ranS += chr(index)
			if j != 3:
				ranS += '-'
		return ranS



#连接MySql数据库
class MySqlOperation(object):
	#mysqlRedis
	def __init__(self):
		self.conn = pymysql.connect(host='localhost',
									user='root',
									password='11111111',
									db='reptile',
									port=3306,
									charset='utf8',
									cursorclass=pymysql.cursors.DictCursor)
		self.cur = self.conn.cursor()
	def op_sql(self, params):
		try:
			self.cur.execute(params)
			self.conn.commit()
			return True
		except pymysql.Error as e:
			print('MySQL Error %d:%s' % (e.args[0], e.args[1]))
		return False

	def insertCode(self, code):
		sql = "insert into mysqlRedis(code) values('%s')" % code
		if not self.op_sql(sql):
			print('insert error %s' % code)
		else:
			print('success')

	def selectCode(self):
		sql = "select code from mysqlRedis"
		try:
			self.cur.execute(sql)
			self.cur.scroll(0, mode='absolute') # 光标回到初始位置
			results = self.cur.fetchall() # 返回游标中所有结果
		except pymysql.Error as e:
			results = 'sql0001' # 数据库执行失败
			print("MySQL Error %d: %s" % (e.args[0], e.args[1]))
		finally:
			return results


#连接redis数据库
class RedisOperation(object):
	def __init__(self):
		pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
		self.r = redis.Redis(connection_pool=pool)
		



#向mysql中插入数据
for i in range(200):
	randC = randomChar()
	code = randC.randomString()
	operation = MySqlOperation()
	operation.insertCode(code)

#查询mysql数据并存储在redis中
operation = MySqlOperation()
ro = RedisOperation()
r = ro.r
r.delete('codes')
for code in operation.selectCode():
	r.sadd('codes', code['code'])
print(r.smembers('codes'))





