def colMean(m, col):
 """
 If col is valid return the mean of values in column col, else print "col out of bounds"
 and return.
 :param m: a matrix of numbers represented as a list of lists
 :param col: an integer that represents a valid column index of m
 :return: the float value that is the mean of the values in column col of m
 Example:
 >>> colMean([[2, 4, 6], [1, 2, 3], [1, 2, 3]], 2)
 4.0
 """
def colMode(m, col):
 """
 If col is valid return the mode of values in col else print "col out of bounds" and return.
 :param m: a matrix of integers represented as a list of lists
 :param col: an integer that represents a valid column index of m
 :return: the integer value that is the mode of the values in column col of m
 Example:
 >>> colMode([[2, 4, 6], [1, 2, 3], [1, 2, 3]], 2)
 3
 """
def colStandardize(m, col):
 """
 If col is valid return a new matrix identical to m except that the values in col are
 standardized, else print "col out of bounds" and return.
 :param m: a matrix of numbers represented as a list of lists
 :param col: an integer that represents a valid column index of m
 :return: a new matrix of the contents of m, with values in column col standardized
 Example:
 >>> colStandardize([[2, 4, 6], [1, 2, 3], [1, 2, 3]], 2)
 [ 1.155, -0.577, -0.577]
 """
def colMinMaxNormalize(m, col):
 """
 If col is valid return a new matrix identical to m except that the values in col are
 Normalized, else print "col out of bounds" and return.
 :param m: a matrix of numbers represented as a list of lists
 :param col: an integer that represents a valid column index of m
 :return: a new matrix of the contents of m with values in column col normalized between 0 and 1
 Example:
 >>> colMinMaxNormalize([[2, 4, 6], [1, 2, 3], [1, 2, 3]], 2)
 [1, 0, 0]
 """
def mutation(dna, index, newNT):
 """
 If index is valid return a string with that represents a SNP (single nucleotide
 polymorphism) of dna, else print "index out of bounds" and return.
 :param dna: a string
 :param index: an integer such that 0 <= index < len(dna)
 :param newNT: a string to replace the character at index
 :return: a string composed of the characters of dna with the value at index replaced with newNT
 Example:
 >>> mutation("ACTCGG", 0, "G")
 "GCTCGG"
 """
def insertion (dna, index, newNTs):
 """
 If index is valid return a string that represents an insertion mutation of dna,
 else print "index out of bounds" and return.
 :param dna: a string
 :param index: an integer such that 0 <= index <= len(dna)
 :param newNTs: a string to insert into dna at position index
 :return: a string composed of the characters of dna with the value at index replaced with newNT
 Examples:
 >>> insertion ("ACTCGG", 6, "AGC")
 "ACTCGGAGC"
 >>> insertion ("ACTCGG", 7, "AGC")
 "Index out of bounds"
 """
def deletion(dna, index, numNTdeleted ):
 """
 If index is valid return a string that represents a deletion mutation of dna,
 else print "index out of bounds" and return.
 :param dna: a string
 :param index: an integer such that 0 <= index < len(dna)
 :param numNTdeleted: integer indicating how many characters to delete
 :return: a string composed of the characters of dna with up to numNTdeleted beginning at position index.
 Examples:
 >>> deletion("ACTCGG", 5, 2)
 "ACTCG"
 >>> deletion("ACTCGG", 1, 2)
 " ACGG”
 """
def euclideanDistance(v1, v2):
 """
 Return the euclidean distance between vectors
 :param v1: a vector of numbers represented as a list
 :param v2: a vector of numbers represented as a list
 :return: the float value that is the Euclidean distance between v1 and v2
 Examples:
 >>> euclideanDistance([3, 1], [6, 5])
 5
 >>> euclideanDistance([0, 0], [3, 4])
 5
 """
def normalizeVector(v):
 """
 Return a new vector that is vector v normalized
 :param v: a vector of numbers represented as a list
 :return: a new vector equivalent to v scaled to length 1 (ie: a unit vector)
 Example:
 >>> normalizeVector([6, 8])
