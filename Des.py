#!/usr/bin/env python
#-*- coding:utf-8 -*-


class Des:


	def __init__(self,inputText,inputKey):

		self.inputText = inputText

		self.inputKey = inputKey


	def DealBin(self,bin):

		if len(bin) != 8:

			bin = '0'*(8-len(bin)) + bin

		return bin

	def HexToBin(self):

		return ''.join([self.DealBin(bin(int(text,16))[2:])[4:] for text in self.inputText])

	def AsciiToBin(self):

		return ''.join([self.DealBin(bin(int(ord(text)))[2:]) for text in self.inputText])

	def BinToAscii(self,Array):

		get = ''.join(Array)

		return ''.join([hex(int(get[i*4:(i+1)*4],2))[2:]for i in range(len(get)/4)]).upper()



	def IpSubFirst(self):

		ipTable = [
		58,50,42,34,26,18,10,2,60,52,44,36,28,20,12,4,
		62,54,46,38,30,22,14,6,64,56,48,40,32,24,16,8,
		57,49,41,33,25,17, 9,1,59,51,43,35,27,19,11,3,
		61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7]

		return [self.HexToBin()[int(i)-1] for i in ipTable]

	def TwoArrayToOne(self,Array):

		oneArray = []

		for i in Array:

			oneArray += i

		return oneArray


	def LeftAndRight(self):

		return self.IpSubFirst()[0:32],self.IpSubFirst()[32:]

	def ExtendChange(self,Array):

		extendTable = [
		32,  1,  2,  3,  4,  5,
		 4,  5,  6,  7,  8,  9,
		 8,  9, 10, 11, 12, 13,
		12, 13, 14, 15, 16, 17,
		16, 17, 18, 19, 20, 21,
		20, 21, 22, 23, 24, 25,
		24, 25, 26, 27, 28, 29,
		28, 29, 30, 31, 32, 1 ]

		left,right = Array

		return [right[int(i)-1] for i in extendTable]

	def XorKey(self,num,Array):

		return [bin(int(x)^int(y))[2:] for x,y in zip(self.ExtendChange(Array),self.inputKey.Compress(num))]

	def SboxCompress(self,inputArray,sBox):

		row = inputArray[0] + inputArray[5]

		col = ''.join(inputArray[1:5])

		getBin = bin(sBox[(int(row,2))*16+int(col,2)])[2:]

		if len(getBin) < 4:

			getBin = '0'*(4-len(getBin)) + getBin

		return getBin



	def ChoeseCompress(self,num,Array):

		sBox = [  
		[  
		0xe,0x4,0xd,0x1,0x2,0xf,0xb,0x8,0x3,0xa,0x6,0xc,0x5,0x9,0x0,0x7,  
		0x0,0xf,0x7,0x4,0xe,0x2,0xd,0x1,0xa,0x6,0xc,0xb,0x9,0x5,0x3,0x8,  
		0x4,0x1,0xe,0x8,0xd,0x6,0x2,0xb,0xf,0xc,0x9,0x7,0x3,0xa,0x5,0x0,  
		0xf,0xc,0x8,0x2,0x4,0x9,0x1,0x7,0x5,0xb,0x3,0xe,0xa,0x0,0x6,0xd,  
		],  
		[  
		0xf,0x1,0x8,0xe,0x6,0xb,0x3,0x4,0x9,0x7,0x2,0xd,0xc,0x0,0x5,0xa,  
		0x3,0xd,0x4,0x7,0xf,0x2,0x8,0xe,0xc,0x0,0x1,0xa,0x6,0x9,0xb,0x5,  
		0x0,0xe,0x7,0xb,0xa,0x4,0xd,0x1,0x5,0x8,0xc,0x6,0x9,0x3,0x2,0xf,  
		0xd,0x8,0xa,0x1,0x3,0xf,0x4,0x2,0xb,0x6,0x7,0xc,0x0,0x5,0xe,0x9,  
		],  
		[  
		0xa,0x0,0x9,0xe,0x6,0x3,0xf,0x5,0x1,0xd,0xc,0x7,0xb,0x4,0x2,0x8,  
		0xd,0x7,0x0,0x9,0x3,0x4,0x6,0xa,0x2,0x8,0x5,0xe,0xc,0xb,0xf,0x1,  
		0xd,0x6,0x4,0x9,0x8,0xf,0x3,0x0,0xb,0x1,0x2,0xc,0x5,0xa,0xe,0x7,  
		0x1,0xa,0xd,0x0,0x6,0x9,0x8,0x7,0x4,0xf,0xe,0x3,0xb,0x5,0x2,0xc,  
		],  
		[  
		0x7,0xd,0xe,0x3,0x0,0x6,0x9,0xa,0x1,0x2,0x8,0x5,0xb,0xc,0x4,0xf,  
		0xd,0x8,0xb,0x5,0x6,0xf,0x0,0x3,0x4,0x7,0x2,0xc,0x1,0xa,0xe,0x9,  
		0xa,0x6,0x9,0x0,0xc,0xb,0x7,0xd,0xf,0x1,0x3,0xe,0x5,0x2,0x8,0x4,  
		0x3,0xf,0x0,0x6,0xa,0x1,0xd,0x8,0x9,0x4,0x5,0xb,0xc,0x7,0x2,0xe,  
		],  
		[  
		0x2,0xc,0x4,0x1,0x7,0xa,0xb,0x6,0x8,0x5,0x3,0xf,0xd,0x0,0xe,0x9,  
		0xe,0xb,0x2,0xc,0x4,0x7,0xd,0x1,0x5,0x0,0xf,0xa,0x3,0x9,0x8,0x6,  
		0x4,0x2,0x1,0xb,0xa,0xd,0x7,0x8,0xf,0x9,0xc,0x5,0x6,0x3,0x0,0xe,  
		0xb,0x8,0xc,0x7,0x1,0xe,0x2,0xd,0x6,0xf,0x0,0x9,0xa,0x4,0x5,0x3,  
		],  
		[  
		0xc,0x1,0xa,0xf,0x9,0x2,0x6,0x8,0x0,0xd,0x3,0x4,0xe,0x7,0x5,0xb,  
		0xa,0xf,0x4,0x2,0x7,0xc,0x9,0x5,0x6,0x1,0xd,0xe,0x0,0xb,0x3,0x8,  
		0x9,0xe,0xf,0x5,0x2,0x8,0xc,0x3,0x7,0x0,0x4,0xa,0x1,0xd,0xb,0x6,  
		0x4,0x3,0x2,0xc,0x9,0x5,0xf,0xa,0xb,0xe,0x1,0x7,0x6,0x0,0x8,0xd,  
		],  
		[  
		0x4,0xb,0x2,0xe,0xf,0x0,0x8,0xd,0x3,0xc,0x9,0x7,0x5,0xa,0x6,0x1,  
		0xd,0x0,0xb,0x7,0x4,0x9,0x1,0xa,0xe,0x3,0x5,0xc,0x2,0xf,0x8,0x6,  
		0x1,0x4,0xb,0xd,0xc,0x3,0x7,0xe,0xa,0xf,0x6,0x8,0x0,0x5,0x9,0x2,  
		0x6,0xb,0xd,0x8,0x1,0x4,0xa,0x7,0x9,0x5,0x0,0xf,0xe,0x2,0x3,0xc,  
		],  
		[  
		0xd,0x2,0x8,0x4,0x6,0xf,0xb,0x1,0xa,0x9,0x3,0xe,0x5,0x0,0xc,0x7,  
		0x1,0xf,0xd,0x8,0xa,0x3,0x7,0x4,0xc,0x5,0x6,0xb,0x0,0xe,0x9,0x2,  
		0x7,0xb,0x4,0x1,0x9,0xc,0xe,0x2,0x0,0x6,0xa,0xd,0xf,0x3,0x5,0x8,  
		0x2,0x1,0xe,0x7,0x4,0xa,0x8,0xd,0xf,0xc,0x9,0x0,0x3,0x5,0x6,0xb,  
		],  
		]

		getKey = self.XorKey(num,Array)

		AfterCom = ''.join([self.SboxCompress(getKey [i*6:(i+1)*6],sBox[i]) for i in range(8)])

		return [i for i in AfterCom]


	def SubPbox(self,num,Array):

		pBox = [  
		16, 7,20,21,29,12,28,17,  
		1 ,15,23,26, 5,18,31,10,  
		2 ,8 ,24,14,32,27, 3, 9,  
		19,13,30, 6,22,11, 4,25]

		getCompress = self.ChoeseCompress(num,Array)

		return [getCompress[i-1] for i in pBox]

	def Final(self):

		Array = self.LeftAndRight()

		left,right = Array

		print "i=0"

		print "left:" + self.BinToAscii(left)

		print "right:" + self.BinToAscii(right)

		for i in range(16):

			print '-'*50

			print "i=" + str(i+1)

			if i < 15:

				getRight = right

				getSubBox = self.SubPbox(i,Array)
		
				right = [str(int(x)^int(y)) for x,y in zip(getSubBox,left)]

				left = getRight

				Array = (left,right)

			else:

				left = [str(int(x)^int(y)) for x,y in zip(self.SubPbox(i,Array),left)]
		
			print "left:" + self.BinToAscii(left)

			print "right:" + self.BinToAscii(right)

		return left + right

	def ConverseFirstIp(self,text):

		converseIpTable = [
		40,  8, 48, 16, 56, 24, 64, 32,
		39,  7, 47, 15, 55, 23, 63, 31,
		38,  6, 46, 14, 54, 22, 62, 30,
		37,  5, 45, 13, 53, 21, 61, 29,
		36,  4, 44, 12, 52, 20, 60, 28,
		35,  3, 43, 11, 51, 19, 59, 27,
		34,  2, 42, 10, 50, 18, 58, 26,
		33,  1, 41,  9, 49, 17, 57, 25]

		return [text[i-1] for i in converseIpTable]


	def Combine(self):

		text = self.Final()

		print '-'*50

		print 'LeftAndRightCombine:\n' + self.BinToAscii(text)

		print 'FinalSecretText:\n' + self.BinToAscii(self.ConverseFirstIp(text))





