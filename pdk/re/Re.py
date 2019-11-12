"""
Title: Re

Author: Bear Payne
Date: 2019/11/11 16:25
Description:
        符号 	解释 	示例 	说明
. 	匹配任意字符 	b.t 	可以匹配bat / but / b#t / b1t等
\w 	匹配字母/数字/下划线 	b\wt 	可以匹配bat / b1t / b_t等
但不能匹配b#t
\s 	匹配空白字符（包括\r、\n、\t等） 	love\syou 	可以匹配love you
\d 	匹配数字 	\d\d 	可以匹配01 / 23 / 99等
\b 	匹配单词的边界 	\bThe\b
^ 	匹配字符串的开始 	^The 	可以匹配The开头的字符串
$ 	匹配字符串的结束 	.exe$ 	可以匹配.exe结尾的字符串
\W 	匹配非字母/数字/下划线 	b\Wt 	可以匹配b#t / b@t等
但不能匹配but / b1t / b_t等
\S 	匹配非空白字符 	love\Syou 	可以匹配love#you等
但不能匹配love you
\D 	匹配非数字 	\d\D 	可以匹配9a / 3# / 0F等
\B 	匹配非单词边界 	\Bio\B
[] 	匹配来自字符集的任意单一字符 	[aeiou] 	可以匹配任一元音字母字符
[^] 	匹配不在字符集中的任意单一字符 	[^aeiou] 	可以匹配任一非元音字母字符
* 	匹配0次或多次 	\w*
+ 	匹配1次或多次 	\w+
? 	匹配0次或1次 	\w?
{N} 	匹配N次 	\w{3}
{M,} 	匹配至少M次 	\w{3,}
{M,N} 	匹配至少M次至多N次 	\w{3,6}
| 	分支 	foo|bar 	可以匹配foo或者bar
(?#) 	注释
(exp) 	匹配exp并捕获到自动命名的组中
(? <name>exp) 	匹配exp并捕获到名为name的组中
(?:exp) 	匹配exp但是不捕获匹配的文本
(?=exp) 	匹配exp前面的位置 	\b\w+(?=ing) 	可以匹配I'm dancing中的danc
(?<=exp) 	匹配exp后面的位置 	(?<=\bdanc)\w+\b 	可以匹配I love dancing and reading中的第一个ing
(?!exp) 	匹配后面不是exp的位置
(?<!exp) 	匹配前面不是exp的位置
*? 	重复任意次，但尽可能少重复 	a.*b
a.*?b 	将正则表达式应用于aabab，前者会匹配整个字符串aabab，后者会匹配aab和ab两个字符串
+? 	重复1次或多次，但尽可能少重复
?? 	重复0次或1次，但尽可能少重复
{M,N}? 	重复M到N次，但尽可能少重复
{M,}? 	重复M次以上，但尽可能少重复
"""
import re


def main():
    username = input('请输入用户名: ')
    qq = input('请输入QQ号: ')
    # match函数的第一个参数是正则表达式字符串或正则表达式对象
    # 第二个参数是要跟正则表达式做匹配的字符串对象
    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
    if not m1:
        print('请输入有效的用户名.')
    m2 = re.match(r'^[1-9]\d{4,11}$', qq)
    if not m2:
        print('请输入有效的QQ号.')
    if m1 and m2:
        print('你输入的信息是有效的!')


if __name__ == '__main__':
    main()