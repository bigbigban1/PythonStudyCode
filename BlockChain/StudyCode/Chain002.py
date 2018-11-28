#加密模块
import hashlib
#时间模块
import datetime

SHA = hashlib.sha256()

class www_block_chain(object):

    def __init__(self, index, timestamp, data, self_hash):
        #索引
        self.index = index
        #时间戳
        self.timestamp = timestamp
        #交易数据
        self.data = data
        #自身hash
        if self_hash == '':
            self.self_hash = self.hash_self()
        else:
            self.self_hash = self_hash
        #下一区块的hash
        self.next_hash = self.hash_next()

    #计算自身hash，也就是在创世区块时唯一调用此方法
    def hash_self(self):
        self_hash_info = ('%s%s%s')%(self.index,self.timestamp,self.data)
        SHA.update(self_hash_info.encode('utf-8'))
        return SHA.hexdigest()

    #计算下一hash，将区块的整体信息合并，作为加密的数据，注意到将其中任意一项数据改变后都会导致后面整条链的改变
    def hash_next(self):
        next_hash_info = ('%s%s%s%s')%(self.index,self.timestamp,self.data,self.self_hash)
        SHA.update(next_hash_info.encode('utf-8'))
        return SHA.hexdigest()

#创世区块的创建
def create_first_block():
    return www_block_chain(0,datetime.datetime.now(),9999,'')

#其他区块的创建
def create_other_block(last_block):
    this_index = last_block.index+1
    this_datastamp = datetime.datetime.now()
    this_data = last_block.data-1
    #注意到这里，当前区块的自身self_hash应当为上一区块的next_hash
    this_hash = last_block.next_hash
    return www_block_chain(this_index, this_datastamp, this_data, this_hash)

#采用列表存储区块，创世区块为链表的第一个元素
www_blocks = [create_first_block()]

#暂且先创建十个区块
for i in range(1,10):
    www_block_add = create_other_block(www_blocks[i-1])
    www_blocks.append(www_block_add)

#输出区块信息并验证
for block in www_blocks:
    print(block.index,block.timestamp,block.data,block.self_hash,block.next_hash)