class Key:

	def __init__(self,inputKey):

		self.inputKey = inputKey

	def HexToBin(self):

		return ''.join([self.DealBin(bin(int(text,16))[2:])[4:] for text in self.inputKey])

	def DealBin(self,bin):

		if len(bin) != 8:

			bin = '0'*(8-len(bin)) + bin

		return bin

	def SubSelect(self):

		changeTable = [
			57,49,41,33,25,17, 9,  
			1 ,58,50,42,34,26,18,  
			10, 2,59,51,43,35,27,  
			19,11, 3,60,52,44,36,  
			63,55,47,39,31,23,15,  
			7 ,62,54,46,38,30,22,  
			14, 6,61,53,45,37,29,  
			21,13, 5,28,20,12, 4,]


		up = [self.HexToBin()[i-1] for i in changeTable[0:28]]

		down = [self.HexToBin()[i-1] for i in changeTable[28:]]

		return up,down

	def Move(self,Array):

		element = Array.pop(0)

		Array.append(element)

		return Array


	def CountList(self,Array,num):

		return sum([Array[i] for i in range(num)])

	def LeftMove(self,times):

		moveTimes = [
		1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

		leftArray,rightArray = self.SubSelect()

		#for i in range(moveTimes[times]):

		for i in range(self.CountList(moveTimes,times+1)):

			leftArray = self.Move(leftArray)

			rightArray = self.Move(rightArray)

		return leftArray + rightArray

	def BinToAscii(self,Array):

		get = ''.join(Array)

		return ''.join([hex(int(get[i*4:(i+1)*4],2))[2:] for i in range(len(get)/4)]).upper()


	def Compress(self,times):

		compressTable = [  
		14,17,11,24, 1, 5, 3,28,
		15, 6,21,10,23,19,12, 4, 
		26, 8,16, 7,27,20,13, 2,
		41,52,31,37,47,55,30,40, 
		51,45,33,48,44,49,39,56, 
		34,53,46,42,50,36,29,32] 

		key = [self.LeftMove(times)[i-1] for i in compressTable]

		print "key:" + self.BinToAscii(key)

		return key


def main():


	inputText = '123456ABCD132536'

	inputKey = 'AABB09182736CCDD'

	key = Key(inputKey)

	des = Des(inputText,key)

	des.Combine()



if __name__ == '__main__':

	main()