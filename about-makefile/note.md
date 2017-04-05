# 自动化makefile

根据网上摘录的代码，改为了一个自动化的makefile

```makefile
	DIR_SRC = ./
	DIR_OBJ = ./obj
	DIR_BIN = ./

	SRC = $(wildcard ${DIR_SRC}*.f90)  
	OBJ = $(patsubst %.f90,${DIR_OBJ}/%.o,$(notdir ${SRC}))

	TARGET = main

	BIN_TARGET = ${DIR_BIN}${TARGET}

	CC = gfortran

	CFLAGS = -Wall -O2

	${BIN_TARGET}: ${OBJ}
		$(CC) $(OBJ)  -o $@

	${DIR_OBJ}/%.o:${DIR_SRC}%.f90
		$(CC) $(CFLAGS) -c  $< -o $@

	.PHONY:clean

	clean:
		rm $(DIR_OBJ)/*.o
```

# 关于makefile

一些资料是来自于网络，主要学习 [跟我一起学习makefile](http://blog.csdn.net/haoel/article/details/2886)的系列文章，文中详细列出了*makefile*的用法，可以作为以后参考。


在这个示例代码中，有两个文件，*hello.f90*，和*fun.f90*，代码实现将目标文件放在*./boj*文件夹中，最后生成的可执行文件放在当前文件夹下。

该*makefile*用到的一些语法如下所示：

 - 函数*addprefix*

 	> $(addprefix &lt;prefix>,&lt;names...>) <br>
 	> 名称：加前缀函数——addprefix。<br>
 	> 功能：把前缀<prefix>加到<names>中的每个单词前面。  
 	> 返回：返回加过前缀的文件名序列。  
 	> 示例：$(addprefix src/,foo bar)返回值是“src/foo src/bar”。

  - 使用%进行部分字符的替换

    > 例如有：`objects = foo.o bar.o baz.o`，<br>
    > 那么，`$(objects:.o=.c)`和`$(patsubst %.o,%.c,$(objects))`是一样的。<br>
    > 在依赖关系中，可以简单写为`%.o: %.f90` <br>

  - 自动变量"$<"和"$@"

   例如：

```makefile
	objects = foo.o bar.o
	all: $(objects)
    $(objects): %.o: %.c
    	$(CC) -c $(CFLAGS) $< -o $@
```

   >上面的例子中，指明了我们的目标从$object中获取，“%.o”表明要所有以“.o”结尾的目标，也就是“foo.o bar.o”，也就是变量$object集合的模式，而依赖模式“%.c”则取模式“%.o”的“%”，也就是“foo bar”，并为其加下“.c”的后缀，于是，我们的依赖目标就是“foo.c bar.c”。而命令中的“$<”和“$@”则是自动化变量，“$<”表示所有的依赖目标集（也就是“foo.c bar.c”），“$@”表示目标集（也就是“foo.o bar.o”）。于是，上面的规则展开后等价于下面的规则：


```makefile
	    foo.o : foo.c
	            $(CC) -c $(CFLAGS) foo.c -o foo.o
	    bar.o : bar.c
	            $(CC) -c $(CFLAGS) bar.c -o bar.o
```

在写makefile过程中，灵活使用变量，这样可以方便更改，也使得makefile简洁


附一个网上摘录的多目录下编译的makefile代码

```makefile
	DIR_INC = ./include
	DIR_SRC = ./src
	DIR_OBJ = ./obj
	DIR_BIN = ./bin

	SRC = $(wildcard ${DIR_SRC}/*.c)  
	OBJ = $(patsubst %.c,${DIR_OBJ}/%.o,$(notdir ${SRC}))

	TARGET = main

	BIN_TARGET = ${DIR_BIN}/${TARGET}

	CC = gcc
	CFLAGS = -g -Wall -I${DIR_INC}

	${BIN_TARGET}:${OBJ}
	    $(CC) $(OBJ)  -o $@

	${DIR_OBJ}/%.o:${DIR_SRC}/%.c
	    $(CC) $(CFLAGS) -c  $< -o $@
	.PHONY:clean
	clean:
	    find ${DIR_OBJ} -name *.o -exec rm -rf {}
```
