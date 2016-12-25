# learn python


some note, while learn python

## about itertools

Python's 'itertools' is powerfull, can do some awesome 'for' loop.

### itertools.islice

itertools.islice(iterable, start, stop[, step])

返回的迭代器是返回了输入迭代器根据索引来选取的项

创建一个迭代器，生成项的方式类似于切片返回值： iterable[start : stop : step]，将跳过前start个项，迭代在stop所指定的位置停止，step指定用于跳过项的步幅。
与切片不同，负值不会用于任何start，stop和step，
如果省略了start，迭代将从0开始，如果省略了step，步幅将采用1.

返回序列seq的从start开始到stop结束的步长为step的元素的迭代器


```Python
#!/usr/bin/env python3

import itertools

with open('files') as f:
	ite=itertools.islice(f,1,None)	# skip the first line in 'files', the start of iter is '0'
	for line in ite:
		# deal with the line data
		print(line)

```


## csv file

the usage in *mtcsv2dat.py*.


## Python deal mt/amt data

mt/amt csv files use *mtcsv2dat.py*, translate csv file to data which can be read by mtsoft(old version).

*mtmtsoft2in.py*, translate mtsoft readable file to *in.dat* which can be use for inversion.
