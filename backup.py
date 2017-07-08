import os
import json
import pprint
import requests
#留言
#http://v2.dcard.tw/_api/posts/文章id/comments?limit=100
#留言
#http://v2.dcard.tw/_api/posts/文章id/comments?after=200&limit=100
def comment(*args):
	comment = args[1]
	url = 'http://v2.dcard.tw/_api/posts/%s/comments?limit=100' % (args[0])
def read(*args):
	read = 'http://v2.dcard.tw/_api/posts/%s?read=true' % (args[0])
	r = requests.get(read)
	olist = json.loads(r.text)
	title = olist['title']
	content = olist['content']
	likecount = olist['likeCount']
	update = olist['updatedAt']
	dirname = ''
	for x in title:
		dirname = dirname + '\\'+ x
	os.system('mkdir %s' % (dirname))

	if olist['gender'] == 'F':
		gender = '女森'
	else:
		gender = '男森'

	if olist['anonymousDepartment'] == True:
		department = '匿名'
	else:
		department = olist['department']
	with open('%s/content.txt' % (title),'w') as f:
		f.write('日期：%s\n標題：%s\n科系：%s\n性別：%s\n內文：%s' % (update,title,department,gender,content))
	try:
		for x in olist['media']:
			r = requests.get(x['url'])
			fname = x['url'].split('/')[-1]
			print(fname)
			with open('%s/%s' % (title,fname),'wb') as f:
				f.write(r.content)
	except:
		pass

url = 'http://v2.dcard.tw/_api/forums/cnu/posts?limit=100&popular=false'
r = requests.get(url)
dlist = json.loads(r.text)

read('文章id')
