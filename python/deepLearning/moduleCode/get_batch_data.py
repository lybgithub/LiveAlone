## 获取的数据索引范围是[current_index,current_index+batch_size),一次操作完成之后更新current_index+=batch_size
## 输入的原始数据是array类型的
def get_batch_data(dataArray,batch_size,current_index):
    data_len = len(dataArray)
    if(current_index+batch_size>data_len):           # 当后面的数据不够一个batch_size的时候，把数据分两段取
        batch_data1 = dataArray[current_index:data_len] 
        current_index = (current_index+batch_size)%data_len
        batch_data2 = dataArray[0:current_index]
        batch_data = batch_data1+batch_data2 
    else:
        batch_data = dataArray[current_index:current_index+batch_size]
        current_index = current_index+batch_size
    return batch_data,current_index 