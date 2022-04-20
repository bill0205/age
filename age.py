driving = input('请问你有没有开过车：')
if driving != '有' and driving != '没有':
	print('只能输入有或者没有')
	raise SystemExit #触发错误，检查，不能运行就跳出，系统离开
# 如果想要不停的问他，直到他回答有或者没有怎么办 while回圈
# else是一定要写么？ 不一定，原则是要确保你的程序是完备的
# 不管怎么输入，都会有回答 
age = input('你的年龄：')
age = int(age)
#先处理开车部分 一块一块处理

if driving == '有':
	if age >= 18:
		print('你通过了测验')
	else:
		print('奇怪你怎么会开车')
elif driving == '没有':
	if age >= 18:
		print('你可以考驾照了，怎么没有考')
	else:
		print('很好，再过几年就可以考驾照了')
#else:
#	print('只能输入有或者没有')
#如果把有没有的判断 放到年龄前面
#就不需要这么一句话了		

# if与if的嵌套
# : 一定要切换到英文下去打标点符号
