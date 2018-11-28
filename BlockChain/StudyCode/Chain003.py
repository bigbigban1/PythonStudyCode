import hashlib
import datetime

SHA = hashlib.sha256()

class www_block_chain(object):

    def __init__(self, index, timestamp, data, last_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.last_hash = last_hash
        self.self_hash = self.hash_self()

    def hash_self(self):
        if self.last_hash == '':
            block_info = '%s%s%s' % (self.index, self.timestamp, self.data)
        else:
            block_info = '%s%s%s%s'%(self.index,self.timestamp,self.data,self.last_hash)
        SHA.update(block_info.encode('utf-8'))
        return SHA.hexdigest()

def create_first_block():
    return www_block_chain(0,datetime.datetime.now(),9999,'')

def create_other_block(last_block):
    this_index = last_block.index+1
    this_datastamp = datetime.datetime.now()
    this_data = last_block.data-1
    #注意到这里，当前区块的自身self_hash应当为上一区块的next_hash
    this_last_hash = last_block.self_hash
    return www_block_chain(this_index, this_datastamp, this_data, this_last_hash)

www_blocks = [create_first_block()]

for i in range(1,10):
    www_blocks_add = create_other_block(www_blocks[i-1])
    www_blocks.append(www_blocks_add)

for block in www_blocks:
    print(block.index,block.timestamp,block.data,block.last_hash,block.self_hash)