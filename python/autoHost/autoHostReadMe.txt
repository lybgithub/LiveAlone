程序的输入是：包含所有http文件的文件夹路径
输出：sumFile.txt（文件夹folder or directory下面所有的文件写在一个新的txt中）
	  allHost.txt（没有去重的域名）
	  distinctHost.txt（去重之后的域名）
思路：1、获得文件夹中每一个file的名称，组合最开始的路径+'/'，组合成新的每一个文件的路径，然后依次读取，写入。
	  得到最终的处理文件sumFile.txt。
	  
	  2、对于最终的txt提取域名host，存入allHost.txt。
	  
	  3、去重。按行读取allHost.txt，存入set，然后对于下一个line，判断是都在之前的set中，如果不在的话，
			   完成两个操作：1、写入distinctHost.txt。2、add到之前的set中。
	
	
	遇到的问题：1、写入txt的时候，需要使用\n（回车），这样在按行读取之前的txt的时候才能正常读取。如果使用
				   的是'\r'（换行），这时候就不能正常的读取，因为python默认把回车当做换行的标志。
				2、关于使用open（fileName，‘w’）不能创建文件的问题，最后的解决方案是open(r'filename.txt','w')
				3、python中打开文件：w代表只写，r代表只读（也就是不往file中写内容），a代表追加，也就是每次都在上次的末尾加内容
				   解释一下上面提到的“上次”，python使用f = open（fileName)获得句柄，一次的概念就是这个句柄没有关闭，也就是这个流没有关闭
				   所以需要形成的一个好的条件是，对于一个文件的操作结束之后使用close（）关掉这个句柄。
				4、使用下面的方法切换当前目录，然后在切换后的目录中生成txt
				path = "F:\wiresharkPackage\mogujie"      #文件夹名称,只需要修改这一个地方
				os.chdir(path)