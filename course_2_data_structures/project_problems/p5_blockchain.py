import hashlib
import datetime


class Node:
  def __init__(self, block=None):
    self.block = block
    self.next = None


class Block:
  def __init__(self, timestamp, data, previous_hash):
    self.timestamp = timestamp
    self.data = data
    self.previous_hash = previous_hash
    self.hash = self.calc_hash()

  def __str__(self):
    str_block = "Timestamp: {} \nData: {} \nSHA256 Hash: {} \nPrevious Hash: {}".format(
        self.timestamp, self.data, self.hash, self.previous_hash)
    return str_block

  def calc_hash(self):
    sha = hashlib.sha256()
    hash_str = self.data.encode('utf-8')
    sha.update(hash_str)
    return sha.hexdigest()


class Blockchain:
  def __init__(self):
    self.head = Node()

  def __str__(self):
    node = self.head
    str_blockchain = ""
    while node:
      str_blockchain += str(node.block) + '\n \n'
      node = node.next
    return str_blockchain

  def add_block(self, timestamp, data):
    if self.head.block:
      a = self.head
      block = Block(timestamp, data, a.block.hash)
      self.head = Node(block)
      self.head.next = a
    else:
      block = Block(timestamp, data, None)
      self.head = Node(block)

  def get_head(self):
    return self.head


def test():
  # test 1
  blockchain = Blockchain()
  blockchain.add_block(datetime.datetime.now(
      datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f%Z"), "first block")
  blockchain.add_block(datetime.datetime.now(datetime.timezone.utc).strftime(
      "%Y-%m-%dT%H:%M:%S.%f%Z"), "second block")
  blockchain.add_block(datetime.datetime.now(
      datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f%Z"), "third block")
  print("Test 1: normal blocks")
  print(blockchain)
  # test 2
  print("Test 2: empty blockchain")
  blockchain = Blockchain()
  print(blockchain)
  # test 3
  print("Test 3: data is empty string")
  blockchain = Blockchain()
  blockchain.add_block(datetime.datetime.now(
      datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f%Z"), "")
  print(blockchain)


if __name__ == '__main__':
  test()
