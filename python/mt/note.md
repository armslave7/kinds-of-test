## Python脚本，切割剖面（north2south.py）
输入为东西向的剖面数据，命名为`point.txt`，其中`point`为数字，表示剖面位置，批量处理，首先使用`ls *.txt > files`，获取当前文件夹的`txt`文件，脚本中`point`变量对应要取得的点的位置，程序输出为`n2spoint.txt`数据文件，`n2spoint.bln`，bln文件（添加`base map`比较好），`n2spointpost.dat`，post文件，输出获取的点的位置


## Python脚本，扩展MT单点反演结果（expand-mt.py）

将单点MT反演结果扩展成多个点，便于surfer成图
输入为OUT.TXT，单点反演结果，输出为ex-out.dat
扩展为10个测点，step=0.025

批量处理，首先使用`ls *.txt > files`，获取当前文件夹的txt文件，然后执行*python*脚本，获得`*.dat`扩展之后的数据

2017/2/16 2:07:58

## Python脚本，mtsoft数据导出成反演所需数据in（mtsoft2in.py）

输入为mtsoft.dat，输出为in.dat和fre.dat，频率为计算出来的，可能存在很小的误差（不影响计算），但in和fre中保持一致

## Python脚本，csv格式导出成mtsoft所需格式（csv2mtsoft.py）

自动调整相位到0-90°，批量处理，首先使用`ls *.csv > csvfiles`，执行脚本之后得到`mtsoft.dat`

## Python脚本，in格式导出成mtsoft所需格式（in2mtsoft.py）

输入`in.dat`，输出`mtsoft.dat`
