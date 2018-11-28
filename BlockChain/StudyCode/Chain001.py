#加密算法模块
import hashlib
#时间模块
import datetime

class www_block_coin(object):

    def __init__(self,index,timestamp,data,next_hash):
        #索引
        self.index = index
        #时间戳
        self.timestamp = timestamp
        #交易数据
        self.data = data
        #下一区块的hash
        self.next_hash = next_hash
        #自身hash
        self.self_hash = self.hash_www_block()

    #计算自身hash
    def hash_www_block(self):
        #将区块的整体信息合并，作为加密的数据，注意到将其中任意一项数据改变后都会导致后面整条链的改变
        block_info = '%s%s%s%s'%(self.index,self.timestamp,self.data,self.next_hash)
        SHA = hashlib.sha256()
        SHA.update(block_info.encode('utf-8'))
        #返回加密后得到的自身hash
        return SHA.hexdigest()

#创建第一个区块，即创世区块
def create_first_www_block():
    #索引为0，时间戳为创建时的时间戳，交易数据定为'hello world'，下一区块的hash为0
    return www_block_coin(0,datetime.datetime.now(),100000,'0')

#创建普通区块，根据上一个区块的数据进行改变
def create_many_www_coin(last_block):
    #索引为上一个区块的索引+1，很好理解
    this_index = last_block.index+1
    #时间戳为当前时间戳
    this_datastamp = datetime.datetime.now()
    #数据暂且定为hello world+index
    this_data = last_block.data-1000
    this_hash = last_block.self_hash
    #创建区块
    return www_block_coin(this_index, this_datastamp, this_data, this_hash)

#采用列表来存储区块，第一个数据为创世区块
www_blocks = [create_first_www_block()]

#先创建10个区块
for i in range(1,10):
    #i从1开始循环，每次调用创建区块的方法都要用上一个区块作为参数传递
    www_bolcks_add = create_many_www_coin(www_blocks[i-1])
    #将创建好的区块加入列表，即区块链
    www_blocks.append(www_bolcks_add)

for block in www_blocks:
    print(block.index,block.timestamp,block.data,block.self_hash,block.next_hash)