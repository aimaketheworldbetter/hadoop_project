http://www.gutenberg.org/ebooks/4300?msg=welcome_stranger

echo "hadoop mapreduce mapreduce python" | python wordcount_mapper.py | sort -k1
#echo 在Linux中代表输出， | 代表将输出传给后面的文件作为输入
#sort -k1表示按照第一个字段区域进行排序

hadoop jar \
/usr/lib/hadoop-mapreduce/hadoop-streaming-2.6.0-cdh5.13.0.jar \
-files /home/cloudera/word_count/wordcount_mapper.py,\
/home/cloudera/word_count/wordcount_reducer.py \
-mapper "python wordcount_mapper.py" \
-reducer "python wordcount_reducer.py" \
-input /user/cloudera/wordcount/input.txt \ 
-output /user/cloudera/wordcount/output
#第一点
	hadoop jar  提交运行MapReduce程序
#第二点
	files参数，将用python编写的脚本文件上传到集群上，一遍集群中各个机器下载使用
	要求集群中各个节点上必须安装python而且版本一致
#第三点
	指定input，output，mapper和reduce各个参数值
#第四点
	结果输出到output，通过以下命令查看输出结果
	$hdfs dfs -text /user/cloudera/wordcount/output/part-00000