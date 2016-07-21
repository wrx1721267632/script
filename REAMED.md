###一个简单的shell脚本
```
$ cat > nusers

who | wc -l

^D

$ chmod +x nusers

$ ./nusers
```
###位与第一行的#！

当一个文件中开头的两个字符是#！时，内核会扫描该行其余部分，看是否存在可用来执行程序的解释器的完整路径。内核会扫描是否具有一个选项要传递给解释器。内核会以被指定的选项来引用解释器，再搭配命令行的其他部分。

shell脚本通常一开始都是#！/bin/sh

```
$ cat ./nusers.sh 

#! /bin/bash

who | wc -l
```

###变量
Shell变量名称的开头是一个字母或下划线符号，后面可以接着任意长度的字母，数字或下划线符号。变量名称的字符长度并无限制。Shell变量可以用来保存字符串值，所能保存的字符数同样没有限制。

eg：

```
$ myvar=this_is_a_long

$ echo $myvar 

this_is_a_long

```

变量赋值的方法位：先写变量名称，紧接着=字符，最后是新值，中间完全没有任何空格。当你想取出shell变量的值时，需在变量名称前面加上$字符。当所赋予的值内含空格时，请加上引号：

eg：

```
$ first=isaac middle=bashevis last=sinder

$ fullname="isaac bashevis sinder"

$ oldname=$fullname 

$ echo $fullname 

isaac bashevis sinder

$ fullname="$first $middle $last"

$ echo $fullname 

isaac bashevis sinder
```

###简单的echo输出

echo 的任务就是产生输出，可以用来提示用户，或是用来产生数据供进一步处理。

eg：

```
$ echo asdfs dfasdfsad dfasfasdf

asdfs dfasdfsad dfasfasdf

```

###华丽的printf输出

printf命令模仿C程序库里的printf()库程序。

eg：

```
$ printf "adsfsdfsadf\n"

adsfsdfsadf

$ printf "adsfsdfsadf %s %s \n" aaa aaa

adsfsdfsadf aaa aaa 
```

###基本的I/O重定向

标准输入/输出可能是软件设计原则里最重要的概念了。这个概念就是：程序应该有数据的来源端，数据的目的段以及报告问题的地方，他们被称为标准输入，标准输出以及变准错误输出。
```
$ cat       未指定任何参数，读取标准输入，写入标准输出

now         由用户输入

now         由cat返回

for

for

^D
```

1.重定向与管道

（1）由<改变标准输入

program < file 将program的标准输入改为file

（2）由>改变标准输出

program > file 将program的标准输出改为file

‘>’ 重定向符在目的文件不存在时，会新建一个。然而，如果目的文件已存在，它就会被覆盖掉；原本的数据都会丢失。

（3）以 >>附加文件

program >> file 可将program的标准输出附加到file结尾处。如果文件不存在，它会新建一个文件。

（4）以 | 建立管道

program1 | program2  可将program1的标准输出修改为program2的标准输入。

管道可以把两个以上执行中的程序衔接在一起。第一个程序的标准输出可以变成第二个程序的标准输入。

2.特殊文件：/dev/null和/dev/tty

/dev/null文件是位桶。传送到此文件的数据都会被系统丢弃掉。也就是说，当程序将数据写到此文件时，会认为它已成功完成写入数据的操作，但实际上什么事都没做。

相对的，读取/dev/null则会立即返回文件结束符号。

/dev/tty。当程序打开该文件时，UNIX会自动将它重定向到一个终端再与程序结合。

eg：

```
$ cat tty.sh 

#!/bin/bash

printf "Enter new password: "

stty -echo							关闭自动打印输入字符的功能

read pass < /dev/tty

printf "\nEnter begin: "

read pass2 < /dev/tty

printf "\n"

stty echo							打开自动打印输入字符的功能

$ ./tty.sh 

Enter new password: 

Enter begin: 

```

3.基本命令查找

如果你要自己编写脚本，最好准备自己的bin目录来存放它们，并且让shell能够自动找到他们。这不难，只要建立自己的bin目录，并将它加入$PATH中的列表即可：

```
$ mkdir bin						建立个人bin目录

$ mv nusers bin					

$ PATH=$PATH:$HOME/bin    		将个人的bin目录附加到PATH，根据路径附加

$ nusers						nusers以命令的模式使用

5
```

要让修改永久生效，在.profile文件中把你的bin目录加入$PATH，而每次登陆时Shell都将读取.profile文件。

eg：

```
PATH=$PATH：$HOME/bin
```

###访问Shell脚本的参数

所谓的位置参数指的也就是Shell脚本的命令行参数。在Shell函数里，他们同时也可以是函数的参数。各参数都由整数来命名。基于历史原因，当他超过9，就应该用大括号把数字框起来：

```
 echo first arg is $1

 echo tenth arg is ${10}
```

参数的使用：

```
$ cat finduser.sh 

#!/bin/bash

who | grep $1

$ chmod +x finduser.sh

$ ./finduser.sh tty2

linux    tty2         2016-07-18 17:46 (:0)

$ mv finduser.sh $HOME/bin 						将这个文件存入自己的bin目录

$ finduser.sh 									无参数时的情况
用法: grep [选项]... PATTERN [FILE]...
试用‘grep --help’来获得更多信息。
```

###简单的执行跟踪

程序是人写的，难免会出错。但是我们可以通过打开执行跟踪的功能来显示每个被执行的命令。这会使得Shell显示每个被执行到的命令，并在前面加上‘+’：一个加号后面跟着一个空格。

eg：

```
$ sh -x nusers

+ who

+ wc -l

5

```

当然也可以在脚本里用set -x命令执行跟踪的功能打开，然后再用set +x命令关闭。

eg：

```
$ cat nusers.sh 

#!/bin/bash

set -x

who | wc -l

set +x

echo $1

$ nusers.sh www

+ who

+ wc -l

5

+ set +x

www
```

执行时set -x不会被跟踪，因为跟踪功能是在这条命令执行后才打开的。
set +x回被跟踪是因为是在命令执行后跟踪功能才关闭的。